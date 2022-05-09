"""
Base resource
"""

from requests import Session


class Resource:
    """
    Base class for all resources
    """

    def __init__(self, hostname: str, rest_client: Session, token: str):
        self.hostname = hostname
        self.headers = {'content-type': 'application/json',
                        'accept': 'application/vnd.github.v3+json',
                        'Authorization': f'token {token}'}
        self._rest_client = rest_client
