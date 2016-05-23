#!/bin/env python
from pymongo import MongoClient
import simplejson as json
import sys

def main(connstring):
    mc = MongoClient(connstring, connectTimeoutMS=1000)
    db = mc['admin']
    print( json.dumps(db.command("serverStatus"), indent=4, sort_keys=True ))


if __name__ == "__main__":
    main(sys.argv[1])
