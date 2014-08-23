import json
import os
from unittest import TestCase
from gh2insertworker import fileio
from gh2insertworker.fileio import iterate_through_data_folder
from gh2insertworker.settings import DATA_FOLDER


MOCK_DATA = """[[["scene",
"injuri"],
9],
[["scene",
"man"],
9],
[["injuri",
"man"],
9],
[["scene",
"mall"],
6]]"""


class TestWorkerFileIO(TestCase):


    def setUp(self):
        pass

    def test_get_paths(self):
        result = fileio.get_filepaths(DATA_FOLDER)
        self.assertTrue(result)

    def test_group_file_names(self):
        paths = fileio.get_filepaths(DATA_FOLDER)
        result = fileio.group_file_names(paths)
        self.assertTrue(result)

    def test_load_json_data(self):
        path = os.path.join(DATA_FOLDER, '81184-siblings.json')
        result = fileio.load_json_data(path)
        self.assertTrue(result)

    def test_build_relationships(self):
        mock_data = json.loads(MOCK_DATA)
        result = fileio.build_relationship_definitions(mock_data, 'sibling')
        self.assertTrue(result)

    def test_file_io(self):
        result = iterate_through_data_folder()
        self.assertTrue(result)