#FCONTIONNNE EN LOCAL!!!!!!!!!!!!!!!!!!!!! NE PLUS TOUCHER!!!!!!!


from flask import jsonify
import pickle
import flask
import os
import requests
# Importez vos classes de recommandation

from hybrid_recommender import HybridRecommender_v1
from  content_based_recommender import ContentBasedRecommender


CLICK_PATH = "./df_clicks.pkl"
if not os.path.exists(CLICK_PATH):
    url =  "https://github.com/JulienRapacki/fontion_http_trigger/releases/download/v0/df_clicks.pkl"
    response = requests.get(url)

ARTICLES_PATH = "./df_articles.pkl"
if not os.path.exists(ARTICLES_PATH):
    url =  "https://github.com/JulienRapacki/fontion_http_trigger/releases/download/v0/df_articles.pkl"
    response = requests.get(url)
    print(response.text)
CSR_PATH = "./csr_user_item.pkl"
if not os.path.exists(CSR_PATH):
    url =  "https://github.com/JulienRapacki/fontion_http_trigger/releases/download/v0/csr_user_items.pkl"
    response = requests.get(url)

EMBEDDING_PATH = "./articles_embeddings.pickle"
if not os.path.exists(EMBEDDING_PATH):
    url =  "https://github.com/JulienRapacki/fontion_http_trigger/releases/download/v0/articles_embeddings.pickle"
    response = requests.get(url)

with open(ARTICLES_PATH, 'rb') as f:
    df_articles = pickle.load(f)
with open(CLICK_PATH, 'rb') as f:
     df_clicks_sample = pickle.load(f)
with open(CSR_PATH , 'rb') as f:
     csr_user_item = pickle.load(f)
with open('articles_embeddings.pickle', 'rb') as f:
    article_embeddings = pickle.load(f)

print(df_articles.head())


# recommender = HybridRecommender_v1(df_articles, df_clicks_sample, csr_user_item, article_embeddings)
recommender = ContentBasedRecommender(df_articles,df_clicks_sample,article_embeddings)
app = flask.Flask(__name__)

# This is the route to the API
@app.route("/")
def home():
    return "Welcome on the recommendation API ! "

@app.route("/get_recommendation/<id>", methods=["POST", "GET"])
def get_recommendation(id):

    recommendations = recommender.recommend_items(id, topn=5)
    recommendations_list = recommendations.to_dict('records')
    
    data = {
            "user" : id,
            "recommendations" : recommendations_list,
        }
    return jsonify(data)