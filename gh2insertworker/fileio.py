import json
import os
from os.path import isfile, join
from os import listdir
from settings import DATA_FOLDER


def get_filepaths(data_folder):
    text_file_paths = [join(data_folder, f) for f in listdir(data_folder) if isfile(join(data_folder, f))]
    return text_file_paths


def get_article_name_and_type(path):
    filename = os.path.basename(path)
    article_name = filename.split('-')[0]
    article_type = filename.split('-')[1].split('.')[0]
    return article_name, article_type


def group_file_names(paths):
    groups = {}
    for path in paths:
        article_name, article_type = get_article_name_and_type(path)
        if not groups.get(article_name):
            groups[article_name] = {}
        groups[article_name][article_type] = path
    return groups


def load_json_data(path):
    with open(path, 'r') as f:
        print "Opening file {0}".format(path)
        data = json.load(f)
        return data


def build_relationship_definitions(relationship, article_path):
    raw_json = load_json_data(article_path)
    results = []
    for nugget in raw_json:
        primary_node, related_node = nugget[0]
        score = nugget[1]
        results.append((primary_node, related_node, score, relationship))
    return results


def iterate_through_data_folder(handler, http_client):
    filepaths = get_filepaths(DATA_FOLDER)
    for path in filepaths:
        article_name, article_type = get_article_name_and_type(path)
        relationships = []
        for connection in build_relationship_definitions(article_type, path):
            relationships.append(connection)
        handler(http_client, article_name, relationships)
        print "Finished article name: {0}".format(article_name)
