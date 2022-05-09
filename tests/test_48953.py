
import pytest

from github_sdk import GITHUB

from execution_utils.configurators.property_configurator import PROPERTIES


@pytest.yield_fixture()
def setup_teardown():

    github_api = GITHUB(PROPERTIES.github_url, PROPERTIES.github_token)

    yield github_api
    # teardown
    print('complete teardown')


def test_48953(setup_teardown):
    """
    Get User and verify it's the right token access to the username
    """
    github_api = setup_teardown
    response_back = github_api.user.get_user()

    assert 200 == response_back.status_code
    assert PROPERTIES.assignees == response_back.json['login']
