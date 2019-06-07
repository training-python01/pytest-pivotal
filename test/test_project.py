import pytest

from utilities import common_utils


class TestProject:
    def test_get_projects(self, create_project):
        project = create_project
        project_id = project['id']
        response = pytest.client.execute_request('get', f'projects/{project_id}')
        assert response.status_code == 200
        assert common_utils.schema_validation('project_schema.json', response.json())

    def test_post_projects(self):
        project = {"name": "Project01Test"}
        response = pytest.client.execute_request('post', 'projects', data=project)
        assert response.status_code == 200
        assert common_utils.validate_data(response.json(), project)

    def test_put_projects(self, create_project):
        project_id = create_project['id']
        url = f'projects/{project_id}'
        project = {"name": "Project01Test - updated"}
        response = pytest.client.execute_request('put', url, data=project)
        assert response.status_code == 200

    def test_delete_projects(self, create_project):
        project_id = create_project['id']
        url = f'projects/{project_id}'
        response = pytest.client.execute_request('delete', url)
        assert response.status_code == 204
