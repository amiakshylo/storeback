import json
import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset


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


class RecommendationDataset(Dataset):
    def __init__(self, interactions):
        self.user_product_interactions = interactions

    def __len__(self):
        return len(self.user_product_interactions)

    def __getitem__(self, idx):
        user_id, product_id, interaction = self.user_product_interactions[idx]
        return torch.tensor(user_id, dtype=torch.long), torch.tensor(product_id, dtype=torch.long), torch.tensor(
            interaction, dtype=torch.float)


def load_data():
    views_df = pd.read_csv('store/recommendations/product_views.csv')
    orders_df = pd.read_csv('store/recommendations/order_items.csv')

    interactions = []
    for index, row in views_df.iterrows():
        interactions.append((row['user_id'], row['product_id'], 1))

    for index, row in orders_df.iterrows():
        interactions.append((row['order__customer_id'], row['product_id'], 1))

    user_ids = set(views_df['user_id']).union(set(orders_df['order__customer_id']))
    product_ids = set(views_df['product_id']).union(set(orders_df['product_id']))

    return interactions, list(user_ids), list(product_ids)


def train_model():
    interactions, user_ids, product_ids = load_data()

    num_users = max(user_ids) + 1
    num_products = max(product_ids) + 1
    embedding_size = 50

    print(f"Training Model with num_users={num_users}, num_products={num_products}, embedding_size={embedding_size}")

    dataset = RecommendationDataset(interactions)
    dataloader = DataLoader(dataset, batch_size=32, shuffle=True)

    model = NCFModel(num_users, num_products, embedding_size)
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    for epoch in range(10):
        total_loss = 0
        for user_ids_batch, product_ids_batch, interactions_batch in dataloader:
            optimizer.zero_grad()
            outputs = model(user_ids_batch, product_ids_batch)
            loss = criterion(outputs, interactions_batch)
            loss.backward()
            optimizer.step()
            total_loss += loss.item()

        print(f'Epoch {epoch + 1}, Loss: {total_loss}')

    model_path = 'store/recommendations/recommendation_model.pth'
    torch.save(model.state_dict(), model_path)

    metadata = {
        'num_users': num_users,
        'num_products': num_products,
        'embedding_size': embedding_size
    }

    metadata_path = 'store/recommendations/metadata.json'
    with open(metadata_path, 'w') as f:
        json.dump(metadata, f)

    print("Training complete and metadata generated successfully.")
    print(f"Metadata: num_users={num_users}, num_products={num_products}, embedding_size={embedding_size}")


if __name__ == '__main__':
    train_model()
