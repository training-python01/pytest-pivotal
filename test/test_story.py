import pytest


class TestStory:
    def test_get_story(self, create_project):
        project_id = create_project['id']
        url = f'/projects/{project_id}/stories'
        response = pytest.client.execute_request('get', url)
        assert response.status_code == 200

    def test_post_story(self, create_project):
        project_id = create_project['id']
        url = f'/projects/{project_id}/stories'
        story_data = {"name": "Story test 01"}
        response = pytest.client.execute_request('post', url, data=story_data)
        assert response.status_code == 200

    def test_put_story(self, create_story):
        project_id = create_story['project_id']
        story_id = create_story['id']
        url = f'/projects/{project_id}/stories/{story_id}'
        story_data = {"name": "Story test 01-updated"}
        response = pytest.client.execute_request('put', url, data=story_data)
        assert response.status_code == 200

    def test_delete_story(self, create_story):
        project_id = create_story['project_id']
        story_id = create_story['id']
        url = f'/projects/{project_id}/stories/{story_id}'
        response = pytest.client.execute_request('delete', url)
        assert response.status_code == 204
        story = pytest.client.execute_request('get', url)
        assert story.json()['code'] == "unfound_resource"
