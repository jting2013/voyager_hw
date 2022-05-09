"""
Setup test data before test execution
"""

import random
import os
import string

from utils_sdk import Properties


PROPERTIES = Properties()


class PropertyConfigurator:
    """
    Contains methods to setup test data necessary for test execution
    """

    _config_file = None
    _json_file = None

    @classmethod
    def initialize(cls, config_file: str):
        """
        Initialize config file to work with

        :param config_file: Name of config file
        :param reuse_previous_test_data: If True, test data from previous execution will be used.
            If False, new test data will be generated
        :return: None
        """
        base_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

        cls._config_file = os.path.abspath("{}/configuration/{}".format(base_path, config_file))


    @classmethod
    def setup(cls):
        """
        Generate test data and store it in PROPERTIES object
        """
        PROPERTIES.append_config_data(cls._config_file)
        PROPERTIES.report_file = os.path.basename(cls._config_file).replace('config', 'report').replace('.ini', '.xml')
        PROPERTIES.allure_report_folder = "{}/{}".format(PROPERTIES.allure_report_path,
                                                         PROPERTIES.report_file.split(".")[0])
