import json

HEADERS = {'Content-Type': 'application/json'}


def post_connections(flask_test_client, primary_node_id, related_node_id, relationship='sibling', score=0, show=True):
    payload = dict(
        primary_node_id=primary_node_id,
        related_node_id=related_node_id,
        relationship=relationship,
        score=score,
        show=show,

    )
    result = flask_test_client.post('/api/v1/connections', data=json.dumps(payload), headers=HEADERS)
    return result