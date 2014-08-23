import json
import requests
import connections, noun_usages, nodes, transactions, articles


def _read_data_from_file():
    data = {}
    for fname in []:
        f = open(fname, 'rb')
        data[fname] = f.read()
    return data


def parse_response_body(response_body):
    response = json.loads(response_body.data.decode('utf8'))
    try:
        return response['_id']
    except:
        raise Exception('Could not pull the field _id. Response: {0}'.format(response))


def parse_response_body_get_etag(response_body):
    id = parse_response_body(response_body)
    return id, response_body['_etag']


def build_data(http_client, article_preprocessed):
    article_data = json.loads(article_preprocessed)

    # create a new article and get its id and etag
    new_article_id, new_article_etag = parse_response_body_get_etag(
        articles.post_article(http_client, article_data.path, []))

    #create noun usages and their ids
    noun_usages_ids = []
    for noun_usage in article_data.nouns:
        add_noun_usage_response = parse_response_body(
            noun_usages.post_noun_usages(http_client, noun_usage, new_article_id))
        noun_usages_ids.append(add_noun_usage_response)

        #create node for the noun


    #attach those noun usages to article
    new_article_id, new_article_etag = articles.patch_article(http_client, new_article_id, new_article_etag,
                                                              noun_usages_ids)



