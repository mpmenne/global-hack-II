"""
An EVE settings file that dynamically imports everything from the production
file. Then, add some of your own settings.
"""

import settings

# Copy all production setting like the EVE Domain
globals().update(settings.__dict__)

# Overwrite some globals now

MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_USERNAME = 'user'
MONGO_PASSWORD = 'BongoDrums!'
MONGO_DBNAME = 'testdb'

