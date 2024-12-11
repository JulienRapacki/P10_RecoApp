from content_based_recommender import ContentBasedRecommender
from collaborative_filtering_recommender import CollaborativeRecommender
import pandas as pd

class HybridRecommender_v1:
    def __init__(self, articles_df, interaction_df, interactions_matrix, article_embeddings):
        self.articles_df = articles_df
        self.interaction_df = interaction_df
        self.interactions_matrix = interactions_matrix
        self.article_embeddings = article_embeddings
        
        self.content_recommender = ContentBasedRecommender(self.articles_df, self.interaction_df, self.article_embeddings)
        self.collab_recommender = CollaborativeRecommender(self.interaction_df, self.interactions_matrix)

    def recommend_items(self, user_id, items_to_ignore=[], topn=10):
        # Logique de combinaison des recommandations
        content_recs = self.content_recommender.recommend_items(user_id=user_id , items_to_ignore=items_to_ignore, topn=topn).head(3)
        collab_recs = self.collab_recommender.recommend_items(user_id, items_to_ignore=items_to_ignore, topn=topn).head(2)
        
        # Combiner/pondérer les recommandations
        hybrid_recs = self._combine_recommendations(content_recs, collab_recs)
        
        return content_recs #hybrid_recs[:topn]

    def _combine_recommendations(self, content_recs, collab_recs):
        # Implémentez ici la logique de combinaison des recommandations
        # Par exemple, une moyenne pondérée des scores
        combined_recs = pd.concat([content_recs, collab_recs])
        combined_recs = combined_recs.groupby('click_article_id')['recStrength'].min().reset_index()
        return combined_recs.sort_values('recStrength', ascending=False)

    def get_model_name(self):
        return "Hybrid Recommender v1"