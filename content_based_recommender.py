import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


class ContentBasedRecommender:

    MODEL_NAME = 'Content-Based'

    def __init__(self, articles_df, interaction_df, article_embeddings):
        self.article_df = articles_df
        self.interaction_df = interaction_df
        self.article_embeddings = article_embeddings
        self.item_ids = articles_df['article_id'].tolist()

    def get_model_name(self):
        return self.MODEL_NAME

    def _get_similar_items_to_user_profile(self,person_id, topn=5000000):
        # Listing des artciles vus par l'utilisateur
        person_id = int(person_id)
        user_items = self.interaction_df[self.interaction_df.index == person_id]['click_article_id'].to_list()
        if not user_items:
            return []  
        # Création d'un profil utilisateur avec les embeddings des articles consultés
        user_profile = np.mean([self.article_embeddings[self.item_ids.index(item)] for item in user_items if item in self.item_ids], axis=0)

        
        # Calcul de la similarité entre le profil utilisateur est tous les articles disponibles
        similarities = cosine_similarity([user_profile], self.article_embeddings)[0]

        # Articles similaires au profil utilisateur en excluant la liste des articles déjà vus
        similar_indices = similarities.argsort()[::-1]
        similar_items = [(self.item_ids[i], similarities[i]) for i in similar_indices if self.item_ids[i] not in user_items]

        return similar_items[:topn]



    def recommend_items(self, user_id, items_to_ignore=[], topn=5, verbose=False):
        similar_items = self._get_similar_items_to_user_profile(user_id)
        #Ignores items the user has already interacted
        similar_items_filtered = list(filter(lambda x: x[0] not in items_to_ignore, similar_items))

        recommendations_df = pd.DataFrame(similar_items_filtered, columns=['click_article_id', 'recStrength']) \
                                    .head(topn)

        if verbose:
            if self.items_df is None:
                raise Exception('"items_df" is required in verbose mode')

            recommendations_df = recommendations_df.merge(self.items_df, how = 'left',
                                                          left_on = 'click_article_id',
                                                          right_on = 'contentId')[['recStrength', 'contentId', 'title', 'url', 'lang']]


        return recommendations_df

# content_based_recommender_model = ContentBasedRecommender(df_articles,df_clicks,article_embeddings)