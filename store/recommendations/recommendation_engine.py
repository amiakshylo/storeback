import logging

import torch
import torch.nn as nn


class NCFModel(nn.Module):
    def __init__(self, num_users, num_items, embedding_dim):
        super(NCFModel, self).__init__()
        self.user_embedding = nn.Embedding(num_users, embedding_dim)
        self.item_embedding = nn.Embedding(num_items, embedding_dim)
        self.fc_layers = nn.Sequential(
            nn.Linear(embedding_dim * 2, 128),
            nn.ReLU(),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, 32),
            nn.ReLU(),
            nn.Linear(32, 1)
        )

    def forward(self, user_indices, item_indices):
        user_embedding = self.user_embedding(user_indices)
        item_embedding = self.item_embedding(item_indices)
        concat = torch.cat([user_embedding, item_embedding], dim=-1)
        return self.fc_layers(concat).squeeze()


def load_model(model_path, num_users, num_products, embedding_size):
    model = NCFModel(num_users, num_products, embedding_size)
    state_dict = torch.load(model_path)

    # Handle mismatched keys and sizes
    model_state_dict = model.state_dict()
    for k, v in state_dict.items():
        if k in model_state_dict and model_state_dict[k].shape == v.shape:
            model_state_dict[k] = v
        else:
            print(f"Ignored key {k} due to shape mismatch or unexpected key.")

    model.load_state_dict(model_state_dict)
    model.eval()
    return model


def load_metadata(metadata_path):
    import json
    with open(metadata_path, 'r') as f:
        metadata = json.load(f)
    num_users = metadata['num_users']
    num_products = metadata['num_products']
    embedding_size = metadata['embedding_size']
    return num_users, num_products, embedding_size


# def recommend_products(user_id, model, product_ids, top_k=10):
#     model.eval()
#     user_tensor = torch.tensor([user_id], dtype=torch.long)
#     valid_product_ids = [pid for pid in product_ids if pid < model.item_embedding.num_embeddings]
#     product_tensor = torch.tensor(valid_product_ids, dtype=torch.long)
#
#     with torch.no_grad():
#         scores = model(user_tensor.repeat(len(valid_product_ids)), product_tensor)
#
#     if len(valid_product_ids) < top_k:
#         top_k = len(valid_product_ids)
#
#     _, recommended_indices = torch.topk(scores, top_k)
#     recommended_products = [valid_product_ids[idx] for idx in recommended_indices]
#
#     return recommended_products

def recommend_products(user_id, model, product_ids, top_k=10):
    model.eval()
    user_tensor = torch.tensor([user_id], dtype=torch.long)

    # Handle missing product IDs
    valid_product_ids = [pid for pid in product_ids if pid < model.item_embedding.num_embeddings]
    missing_product_ids = [pid for pid in product_ids if pid not in valid_product_ids]
    if len(missing_product_ids) > 0:
        logging.warning(f"Encountered {len(missing_product_ids)} missing product IDs during recommendation.")

    product_tensor = torch.tensor(valid_product_ids, dtype=torch.long)

    with torch.no_grad():
        # Option 1: Efficient Top-K selection with smaller k initially
        # topk_scores, topk_indices = torch.topk(scores, min(top_k, len(valid_product_ids)))
        # recommended_indices = torch.topk(topk_scores, top_k)[1]  # Select top k from top min(top_k, len(valid_product_ids))

        # Option 2: Utilize GPU-accelerated sorting (if applicable)
        scores = model(user_tensor.repeat(len(valid_product_ids)), product_tensor)
        _, sorted_indices = torch.sort(scores, descending=True)
        recommended_indices = sorted_indices[:top_k]

    recommended_products = [valid_product_ids[idx] for idx in recommended_indices]

    return recommended_products
