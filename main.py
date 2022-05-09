import logging
import pytest


from execution_utils import argument_parser, logger
from execution_utils.configurators.property_configurator import PropertyConfigurator, PROPERTIES

args = argument_parser.parse_args()
logger.initialize(args.config)


def setup():
    PropertyConfigurator.initialize(args.config)
    PropertyConfigurator.setup()


logging.info("******************START*******************")
setup()
pytest.main(["-m", "bat" if PROPERTIES.bat_only.lower() == "true" else "",
             PROPERTIES.test_path,
             "--log-level", "DEBUG",
             "--log-format", "# %(levelname)-8s [%(asctime)s] %(filename)-20s [LINE:%(lineno)s]   %(message)s",
             "--log-date-format", "%Y-%m-%d %H:%M:%S",
             r"--junitxml={}\{}".format(PROPERTIES.report_path, PROPERTIES.report_file),
             "--disable-pytest-warnings",
             r"--alluredir", PROPERTIES.allure_report_folder,
             ])

logging.info("******************FINISH******************")
