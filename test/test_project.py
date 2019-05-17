import pytest

from utilities.api_request import APIRequest


class TestProject:
    def test_get_projects(self):
        request = APIRequest('1a77ed61bf49f50a95282757b849b099', 'https://www.pivotaltracker.com/services/v5/')
        response = request.execute_request('get', 'projects')
        assert response.status_code == 200
