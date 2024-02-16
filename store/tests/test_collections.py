from rest_framework.test import APIClient
from rest_framework import status
import pytest


@pytest.mark.django_db
class TestCreateCollection:
    def test_if_user_is_anonynous_return_401(self):
        client = APIClient()
        response = client.post('/store/collections/', {})
        assert response.status_code == status.HTTP_401_UNAUTHORIZED #type: ignore
        
    def test_if_user_is_not_admin_return_403(self):
        client = APIClient()
        client.force_authenticate(user={'login': 'admin', 'password': ''})
        response = client.post('/store/collections/', {'title': 'a'})
        assert response.status_code == status.HTTP_403_FORBIDDEN #type: ignore
        
        

    