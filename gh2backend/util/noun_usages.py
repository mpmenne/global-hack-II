import json

HEADERS = {'Content-Type': 'application/json'}


def post_noun_usages(flask_test_client, noun, article_id):
    payload = dict(
        noun=noun,
        article_id=article_id
    )
    result = flask_test_client.post('/api/v1/noun_usages', data=json.dumps(payload), headers=HEADERS)
    return result