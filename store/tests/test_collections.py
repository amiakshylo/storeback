from rest_framework.test import APIClient
from rest_framework import status
import pytest
from django.contrib.auth.models import User

@pytest.mark.django_db
class TestCreateCollection:
    def test_if_user_is_anonynous_return_401(self):
        client = APIClient()
        response = client.post('/store/collections/', {'title': 'a'})
        assert response.status_code == status.HTTP_401_UNAUTHORIZED #type: ignore
        
    def test_if_user_is_not_admin_return_403(self):
        client = APIClient()
        client.force_authenticate(user={})
        response = client.post('/store/collections/', {'title': 'a'})
        assert response.status_code == status.HTTP_403_FORBIDDEN #type: ignore
        
    def test_valid_data_return_201(self):
        client = APIClient()
        client.force_authenticate(user=User(is_staff=True))
        response = client.post('/store/collections/', {'title': 'a'})
        assert response.status_code == status.HTTP_201_CREATED #type: ignore
        assert response.data['id'] > 0 #type: ignore
        
    def test_invalid_data_return_400(self):
        client = APIClient()
        client.force_authenticate(user=User(is_staff=True))
        response = client.post('/store/collections/', {'title': ''})
        assert response.status_code == status.HTTP_400_BAD_REQUEST #type: ignore
        assert response.data['title'] is not None #type: ignore
        
        

    