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
    SERVER_NAME = '65.254.105.147:5000'

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
        'noun': {
            'type': 'string'
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
        }
    }
}

connections = {
    # 'title' tag used in item links.
    'item_title': 'connection',
    # Schema definition, based on Cerberus grammar. Check the Cerberus project
    # (https://github.com/nicolaiarocci/cerberus) for details.
    'schema': {
        'primary_node_id': {
            'type': 'objectid',
            'data_relation': {
                'resource': 'nodes'
            }
        },
        'related_node_id': {
            'type': 'objectid',
            'data_relation': {
                'resource': 'nodes'
            }
        },
        'relationship': {
            'type': 'string',
            'allowed': ['parent', 'uncle', 'siblings', 'children']
        },
        'score': {
            'type': 'integer',
            'default': 5
        },
        'show': {
            'type': 'boolean'
        }
    }
}

transactions = {
    'item_title': 'transaction',
    'schema': {
        'related_connection_id': {
            'type': 'objectid',
            'data_relation': {
                'resource': 'connections'
            }
        },
        'score_delta': {
            'type': 'integer'
        },
        'transaction_type': {
            'type': 'string',
            'allowed': ['nltk', 'human', 'articles']
        }
    }
}

noun_usages = {
    # 'title' tag used in item links.
    'item_title': 'noun_usage',
    # Schema definition, based on Cerberus grammar. Check the Cerberus project
    # (https://github.com/nicolaiarocci/cerberus) for details.
    'schema': {
        'noun': {
            'type': 'string',
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


# The DOMAIN dict explains which resources will be available and how they will
# be accessible to the API consumer.
DOMAIN = {
    'articles': articles,
    'noun_usages': noun_usages,
    'nodes': nodes,
    'connections': connections,
    'transactions': transactions,
}
