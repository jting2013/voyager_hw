"""
Module for base GITHUB response
"""

import logging as log
from typing import Dict

import requests


class Response:
    """
    Class for Base GITHUB response
    """

    def __init__(self, response: requests.Response):
        """
        :param response: Object, which contains a server's response to HTTP request
        """
        self.response = response

    @property
    def status_code(self):
        """
        Return status code of response

        :return: Status code
        """
        try:
            return self.response.status_code
        except Exception as msg:
            log.error("GITHUB: Exception occurred: {}".format(msg))
            raise

    @property
    def headers(self) -> Dict:
        """
        Return all headers

        :return: Dictionary with headers names and values
        """
        try:
            return self.response.headers
        except Exception as msg:
            log.error("GITHUB: Exception occurred: {}".format(msg))
            raise

    def get_header(self, header_name: str) -> str:
        """
        Return header value by name

        :param header_name: Name of header
        :return: Header value
        """
        try:
            return self.response.headers[header_name]
        except Exception as msg:
            log.error("GITHUB: Exception occurred: {}".format(msg))
            raise

    @property
    def content(self) -> str:
        """
        Return content of the response as string

        :return: Content of the response
        """
        try:
            return self.response.content.decode()
        except Exception as msg:
            log.error("GITHUB: Exception occurred: {}".format(msg))
            raise

    @property
    def json(self) -> Dict:
        """
        Return json from the response

        :return: Content of the response
        """
        try:
            return self.response.json()
        except Exception as msg:
            log.error("GITHUB: Exception occurred: {}".format(msg))
            raise

    @property
    def url(self) -> str:
        """
        Return URL of the response as string

        :return: Response URL
        """
        try:
            return self.response.url
        except Exception as msg:
            log.error("GITHUB: Exception occurred: {}".format(msg))
            raise
