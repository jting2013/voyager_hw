"""User resource"""

from requests import Session

from github_sdk.resources.resource import Resource
from ..responses.response import Response


class User(Resource):
    """Class for user resource"""

    def __init__(self, hostname: str, token: str, rest_client: Session):
        super().__init__(hostname, rest_client, token)
        self.url = f"{hostname}/user"

    def get_user(self) -> Response:
        """
        Get user from Github
        :return: Response object
        """
        resp = self._rest_client.get(self.url, headers=self.headers)
        return Response(resp)
