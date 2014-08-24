from eve import Eve
import os
from util import builder, fileio

app = Eve(settings=os.path.join(
    os.path.dirname(os.path.realpath(__file__)), 'settings.py'))


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/generate')
def generate():
    http_client = app.test_client()
    handler = builder.build_data
    fileio.iterate_through_data_folder(handler, http_client)
    print 'OK!'


def add_score(items):
    connections = app.data.driver.db['connections']
    connection = connections.find_one({'_id': items[0]['related_connection_id']})
    if connection:
        connections.update({'_id': connection['_id']},
                           {"$inc": {"score": items[0]['score_delta']}})
        # print("Score change +{0} to {1}".format(
        #     items[0]['score_delta'],
        #     connections.find_one({'_id': items[0]['related_connection_id']})['score']
        # ))

app.on_insert_transactions += add_score


if __name__ == '__main__':

    app.run('0.0.0.0')
