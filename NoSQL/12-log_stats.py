#!/usr/bin/env python3
"""
This script connects to a MongoDB
instance and analyzes Nginx logs stored in a collection.
"""

from pymongo import MongoClient


if __name__ == "__main__":
    # Connect to the local MongoDB instance
    client = MongoClient("mongodb://127.0.0.1:27017")

    # Access the Nginx logs collection
    nginx_collection = client.logs.nginx

    # Count the total number of logs in the collection
    logs = nginx_collection.count_documents({})

    # Print the total number of logs
    print(f"{logs} logs")

    # Define a list of HTTP methods to analyze
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    # Count the number of logs for each HTTP method
    method_counts = {
        method: nginx_collection.count_documents({"method": method})
        for method in methods
    }

    # Print the number of logs for each HTTP method
    print("Methods:")
    for method, count in method_counts.items():
        print(f"\tmethod {method}: {count}")

    # Count the number of GET requests to the '/status' path
    status_count = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )

    # Print the number of GET requests to the '/status' path
    print(f"{status_count} status check")
