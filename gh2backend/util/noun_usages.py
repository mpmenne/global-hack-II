import json
import urllib

HEADERS = {'Content-Type': 'application/json'}


def get_noun_usages(http_client, noun):
    noun = urllib.quote_plus(noun)
    result = http_client.get('''/api/v1/noun_usages?where={{"noun": "{0}"}}'''.format(noun), headers=HEADERS)
    items = json.loads(result.data)['_items']
    return items[0]['_id'] if items else []


def post_noun_usage(flask_test_client, noun, article_id):
    payload = dict(
        noun=noun,
        article_id=article_id
    )
    result = flask_test_client.post('/api/v1/noun_usages', data=json.dumps(payload), headers=HEADERS)
    return result