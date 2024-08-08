import logging


def setup_logger(name: str, log_file: str, level: int = logging.INFO):
    formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")

    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger


def set_logging_level(level_name: str) -> int:
    level_name = level_name.upper()
    level = {
        "DEBUG": logging.DEBUG,
        "INFO": logging.INFO,
        "WARNING": logging.WARNING,
        "ERROR": logging.ERROR,
        "CRITICAL": logging.CRITICAL,
    }.get(level_name, logging.INFO)

    return level
