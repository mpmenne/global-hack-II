import json

HEADERS = {'Content-Type': 'application/json'}

def post_noun(flask_test_client, noun_name, hypernyms, hyponyms):
    payload = dict(
        text=noun_name,
        hypernyms=hypernyms,
        hyponyms=hyponyms
    )
    result = flask_test_client.post('/api/v1/nouns', data=json.dumps(payload), headers=HEADERS)
    return result
