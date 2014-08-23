import json
from settings import SERVER_BASE_URL

HEADERS = {'Content-Type': 'application/json'}


def post_transactions(http_client, related_connection_id, score_delta, transaction_type):
    payload = dict(
        related_connection_id=related_connection_id,
        score_delta=score_delta,
        transaction_type=transaction_type,

    )
    result = http_client.post('{0}/transactions'.format(SERVER_BASE_URL), data=json.dumps(payload), headers=HEADERS)
    return result