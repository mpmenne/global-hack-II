from eve import Eve
import os
import nounifier

app = Eve(settings=os.path.join(
    os.path.dirname(os.path.realpath(__file__)), 'settings.py'))


@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run('0.0.0.0')
