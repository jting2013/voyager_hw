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
    print('complete teardown')


def test_48953(setup_teardown):
    """
    Create a github issue
    """
    github_api = setup_teardown
    response_back = github_api.issues.create_issues(PROPERTIES.assignees, PROPERTIES.repo,
                                                    title='Issues to be create',
                                                    body=f'Just placing some issues here so we can take a look at it',
                                                    assignees=PROPERTIES.assignees,
                                                    labels='bug')

    assert 201 == response_back.status_code

    logging.info(response_back.json)
    logging.info((json.dumps(response_back.json, indent=4, sort_keys=True)))
