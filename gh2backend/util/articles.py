import json

HEADERS = {'Content-Type': 'application/json'}


def post_article(flask_test_client, path, noun_usages):
    payload = dict(
        path=path,
        noun_usages=noun_usages
    )
    result = flask_test_client.post('/api/v1/articles', data=json.dumps(payload), headers=HEADERS)
    return result
