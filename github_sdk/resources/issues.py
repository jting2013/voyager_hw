"""Issues resource"""

from requests import Session

from github_sdk.resources.resource import Resource
from ..responses.response import Response


class Issues(Resource):
    """Class for issues resource"""

    def __init__(self, hostname: str,
                 token: str,
                 rest_client: Session):
        super().__init__(hostname, rest_client, token)
        self.base = f"{hostname}/repos"

    def create_issues(self, owner: str, repo: str, title: str, body: str, assignees: str, labels: str) -> Response:
        """
        Rename the branch from Github
        :param owner: The account owner of the repository. The name is not case sensitive.
        :param repo: The name of the repository. The name is not case sensitive.
        :param title: The title of the issue.
        :param body: The contents of the issue.
        :param assignees: Logins for Users to assign to this issue.
        :param labels: Labels to associate with this issue.
        :return: Response object
        """
        api_url = f'{self.base}/{owner}/{repo}/issues'
        json_body = {'title': title, 'body': body,
                     'assignees': [assignees], 'labels': [labels]}
        resp = self._rest_client.post(api_url, json=json_body, headers=self.headers)
        return Response(resp)
