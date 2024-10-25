#!/usr/bin/env python3

""" Function that lists all documents in a collection """

# from pymongo import MongoClient


def list_all(mongo_collection):
    """ Function that lists all documents in a collection """
    if mongo_collection is None:
        return []
    else:
        return list(mongo_collection.find())
