from eve import Eve
import os
from flask import send_file
from util import builder, fileio

app = Eve(settings=os.path.join(os.path.dirname(os.path.realpath(__file__)), 'settings.py'),
          static_folder=os.path.join(os.path.dirname(os.path.realpath(__file__)), 'static'))

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/generate')
def generate():
    http_client = app.test_client()
    handler = builder.build_data
    fileio.iterate_through_data_folder(handler, http_client)
    print 'OK!'


rdf_filename = os.path.join('static', 'output.rdf')


@app.route('/genrdf')
def gen_rdf():
    prefix = "\n".join(["@prefix node:   <http://65.254.105.147:5000/api/v1/nodes#> .",
                        "@prefix connection: <http://65.254.105.147:5000/api/v1/connections#> . "])

    THRESH_HOLD = 10

    data = app.data.driver.db['connections'].find({'score': {'$gt': THRESH_HOLD}}).sort("score")

    entries = []

    with open(rdf_filename, 'w') as f:
        f.write(prefix)
        f.write('\n')

        for datum in data:
            primary_node_name = app.data.driver.db['nodes'].find_one({"_id": datum['primary_node_id']})['noun']
            related_node_name = app.data.driver.db['nodes'].find_one({"_id": datum['related_node_id']})['noun']

            entry = "node:" + str(primary_node_name) + " "
            entry += "connection:" + datum['relationship'] + " "
            entry += "node:" + str(related_node_name)
            entry += " .\n"

            f.writelines(entry)

    return 'ok'


@app.route('/genkingrdf')
def king_rdf():
    prefix = "\n".join(["@prefix node:   <http://65.254.105.147:5000/api/v1/nodes#> .",
                        "@prefix connection: <http://65.254.105.147:5000/api/v1/connections#> . "])

    THRESH_HOLD = 40

    data = app.data.driver.db['connections'].find(
        {'score': {'$gt': THRESH_HOLD}, 'primary_node_id': "53f98d525eb55f19786653fc"}).sort("score")

    entries = []

    with open('static\\king.rdf', 'w') as f:
        f.write(prefix)
        f.write('\n')

        for datum in data:
            primary_node_name = app.data.driver.db['nodes'].find_one({"_id": datum['primary_node_id']})['noun']
            related_node_name = app.data.driver.db['nodes'].find_one({"_id": datum['related_node_id']})['noun']

            entry = "node:" + str(primary_node_name) + " "
            entry += "connection:" + datum['relationship'] + " "
            entry += "node:" + str(related_node_name)
            entry += " .\n"

            f.writelines(entry)

    return 'ok'


def add_score(items):
    connections = app.data.driver.db['connections']
    connection = connections.find_one({'_id': items[0]['related_connection_id']})
    if connection:
        connections.update({'_id': connection['_id']},
                           {"$inc": {"score": items[0]['score_delta']}})
        # print("Score change +{0} to {1}".format(
        # items[0]['score_delta'],
        # connections.find_one({'_id': items[0]['related_connection_id']})['score']
        # ))


app.on_insert_transactions += add_score

if __name__ == '__main__':
    app.run('0.0.0.0')
