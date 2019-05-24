import pytest

from utilities.api_request import APIRequest


@pytest.fixture(scope='session', autouse=True)
def configure_api_client():
    pytest.client = APIRequest('1a77ed61bf49f50a95282757b849b099', 'https://www.pivotaltracker.com/services/v5/')


@pytest.fixture(autouse=True)
def delete_project():
    project_list = pytest.client.execute_request('get', 'projects')
    if project_list.json():
        for project in project_list.json():
            delete_url = 'projects/{}'.format(project['id'])
            pytest.client.execute_request('delete', delete_url)
