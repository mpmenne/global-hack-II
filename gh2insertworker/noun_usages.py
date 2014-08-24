import json
import urllib
from settings import SERVER_BASE_URL

HEADERS = {'Content-Type': 'application/json'}


def get_noun_usages(http_client, noun):
    noun = urllib.quote_plus(noun)
    result = http_client.get('''{0}/noun_usages?where={{"noun": "{1}"}}'''.format(SERVER_BASE_URL, noun), headers=HEADERS)
    items = result.json()['_items']
    return items[0]['_id'] if items else []


def post_noun_usage(http_client, noun, article_id):
    payload = dict(
        noun=noun,
        article_id=article_id
    )
    result = http_client.post('{0}/noun_usages'.format(SERVER_BASE_URL), data=json.dumps(payload), headers=HEADERS)
    return result