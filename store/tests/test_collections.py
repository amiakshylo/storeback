from rest_framework import status
import pytest
from django.contrib.auth.models import User

@pytest.fixture()
def create_collection(api_client):
    def do_create_collection(data):
        return api_client.post('/store/collections/', data)
    return do_create_collection
       

@pytest.mark.django_db
class TestCreateCollection:
    def test_if_user_is_anonynous_return_401(self, create_collection):
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
        
        

    