'''
This script loads local csv files into existing MongoDB Cluster
If you you haven't, install the ff libraries in your working env:
$ python -m pip install pymongoarrow
$ python -m pip install "pymongo[srv]"
$ pyhton -m pip install pandas numpy pyarrow
'''

# 1. Import libraries
import pymongoarrow
import pymongo
import pyarrow
import pandas as pd
import numpy as np
import pprint
from datetime import datetime
from pymongoarrow.monkey import patch_all
from pymongoarrow.api import write


# 2. Establish connection to MongoDB database
# Step 1) Have a MongoDB project ready, and make sure to add your IP addrress
# Step 2) Connect to your MongoDB database in Atlas UI, and select the Python driver
# Step 3) Copy the connection string provided

connection_string = "mongodb+srv://admin:BojYsM26b8SIcici@cluster0.mqvch2s.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(connection_string)

# 3. Import `.csv` files from local

# 3.1. Define file path
path_users = "/content/drive/MyDrive/social_media_analysis/users.csv"
path_posts = "/content/drive/MyDrive/social_media_analysis/posts.csv"
path_comments = "/content/drive/MyDrive/social_media_analysis/comments.csv"
path_likes = "/content/drive/MyDrive/social_media_analysis/likes.csv"

# 3.2. Load files into pd.df
df_users =  pd.read_csv(path_users)
df_posts = pd.read_csv(path_posts)
df_comments = pd.read_csv(path_comments)
df_likes = pd.read_csv(path_likes)

# 4. Define reference database, this creates a database called `sm_analytics` in your cluster
db = client.sm_analytics
# 4.1 Check if the database `sm_analytics` is already available
print(client.list_database_names())

# 5. Write pandas' df to MongoDB collections
write(db.users, df_users)  # save users collection
write(db.posts, df_posts)  # save posts collection
write(db.comments, df_comments)# save comments collection
write(db.likes, df_likes)  # save likes collection

# You can check if your collection is saved by querying to it
pprint.pprint(db.users.find_one({}))