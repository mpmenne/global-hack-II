import json
import urllib
from settings import SERVER_BASE_URL

HEADERS = {'Content-Type': 'application/json'}


def get_connection(http_client, primary_id, related_id):
    result = http_client.get(
        '''{0}/connections?where={{"primary_node_id":"{1}","related_node_id":"{2}"}}'''.format(SERVER_BASE_URL,
                                                                                               primary_id,
                                                                                               related_id),
        headers=HEADERS)
    items = result.json()['_items']
    return items[0]['_id'] if items else []


def post_connections(http_client, primary_node_id, related_node_id, relationship='sibling', score=0, show=True):
    payload = dict(
        primary_node_id=primary_node_id,
        related_node_id=related_node_id,
        relationship=relationship,
        score=score,
        show=show,

    )
    result = http_client.post('{0}/connections'.format(SERVER_BASE_URL), data=json.dumps(payload), headers=HEADERS)
    return result