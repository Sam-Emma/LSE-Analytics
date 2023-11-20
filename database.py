from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import json
import pandas as pd
class MongoDB:
    def __init__(self):
        uri = "mongodb+srv://doadmin:T0vG235psA9Xz617@db-mongodb-nyc3-29417-af6dac8b.mongo.ondigitalocean.com/admin?tls=true&authSource=admin"
        # Create a new client and connect to the server
        client = MongoClient(uri, server_api=ServerApi('1'))
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        # Select the database
        db = client["lse_data"]
        self.db = db
    
    def post(self, collection: str, data: dict) -> None:
        db = self.db
        collect = db[collection]
        print(data)
        json_str = json.dumps(data)
        tasks_dict = json.loads(json_str)
        collect.insert_one(tasks_dict)
        print("done")
    
    def get(self, collection: str, query: dict):
        data = [] # get roles from database or API based on user_id and company_id
        db = self.db
        collection = db[collection]
        print("fetching...")
        print(query)
        results = collection.find(query)
        for result in results:
            data.append(result)
        print(pd.DataFrame(data).columns)
        print("done")
        return data