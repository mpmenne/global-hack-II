import json
import urllib

HEADERS = {'Content-Type': 'application/json'}


def get_nodes(http_client, noun):
    noun = urllib.quote_plus(noun)
    result = http_client.get('''/api/v1/nodes?where={{"noun": "{0}"}}'''.format(noun), headers=HEADERS)
    items = json.loads(result.data)['_items']
    return items[0]['_id'] if items else []


def post_nodes(flask_test_client, noun, show):
    payload = dict(
        noun=noun,
        show=show,
        noun_usages=[]
    )
    result = flask_test_client.post('/api/v1/nodes', data=json.dumps(payload), headers=HEADERS)
    return result