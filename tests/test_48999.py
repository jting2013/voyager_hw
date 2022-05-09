import json
import logging
import pytest

from github_sdk import GITHUB

from execution_utils.configurators.property_configurator import PROPERTIES


@pytest.yield_fixture()
def setup_teardown():

    github_api = GITHUB(PROPERTIES.github_url, PROPERTIES.github_token)

    yield github_api
    # teardown
    # Reset branch back to normal state
    github_api.branch.rename_branch(PROPERTIES.assignees, PROPERTIES.repo,
                                    branch='demo_edit',
                                    rename_branch='demo')


def run_rename(github_api):
    """
    Refactor to run without copy and paste
    """
    response_back = github_api.branch.rename_branch(PROPERTIES.assignees, PROPERTIES.repo,
                                                    branch='demo',
                                                    rename_branch='demo_edit')
    return response_back


def test_48953(setup_teardown):
    """
    Rename branch
    """
    github_api = setup_teardown
    response_back = run_rename(github_api)
    assert 201 == response_back.status_code
    assert PROPERTIES.assignees == response_back.json['commit']['author']['login']
    logging.info((json.dumps(response_back.json, indent=4, sort_keys=True)))

    # Second time to rename again with the previous branch name should fail
    response_back = run_rename(github_api)
    assert 422 == response_back.status_code

    logging.info(response_back.json)
    logging.info((json.dumps(response_back.json, indent=4, sort_keys=True)))
