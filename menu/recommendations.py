from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from .models import FoodItem

def calculate_vector():
    food_items = FoodItem.objects.all()

    food_id_mapping = {food_item.food_title: food_item.id for food_item in food_items}
    id_food_mapping = {v: k for k, v in food_id_mapping.items()}

    descriptions = [f"{food_item.food_title} {food_item.category} {food_item.slug} {food_item.description}" for food_item in food_items]

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(descriptions)

    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

    return food_id_mapping, id_food_mapping, cosine_sim, food_items


def get_recommendations(food_title, top_n=5):
    food_id_mapping, _, cosine_sim, food_items = calculate_vector()

    food_id = food_id_mapping[food_title]
    food_idx = list(food_id_mapping.values()).index(food_id)

    sim_scores = list(enumerate(cosine_sim[food_idx]))

    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    top_items = [item for item in sim_scores if item[1] >= 0.002][:6]

    top_food_items = [food_items[item[0]] for item in top_items]

    return top_food_items