#from flask_pymongo import MongoClient, ASCENDING, DESCENDING
from pymongo import MongoClient
import os
#mongo_ip = "172.17.0.8"
"""Setting up database connection using flask PyMongo"""

mongo_ip = "localhost"
mongo_port = 27017

#mongo = MongoClient(os.environ['DB_PORT_27017_TCP_ADDR'],27017)
#db = client.tododb

mongo = MongoClient("mongodb://localhost:27017")
lms=mongo['lms']
 