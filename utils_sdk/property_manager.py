"""
Holder for external properties
"""

import configparser
import json
import os


class PropertyError(Exception):
    """
    Exception related to property manager
    """
    pass


def get_property(config_file: str, property_name: str, section_name: str = None) -> str:
    """
    Get property value from config file

    :param config_file: Path to config file
    :param property_name: Name of property to get value from
    :param section_name: Name of section to which property belongs. Optional parameter.
        If not set, method will look for property in all sections
    :return: Property value as a string
    :raises PropertyError: If property or section or config file doesn't exist

    :Example:

        The code below will get value of property "my_property" from file "C:\\config.ini"

        | Content of config.ini:
        | -------------
        | [my_section]
        | property_1 = value_1
        | ...
        | my_property = my_value
        | ....
        | property_n = value_n
        | -------------

        .. code-block:: python

            from utils_sdk import get_property

            print(get_property("C:\\config.ini", "my_property"))
            my_value

            # or

            print(get_property("C:\\config.ini", "my_property", "my_section"))
            my_value
    """
    try:
        config = configparser.ConfigParser()
        config.optionxform = str
        config.read(config_file)
        if section_name is not None:
            return config.get(section_name, property_name)

        for section in config.sections():
            for option in config.options(section):
                if option == property_name:
                    return config.get(section, option)
    except Exception as msg:
        raise PropertyError(msg)
    raise PropertyError("Cannot get property (property file or property doesn't exist)")


def set_property(config_file: str, property_name: str, value: str, section_name: str = None):
    """
    Set property value to config file

    :param config_file: Path to config file
    :param property_name: Name of property to set value to
    :param value: Value to be set to property
    :param section_name: Name of section to which property belongs. Optional parameter.
        If not set, method will look for property in all sections
    :return: None
    :raises PropertyError: If property or section or config file doesn't exist

    :Example:

        The code below will set value of property "my_property" from file "C:\\config.ini" to "my_new_value"

        | Content of config.ini:
        | -------------
        | [my_section]
        | property_1 = value_1
        | ...
        | my_property = my_value
        | ....
        | property_n = value_n
        | -------------

        .. code-block:: python

            from utils_sdk import get_property

            set_property("C:\\config.ini", "my_property", "my_new_value")

            # or

            set_property("C:\\config.ini", "my_property", "my_new_value", "my_section"))
            my_value

    """
    if not os.path.exists(config_file):
        raise PropertyError("Property file doesn't exist")

    config = configparser.ConfigParser()
    config.optionxform = str
    config.read(config_file)
    try:
        if section_name is not None and property_name in config.options(section_name):
            config.set(section_name, property_name, value)
        else:
            for section in config.sections():
                if property_name in config.options(section):
                    config.set(section, property_name, value)
                    break
        with open(config_file, 'w') as configfile:
            config.write(configfile)
    except Exception as msg:
        raise PropertyError(msg)


class Properties:
    """
    Holder for external properties
    """
    def __init__(self):
        super().__setattr__('_properties', {})

    def __getattr__(self, item):
        try:
            return self._properties[item]
        except KeyError:
            raise AttributeError

    def __setattr__(self, key, value):
        self._properties[key] = value

    def __repr__(self):
        return str(self._properties)

    def append_config_data(self, config_file: str):
        """
        Get config data from config file and append it into object

        :param config_file: Path to config file
        :return: None

        :Example:

        Get all properties from file C:\\\\config.ini that has properties in format key = value
        and append them to object

        .. code-block:: python

            from utils_sdk import Properties

            # Read properties into object
            props = Properties()
            props.append_config_data("C:\\config.ini")

            # Manage properties
            print(props.endpoint_ip)
            10.11.12.13

        """

        config = configparser.ConfigParser()
        config.optionxform = str
        config.read(config_file)
        for section in config.sections():
            for option in config.options(section):
                self._properties[option] = config.get(section, option)

    def deserialize(self, file_path: str):
        """
        Read all properties from .json file into object

        :param file_path: Path to .json file
        :return: None

        :Example:

        .. code-block:: python

            from utils_sdk import Properties

            # Read properties into object
            props = Properties()
            props.deserialize("C:\\test_data.json")

            # Manage properties
            print(props.ad_user3_name)
            Pwmponj3

            props.ad_user3_name = "Abra"
            print(props.ad_user3_name)
            Abra
        """
        with open(file_path, 'r') as data_file:
            loaded_dict = json.load(data_file)
        for key, value in loaded_dict.items():
            setattr(self, key, value)

    def serialize(self, file_path: str):
        """
        Write all properties into file

        :param file_path: Path to .json file
        :return: None

        :Example:

        .. code-block:: python

            from utils_sdk import Properties

            # Read properties into object
            props = Properties()
            props.deserialize("C:\\test_data.json")

            # Manage properties
            props.ad_user3_name = "Abra"
            print(props.ad_user3_name)
            Abra

            # Serialize properties
            props.serialize("C:\\test_data.json")
        """
        with open(file_path, 'w') as data_file:
            json.dump(self._properties, data_file, indent=4)
