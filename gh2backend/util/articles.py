import json

HEADERS = {'Content-Type': 'application/json'}


def post_article(flask_test_client, path, noun_usages):
    payload = dict(
        path=path,
        noun_usages=noun_usages
    )
    result = flask_test_client.post('/api/v1/articles', data=json.dumps(payload), headers=HEADERS)
    return result


def patch_article(flask_test_client, id, etag, noun_usages):
    payload = dict(
        id=id,
        etag=etag,
        noun_usages=noun_usages
    )
    result = flask_test_client.patch('/api/v1/articles/{0}'.format(id), data=json.dumps(payload),
                                     headers={'Content-Type': 'application/json', 'If-Match': etag})
    return result

