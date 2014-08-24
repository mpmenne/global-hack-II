import json
import urllib
from settings import SERVER_BASE_URL

HEADERS = {'Content-Type': 'application/json'}


def get_nodes(http_client, noun):
    noun = urllib.quote_plus(noun)
    result = http_client.get('''{0}/nodes?where={{"noun": "{1}"}}'''.format(SERVER_BASE_URL, noun), headers=HEADERS)
    items = result.json()['_items']
    return items[0]['_id'] if items else []

def post_nodes(http_client, noun, show):
    payload = dict(
        noun=noun,
        show=show,
        noun_usages=[]
    )
    result = http_client.post('{0}/nodes'.format(SERVER_BASE_URL), data=json.dumps(payload), headers=HEADERS)
    return result