import requests
from gh2insertworker import builder
from gh2insertworker import fileio

if __name__ == "__main__":

    http_client = requests
    handler = builder.build_data
    fileio.iterate_through_data_folder(handler, http_client)