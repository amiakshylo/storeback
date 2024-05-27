import numpy as np

from store.recommendations.recommendation_engine import load_model, recommend_products, load_metadata
from store.recommendations import recommendation_model

# Load data for evaluation
evaluation_data = recommendation_model.load_data()


def precision_at_k(recommended, relevant, k):
    recommended_at_k = recommended[:k]
    relevant_set = set(relevant)
    relevant_recommended = [1 if item in relevant_set else 0 for item in recommended_at_k]
    return np.sum(relevant_recommended) / k


def recall_at_k(recommended, relevant, k):
    recommended_at_k = recommended[:k]
    relevant_set = set(relevant)
    relevant_recommended = [1 if item in relevant_set else 0 for item in recommended_at_k]
    return np.sum(relevant_recommended) / len(relevant)


def mean_average_precision(recommendations):
    aps = []
    for user_id, recommended, relevant in recommendations:
        relevant_set = set(relevant)
        ap = 0.0
        hits = 0.0
        for i, item in enumerate(recommended):
            if item in relevant_set:
                hits += 1.0
                ap += hits / (i + 1.0)
        aps.append(ap / len(relevant))
    return np.mean(aps)


def mean_reciprocal_rank(recommendations):
    rr = []
    for user_id, recommended, relevant in recommendations:
        for rank, item in enumerate(recommended, start=1):
            if item in relevant:
                rr.append(1.0 / rank)
                break
        else:
            rr.append(0)
    return np.mean(rr)


def evaluate_recommendations():
    interactions, user_ids, product_ids = evaluation_data

    metadata_path = 'store/recommendations/metadata.json'
    num_users, num_products, embedding_size = load_metadata(metadata_path)
    model_path = 'store/recommendations/recommendation_model.pth'
    model = load_model(model_path, num_users, num_products, embedding_size)

    recommendations = []
    for user_id, product_id, interaction in interactions:
        recommended_product_ids = recommend_products(user_id, model, product_ids)
        relevant_product_ids = [product_id]

        print(f"User ID: {user_id}")
        print(f"Recommended: {recommended_product_ids[:10]}")
        print(f"Relevant: {relevant_product_ids}")

        recommendations.append((user_id, recommended_product_ids, relevant_product_ids))

    k = 5
    precision_scores = [precision_at_k(rec, rel, k) for _, rec, rel in recommendations]
    recall_scores = [recall_at_k(rec, rel, k) for _, rec, rel in recommendations]
    map_score = mean_average_precision(recommendations)
    mrr_score = mean_reciprocal_rank(recommendations)

    print(f"Precision@{k}: {np.mean(precision_scores)}")
    print(f"Recall@{k}: {np.mean(recall_scores)}")
    print(f"MAP: {map_score}")
    print(f"MRR: {mrr_score}")


if __name__ == '__main__':
    evaluate_recommendations()
