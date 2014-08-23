import os
from gh2backend import wsgi_app
from unittest import TestCase
from eve import Eve
from pymongo import MongoClient
from gh2backend import nounifier
from gh2backend import util
from gh2backend.tests.settings_test_py import MONGO_HOST, MONGO_PORT, MONGO_DBNAME, \
    MONGO_USERNAME, MONGO_PASSWORD

blob = """An aide to Libya's Prime Minister Ali Zeidan has been kidnapped on the outskirts of the capital, Tripoli, government officials say.

Mohamed al-Ghattous is believed to have been seized on Sunday in the Ghot al-Roman district as he was driving from his hometown of Misrata.

His car was found abandoned and the authorities have launched a search.

Also on Sunday, Mr Zeidan warned that members of his government had received death threats.

He told a routine news briefing they were working under "very difficult conditions" since coming to power four months ago.

A cabinet source, speaking anonymously, told AFP news agency Mr Ghattous "was without doubt taken at a fake checkpoint".

It is thought the kidnappers could have been posing as security personnel in South America.

"Nobody knows where he is. They left his car behind, probably they thought it could be traced," a government source told the Associated Press.

The BBC's Rana Jawad in Tripoli says there has been a sharp increase in security threats against the cabinet since the government announced it was taking steps to disarm and disband the militias.

Last week, the prime minister's building was briefly surrounded by an armed group demanding his resignation, and on Sunday, the justice ministry was similarly surrounded for several hours.

The government is still struggling to consolidate its powers over the many militias which formed after the war that toppled Col Muammar Gaddafi.

But out correspondent says there is a widespread view amongst Libyans that their government has become seriously locked in a power struggle with militias trying to keep their influence on the streets of Libya."""



class TestNounifier(TestCase):

    def setUp(self):
        settings_path = os.path.join(os.path.dirname(
        os.path.realpath(__file__)), 'settings_test_py.py')
        self.setupDB()
        self.app = Eve(settings=settings_path)
        self.test_client = wsgi_app.app.test_client()

    def tearDown(self):
        self.dropDB()

    def setupDB(self):
        self.connection = MongoClient(MONGO_HOST, MONGO_PORT)
        self.connection.drop_database(MONGO_DBNAME)
        if MONGO_USERNAME:
            self.connection[MONGO_DBNAME].add_user(MONGO_USERNAME,
                                                   MONGO_PASSWORD)

    def bulk_insert(self):
        pass

    def dropDB(self):
        self.connection = MongoClient(MONGO_HOST, MONGO_PORT)
        self.connection.drop_database(MONGO_DBNAME)
        self.connection.close()

    def test_get_nouns(self):
        result = nounifier.find_nouns(blob)
        self.assertTrue(len(result)>90)

    def test_get_noun_related_words(self):
        result = nounifier.get_noun_related_words('cardinal')
        self.assertTrue(result)

    def test_post_internal_noun(self):

        noun = 'cardinal'
        data = nounifier.get_noun_related_words(noun)

        result = util.nouns.post_noun(self.test_client, noun, **data)
        self.assertEqual(result.status_code, 201)
