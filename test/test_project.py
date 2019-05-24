import pytest

class TestProject:

    @pytest.fixture
    def create_project(self):
        project = {"name": "Project01Test"}
        response = pytest.client.execute_request('post', 'projects', data=project)
        return response.json()

    def test_get_projects(self):
        response = pytest.client.execute_request('get', 'projects')
        assert response.status_code == 200

    def test_post_projects(self):
        project = {"name": "Project01Test"}
        response = pytest.client.execute_request('post', 'projects', data=project)
        assert response.status_code == 200

    def test_put_projects(self, create_project):
        project = create_project
        url = 'projects/{}'.format(project['id'])
        project = {"name": "Project01Test - updated"}
        response = pytest.client.execute_request('put', url, data=project)
        assert response.status_code == 200

    def test_delete_projects(self, create_project):
        project = create_project
        url = 'projects/{}'.format(project['id'])
        response= pytest.client.execute_request('delete', url)
        assert response.status_code == 204