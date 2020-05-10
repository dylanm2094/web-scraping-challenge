import os
from dotenv import load_dotenv

load_dotenv()
conn = f"mongodb://dylanm20:{os.environ.get('password')}@cluster0-shard-00-00-4mnmj.mongodb.net:27017,cluster0-shard-00-01-4mnmj.mongodb.net:27017,cluster0-shard-00-02-4mnmj.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority"