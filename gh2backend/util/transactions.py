import json

HEADERS = {'Content-Type': 'application/json'}


def post_transactions(flask_test_client, related_connection_id, score_delta, transaction_type):
    payload = dict(
        related_connection_id=related_connection_id,
        score_delta=score_delta,
        transaction_type=transaction_type,

    )
    result = flask_test_client.post('/api/v1/transactions', data=json.dumps(payload), headers=HEADERS)
    return result