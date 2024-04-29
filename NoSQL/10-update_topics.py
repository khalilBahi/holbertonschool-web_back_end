#!/usr/bin/env python3
"""function that changes all topics of a school document based on the name"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """Return new id"""
    name = {"name": name}
    topics = {"$set": {"topics": topics}}
    mongo_collection.update_many(name, topics)
    