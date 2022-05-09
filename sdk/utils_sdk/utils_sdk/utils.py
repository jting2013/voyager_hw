"""
Module for holding utilities
"""

import logging
import os
import shutil
import time
from typing import List, Dict


def sleep(seconds: int):
    """
    Go to sleep for specified amount of seconds and log information about sleep start/end

    :param seconds: Time in seconds to sleep
    :return: None

    :Example:

    The following example will perform sleep for 30 seconds

    .. code-block:: python

        from utils_sdk import sleep
        sleep(30)
    """
    logging.info("sleep('{}') start".format(seconds))
    time.sleep(seconds)
    logging.info("sleep end")


def _appl_details_str_to_dict(appl_info: str) -> Dict[str, str]:
    """
    Convert string with information about appliance to dictionary

    :param appl_info: Information about appliance string
    :return: Dictionary with appliance details

    :Example:

    .. code-block:: python

        from utils_sdk.utils import _appl_details_str_to_dict

        appl_info = '''
        IP:			10.15.0.33
        Node:			20b9500b-2558-4485-a629-8233aa01c4f5.ffcfd64b-6c3b-4432-9c58-9f1d7b55a281
        applCreateOrder:	1
        IPMs:			imprivataG3-7-0-99, appliancex64-2017-8-21
        partOfEnterprise:	1
        setupStatus:		Done
        tunnelPort:		9200
        auditServer:		1
        fqdn:			europalviv.imp.eng
        SID:			V1024054
        Serial Number:		VAG3000004
        '''
        appl_dict = _appl_details_str_to_dict(appl_info)
        print(appl_dict["IP"])
        >> 10.15.0.33'
    """
    appl_params = filter(None, appl_info.split('\n'))
    appl_dict = dict()
    for appl_param in appl_params:
        key, value = appl_param.split(":")
        appl_dict[key] = value.strip()
    return appl_dict


def _parse_enterprise_details(details_str: str) -> List[Dict[str, str]]:
    """
    Convert enterprise details string to list of dictionaries
    where each dictionary contains details about one appliance in enterprise

    :param details_str: Enterprise details as string with details for all appliances in enterprise
    :return: List of dictionaries with appliances details
    """
    separator = "-" * 143

    appl_details_list = filter(None, details_str.split(separator))
    details = list()
    for appl_details in appl_details_list:
        details.append(_appl_details_str_to_dict(appl_details))
    return details


def get_enterprise_details(archive_path: str) -> List[Dict[str, str]]:
    """
    Get enterprise details from tar.gz file

    :param archive_path: Full path to archive with enterprise downloaded details files
    :return: List of dictionaries with appliances details
        where each dictionary contains details about one appliance in enterprise

    :Example:

    The following example will get enterprise details from tar.gz file

    .. code-block:: python

        from utils_sdk import get_enterprise_details

        enterprise_details = (get_enterprise_details("C:\\archives\\my_arch.tar.gz"))
        for appliance_details in enterprise_details:
            print(appliance_details["IP"])

        >>10.153.159.135
        >>10.153.159.151
        >>10.153.159.158
    """
    try:
        unpack_path = archive_path.split('.')[0]
        shutil.unpack_archive(archive_path, unpack_path)
        logging.info("UtilsSDK: Archive from path '{}' was successfully unpacked to path '{}'".format(archive_path,
                                                                                                      unpack_path))

        enterprise_details_file = [f for f in os.listdir(unpack_path) if (f.endswith('.txt')
                                                                          and f.startswith("enterpriseDetails"))]
        with open("{}/{}".format(unpack_path, enterprise_details_file[0]), "r") as details_file:
            enterprise_details = details_file.read()
        shutil.rmtree(unpack_path, ignore_errors=True)
        logging.info("UtilsSDK: Enterprise details were received successfully")
        return _parse_enterprise_details(enterprise_details)
    except Exception as msg:
        logging.warning("UtilsSDK: Could not get enterprise details. Exception occurred. Message = {}".format(msg))
