from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
from dotenv import load_dotenv

load_dotenv()
URI = os.getenv("MONGODB_URI")
DB_NAME = os.getenv("DB_NAME")
BOOK_COLL = os.getenv("BOOK_COLL")
client = MongoClient(URI, server_api=ServerApi('1'))
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
    
db = client[DB_NAME]

book_coll = db[BOOK_COLL]
