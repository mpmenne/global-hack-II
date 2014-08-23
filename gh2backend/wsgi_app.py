from eve import Eve
import os
from gh2backend import nounifier

app = Eve(settings=os.path.join(
    os.path.dirname(os.path.realpath(__file__)), 'settings.py'))


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/generate_mock_data')
def generate_mock_data():
    return nounifier.build_data(app.test_client)


if __name__ == '__main__':
    app.run()
