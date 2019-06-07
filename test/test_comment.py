import pytest


class TestComment:
    @pytest.fixture
    def create_comment(self, create_story):
        project_id = create_story['project_id']
        story_id = create_story['id']
        url = f'/projects/{project_id}/stories/{story_id}/comments'
        story_data = {"text": "Comment test 01"}
        response = pytest.client.execute_request('post', url, data=story_data)
        return response.json(), project_id

    def test_get_comment(self, create_comment):
        comment, project_id = create_comment
        story_id = comment['story_id']
        url = f'/projects/{project_id}/stories/{story_id}/comments'
        response = pytest.client.execute_request('get', url)
        assert response.status_code == 200

    def test_post_comment(self, create_story):
        project_id = create_story['project_id']
        story_id = create_story['id']
        url = f'/projects/{project_id}/stories/{story_id}/comments'
        comment_data = {"text": "Comment test 01"}
        response = pytest.client.execute_request('post', url, data=comment_data)
        assert response.status_code == 200

    def test_put_story(self, create_comment):
        comment, project_id = create_comment
        story_id = comment['story_id']
        comment_id = comment['id']
        url = f'/projects/{project_id}/stories/{story_id}/comments/{comment_id}'
        comment_data = {"text": "Comment test 01-updated"}
        response = pytest.client.execute_request('put', url, data=comment_data)
        assert response.status_code == 200

    def test_delete_story(self, create_comment):
        comment, project_id = create_comment
        story_id = comment['story_id']
        comment_id = comment['id']
        url = f'/projects/{project_id}/stories/{story_id}/comments/{comment_id}'
        response = pytest.client.execute_request('delete', url)
        assert response.status_code == 204
        story = pytest.client.execute_request('get', url)
        assert story.json()['code'] == "unfound_resource"
