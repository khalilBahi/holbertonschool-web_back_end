#!/usr/bin/env python3
""" function that inserts a new document in a collection based on kwargs"""
import pymongo


def insert_school(mongo_collection, **kwargs):   
    """Return new id"""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
