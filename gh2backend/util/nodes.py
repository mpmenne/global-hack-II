import json

HEADERS = {'Content-Type': 'application/json'}


def post_nodes(flask_test_client, noun, show, noun_usages):
    payload = dict(
        noun=noun,
        show=show,
        noun_usages=noun_usages
    )
    result = flask_test_client.post('/api/v1/nodes', data=json.dumps(payload), headers=HEADERS)
    return result