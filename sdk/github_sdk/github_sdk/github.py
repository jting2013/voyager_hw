"""Contains main class for manipulating with GITHUB"""

import requests

from .resources.user import User
from .resources.branch import Branch
from .resources.issues import Issues


class GITHUB:
    """
    GITHUB Class
    """

    def __init__(self, hostname: str, token: str):
        """
        :param hostname: github hostname
        :param token: access token
        """
        self.hostname = "https://{}".format(hostname.rstrip("/")) if not hostname.startswith("http") \
            else hostname.rstrip("/")

        self._rest_client = requests.Session()
        self.user = User(self.hostname, token, self._rest_client)
        self.branch = Branch(self.hostname, token, self._rest_client)
        self.issues = Issues(self.hostname, token, self._rest_client)
