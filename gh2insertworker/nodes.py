import json
from settings import SERVER_BASE_URL

HEADERS = {'Content-Type': 'application/json'}


def post_nodes(http_client, noun, show, noun_usages):
    payload = dict(
        noun=noun,
        show=show,
        noun_usages=noun_usages
    )
    result = http_client.post('{0}/nodes'.format(SERVER_BASE_URL), data=json.dumps(payload), headers=HEADERS)
    return result