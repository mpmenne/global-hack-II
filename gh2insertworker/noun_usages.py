import json
from settings import SERVER_BASE_URL

HEADERS = {'Content-Type': 'application/json'}


def post_noun_usages(http_client, noun, article_id):
    payload = dict(
        noun=noun,
        article_id=article_id
    )
    result = http_client.post('{0}/noun_usages'.format(SERVER_BASE_URL), data=json.dumps(payload), headers=HEADERS)
    return result