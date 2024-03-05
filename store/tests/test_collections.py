import random
from rest_framework import status
import pytest
from store.models import Collection, Product
from store.tests.conftest import authenticate_user
from model_bakery import baker


@pytest.fixture()
def create_collection(api_client):
    def do_create_collection(data):
        return api_client.post('/store/collections/', data)

    return do_create_collection


@pytest.fixture()
def create_product(api_client):
    def do_create_product(data):
        return api_client.post('/store/product/', data)

    return do_create_product


@pytest.mark.django_db
class TestCreateCollection:
    def test_if_user_is_anonymous_return_401(self, create_collection):
        response = create_collection({'title': 'a'})

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_not_admin_return_403(self, create_collection, authenticate_user):
        authenticate_user()

        response = create_collection({'title': 'a'})

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_valid_data_return_201(self, create_collection, authenticate_user):
        authenticate_user(is_staff=True)

        response = create_collection({'title': 'a'})

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['id'] > 0

    def test_invalid_data_return_400(self, create_collection, authenticate_user):
        authenticate_user(is_staff=True)

        response = create_collection({'title': ''})

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['title'] is not None


@pytest.mark.django_db
class TestRetrieveCollection:
    def test_retrieve_collection_list(self, api_client):
        response = api_client.get('/store/collections/')

        assert response.status_code == status.HTTP_200_OK

    def test_if_collection_exist_return_200(self, api_client):
        collection = baker.make(Collection)

        response = api_client.get(f'/store/collections/{collection.id}/')

        assert response.status_code == status.HTTP_200_OK
        assert response.data == {
            'id': collection.id,
            'title': collection.title,
            'products_count': 0
        }

    def test_if_collection_not_exist_return_404(self, api_client):
        collection = random.randint(0, 1000)
        response = api_client.get(f'/store/collections/{collection}/')

        assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
class TestCreateProduct:
    def test_if_user_is_anonymous_return_401(self, api_client):
        baker.make(Product)

        response = api_client.post('/store/products/')

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_not_admin_return_403(self, api_client, authenticate_user):
        authenticate_user()
        baker.make(Product)

        response = api_client.post('/store/products/')

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_valid_data_return_201(self, create_collection, authenticate_user):
        authenticate_user(is_staff=True)
        collection = baker.make(Collection)
        data = {
            "title": "test",
            "slug": "test",
            "inventory": 10,
            "price": 22,
            "collection": collection.id
        }

        response = create_collection(data)

        assert response.status_code == status.HTTP_201_CREATED

    def test_invalid_data_return_400(self, create_collection, authenticate_user):
        authenticate_user(is_staff=True)
        collection = baker.make(Collection)
        data = {
            "title": "",
            "slug": "test",
            "inventory": 10,
            "price": 22,
            "collection": collection.id
        }

        response = create_collection(data)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
