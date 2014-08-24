import json
import requests
from gh2insertworker import connections

import noun_usages
import articles
import nodes
import transactions


def _read_data_from_file():
    data = {}
    for fname in []:
        f = open(fname, 'rb')
        data[fname] = f.read()
    return data


def parse_response_body(response_body):
    response = response_body.json()
    try:
        return response['_id']
    except:
        raise Exception('Could not pull the field _id. Response: {0}'.format(response))


def parse_response_body_get_etag(response_body):
    id = parse_response_body(response_body)
    return id, response_body.json()['_etag']


def build_data(http_client, article_name, relationships):
    # create a new article and get its id and etag
    new_article_id, new_article_etag = parse_response_body_get_etag(
        articles.post_article(http_client, article_name, []))

    line = 1
    for primary, related, score, relationship in relationships:

        try:
            print "{0}/{1} Processing primary: {2}".format(line, len(relationships), primary)
            line += 1
        except UnicodeEncodeError:
            pass
        # create noun usages and their ids for the primary
        existing_primary_noun = noun_usages.get_noun_usages(http_client, primary)
        if not existing_primary_noun:
            add_noun_usage_response = parse_response_body(
                noun_usages.post_noun_usage(http_client, primary, new_article_id))


        # create noun usages and their ids for the related
        existing_related_noun = noun_usages.get_noun_usages(http_client, primary)
        if not existing_related_noun:
            add_noun_usage_response = parse_response_body(
                noun_usages.post_noun_usage(http_client, related, new_article_id))


        # create node for the primary
        existing_primary_id = nodes.get_nodes(http_client, primary)
        if not existing_primary_id:
            add_primary_node_id = parse_response_body(
                nodes.post_nodes(http_client, primary, True))
        else:
            add_primary_node_id = existing_primary_id

        # create node for the related
        existing_secondary_id = nodes.get_nodes(http_client, related)
        if not existing_secondary_id:
            add_related_node_id = parse_response_body(
                nodes.post_nodes(http_client, related, True))
        else:
            add_related_node_id = existing_secondary_id

        # create connections
        existing_connection_id = connections.get_connection(http_client, add_primary_node_id, add_related_node_id)
        if not existing_connection_id:
            add_connections_id, add_connections_etag = parse_response_body_get_etag(
                connections.post_connections(http_client, add_primary_node_id, add_related_node_id, relationship))
        else:
            add_connections_id = existing_connection_id

        add_transaction_id = parse_response_body(
            transactions.post_transactions(http_client, add_connections_id, score, 'nltk'))


