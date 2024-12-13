import pickle
import os
import pandas as pd
import requests
class CollaborativeRecommender:
    
    
    
    MODEL_NAME = 'Collaborative Filtering'
    MODEL_PATH = "./collab_model_weights.pkl"
    
    #Chargement des poids du modèle collaboratif à partir d'une GitHub Release
    if not os.path.exists(MODEL_PATH):
        url = " https://github.com/JulienRapacki/fontion_http_trigger/releases/download/v0/collab_model_weights.pkl"
        response = requests.get(url)
    
    
    
    def __init__(self, interaction_df, user_item, model_path=MODEL_PATH):
        self.user_item = user_item
        self.model_path = model_path
        with open(self.model_path, 'rb') as filehandle:
            self.collaborative_model = pickle.load(filehandle)
        
    def get_model_name(self):
        return self.MODEL_NAME

    def recommend_items(self, person_id, items_to_ignore=[], topn=5, verbose=False):
        
        # Convert user_id to int if it's not already
        user_id = int(person_id)
        
        # Get recommendations
        reco = self.collaborative_model.recommend(user_id, self.user_item[user_id], N=topn, filter_already_liked_items=True)
        

        # Dataframe de recommendations
        result = pd.DataFrame({'click_article_id': reco[0], 'recStrength': reco[1]})
        
        # Filtre les articles déjà consultés
        result = result[~result['click_article_id'].isin(items_to_ignore)]
        
        # Filtre top n
        result = result.head(topn)

        return result

