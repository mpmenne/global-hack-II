# -*- coding: utf-8 -*-

"""
    eve-demo settings
    ~~~~~~~~~~~~~~~~~

    Settings file for our little demo.

    PLEASE NOTE: We don't need to create the two collections in MongoDB.
    Actually, we don't even need to create the database: GET requests on an
    empty/non-existant DB will be served correctly ('200' OK with an empty
    collection); DELETE/PATCH will receive appropriate responses ('404' Not
    Found), and POST requests will create database and collections when needed.
    Keep in mind however that such an auto-managed database will most likely
    perform poorly since it lacks any sort of optimized index.

    :copyright: (c) 2013 by Nicola Iarocci.
    :license: BSD, see LICENSE for more details.
"""

import os

# We want to seamlessy run our API both locally and on Heroku so:
if os.environ.get('PORT'):
    # We're hosted on Heroku!  Use the MongoHQ sandbox as our backend.
    MONGO_HOST = 'alex.mongohq.com'
    MONGO_PORT = 10047
    MONGO_USERNAME = 'evedemo'
    MONGO_PASSWORD = 'evedemo'
    MONGO_DBNAME = 'app9346575'

    # also, correctly set the API entry point
    SERVER_NAME = 'eve-demo.herokuapp.com'
else:
    # Running on local machine. Let's just use the local mongod instance.
    # db.addUser( { user: "user", pwd: "BongoDrums!", roles: [ "readWrite" ] } )
    MONGO_HOST = 'localhost'
    MONGO_PORT = 27017
    MONGO_USERNAME = 'user'
    MONGO_PASSWORD = 'BongoDrums!'
    MONGO_DBNAME = 'maindb'

    # let's not forget the API entry point (not really needed anyway)
    #SERVER_NAME = '127.0.0.1:5000'

URL_PREFIX = 'api'
API_VERSION = 'v1'

# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

# Enable reads (GET), edits (PATCH) and deletes of individual items
# (defaults to read-only item access).
ITEM_METHODS = ['GET', 'PATCH', 'DELETE']

# We enable standard client cache directives for all resources exposed by the
# API. We can always override these global settings later.
CACHE_CONTROL = 'max-age=20'
CACHE_EXPIRES = 20

# Our API will expose two resources (MongoDB collections): 'people' and
# 'works'. In order to allow for proper data validation, we define beaviour
# and structure.


nodes = {
    # 'title' tag used in item links.
    'item_title': 'node',
    # Schema definition, based on Cerberus grammar. Check the Cerberus project
    # (https://github.com/nicolaiarocci/cerberus) for details.
    'schema': {
        'noun_id': {
            'type': 'objectid',
            'data_relation': {
                'resource': 'nouns'
            }
        },
        'show': {
            'type': 'boolean'
        },
        'noun_usages': {
            'type': 'list',
            'schema': {
            'type': 'objectid',
                'data_relation': {
                    'resource': 'noun_usages'
                }
            }
        },
        'parents': {
            'type': 'list',
            'schema': {
            'type': 'objectid',
                'data_relation': {
                    'resource': 'connections'
                }
            }
        },
        'children': {
            'type': 'list',
            'schema': {
            'type': 'objectid',
                'data_relation': {
                    'resource': 'connections'
                }
            }
        }

    }
}

connections = {
    # 'title' tag used in item links.
    'item_title': 'connection',
    # Schema definition, based on Cerberus grammar. Check the Cerberus project
    # (https://github.com/nicolaiarocci/cerberus) for details.
    'schema': {
        'parent_node_id': {
            'type': 'objectid',
            'data_relation': {
                'resource': 'nodes'
            }
        },
        'child_node_id': {
            'type': 'objectid',
            'data_relation': {
                'resource': 'nodes'
            }
        },
        'score': {
            'type': 'integer'
        }
    }
}

noun_usages = {
    # 'title' tag used in item links.
    'item_title': 'noun_usage',
    # Schema definition, based on Cerberus grammar. Check the Cerberus project
    # (https://github.com/nicolaiarocci/cerberus) for details.
    'schema': {
        'noun_id': {
            'type': 'objectid',
            'data_relation': {
                'resource': 'nouns'
            }
        },
        'article_id': {
            'type': 'objectid',
            'data_relation': {
                'resource': 'articles'
            }
        },
    }
}

articles = {
    # 'title' tag used in item links.
    'item_title': 'article',
    # Schema definition, based on Cerberus grammar. Check the Cerberus project
    # (https://github.com/nicolaiarocci/cerberus) for details.
    'schema': {
        'path': {
            'type': 'string',
            'required': True,
        },
        'noun_usages': {
            'type': 'list',
            'schema': {
            'type': 'objectid',
                'data_relation': {
                    'resource': 'noun_usages'
                }
            }
        }
    }
}

nouns = {
    'item_title': 'noun',
    # Schema definition, based on Cerberus grammar. Check the Cerberus project
    # (https://github.com/nicolaiarocci/cerberus) for details.
    'schema': {
        'text': {
            'type': 'string',
            'unique': True,
            'required': True,
        },
        'hyponyms': {
            'type': 'list',
            'schema': {
                'type': 'string'
            }
        },
        'hypernyms': {
            'type': 'list',
            'schema': {
                'type': 'string'
            }
        },
    }
}


# The DOMAIN dict explains which resources will be available and how they will
# be accessible to the API consumer.
DOMAIN = {
    'nouns': nouns,
    'articles': articles,
    'noun_usages': noun_usages,
    'nodes': nodes,
    'connections': connections,
}
