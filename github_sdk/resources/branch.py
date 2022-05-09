"""User resource"""

from requests import Session

from github_sdk.resources.resource import Resource
from ..responses.response import Response


class Branch(Resource):
    """Class for branch resource"""

    def __init__(self, hostname: str,
                 token: str,
                 rest_client: Session):
        super().__init__(hostname, rest_client, token)
        self.base = f"{hostname}/repos"

    def rename_branch(self, owner, repo, branch, rename_branch) -> Response:
        """
        Rename the branch from Github
        :param owner: Owner of the name
        :param repo: Repo of the name
        :param branch: Branch name to be rename
        :param rename_branch: Rename the branch
        :return: Response object
        """
        api_url = f'{self.base}/{owner}/{repo}/branches/{branch}/rename'
        json_body = {'new_name': rename_branch}
        resp = self._rest_client.post(api_url, json=json_body, headers=self.headers)
        return Response(resp)
