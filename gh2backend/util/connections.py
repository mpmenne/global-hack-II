import json

HEADERS = {'Content-Type': 'application/json'}


def get_connection(http_client, primary_id, related_id):
    result = http_client.get(
        '''/api/v1/connections?where={{"primary_node_id":"{0}","related_node_id":"{1}"}}'''.format(primary_id,
                                                                                                   related_id),
        headers=HEADERS)
    items = json.loads(result.data)['_items']
    return items[0]['_id'] if items else []


def post_connections(flask_test_client, primary_node_id, related_node_id, relationship='sibling', show=True):
    payload = dict(
        primary_node_id=primary_node_id,
        related_node_id=related_node_id,
        relationship=relationship,
        show=show,
    )
    result = flask_test_client.post('/api/v1/connections', data=json.dumps(payload), headers=HEADERS)
    return result