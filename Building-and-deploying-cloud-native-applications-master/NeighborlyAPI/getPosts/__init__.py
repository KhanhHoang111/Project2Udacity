import logging
import azure.functions as func
import pymongo
import json
import os
from bson.json_util import dumps


def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Python getPosts trigger function processed a request.')

    try:
        url = os.environ["mongoDBConnection"]  # TODO: Update with appropriate MongoDB connection information
        client = pymongo.MongoClient(url)
        database = client['mymongodb1']
        collection = database['posts']

        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8', status_code=200)
    except:
        return func.HttpResponse("Bad request.", status_code=400)
