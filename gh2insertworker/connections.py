import json
from settings import SERVER_BASE_URL

HEADERS = {'Content-Type': 'application/json'}


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