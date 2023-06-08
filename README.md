# social_media_analysis 💬
  
  
This analyzes social media engagement data. The dataset contains user interactions such as likes, comments, posts, and user demographics. Analysis is done in python, while data is stored in MongoDB.

There are three files on this repo:
## 🐍 [00_load_local_to_mongodb.py](https://github.com/TheLastMonolith/social_media_analysis/blob/main/00_load_local_to_mongodb.py)
- This script is used to upload the .csv files into our existing MongoDB Cluster - `sm_analytics`
## 📔 [01_mongodb_queries.ipynb](https://github.com/TheLastMonolith/social_media_analysis/blob/main/01_mongodb_queries.ipynb)
- This report walks you through a quick EDA for our collections. I used [PyMongo](https://pypi.org/project/pymongo/) to interact with the MongoDB database using python as my driver.
## 📔 [02_nlp_social_media_engagement_analysis.ipynb](https://github.com/TheLastMonolith/social_media_analysis/blob/main/02_nlp_social_media_engagement_analysis.ipynb)
- This report walks you through on how I analyzed each collection, and performed NLP techniques such as TF-IDF, Topic Modeling, and Sentiment Analysis.
    
    
  
    
## Author  
Joseph Figuracion  
  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/josephfiguracion/)
