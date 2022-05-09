import logging


def initialize(config_file: str):

    logger = logging.getLogger()
    logger.setLevel(0)
    formatter = logging.Formatter(u'# %(levelname)-8s [%(asctime)s] %(filename)-20s [LINE:%(lineno)s]   %(message)s')
    log_file = config_file.replace('config', '').replace('.ini', '.log')

    logging.getLogger("requests").setLevel(logging.WARNING)
    logging.getLogger("urllib3").setLevel(logging.WARNING)

    handler_info = logging.FileHandler("info" + log_file, encoding="utf-8")
    handler_info.setFormatter(formatter)
    handler_info.setLevel(logging.INFO)

    handler_debug = logging.FileHandler("debug" + log_file, encoding="utf-8")
    handler_debug.setFormatter(formatter)
    handler_debug.setLevel(logging.DEBUG)

    logger.handlers = [handler_info, handler_debug]
