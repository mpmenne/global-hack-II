from eve import Eve
import os
import nounifier

app = Eve(settings=os.path.join(
    os.path.dirname(os.path.realpath(__file__)), 'settings.py'))


@app.route('/')
def hello_world():
    return 'Hello World!'


def add_score(items):
    connections = app.data.driver.db['connections']
    connection = connections.find_one({'related_connection_id': items[0]['related_connection_id']})
    # account = connections.insert(docs)
    print connection

app = Eve()
app.on_insert_transactions += add_score

if __name__ == '__main__':
    app.run('0.0.0.0')
