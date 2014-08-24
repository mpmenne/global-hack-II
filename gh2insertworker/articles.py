import json
from settings import SERVER_BASE_URL

HEADERS = {'Content-Type': 'application/json'}


def post_article(http_client, path, noun_usages):
    payload = dict(
        path=path,
        noun_usages=noun_usages
    )
    result = http_client.post('{0}/articles'.format(SERVER_BASE_URL), data=json.dumps(payload), headers=HEADERS)
    return result


def patch_article(http_client, id, etag):

    result = http_client.patch('{0}/articles/{1}'.format(SERVER_BASE_URL, id),
                                     headers={'Content-Type': 'application/json', 'If-Match': etag})
    return result

