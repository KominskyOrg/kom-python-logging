# src/logging.py
import logging
import json

class JSONFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            "time": self.formatTime(record, self.datefmt),
            "level": record.levelname,
            "message": record.getMessage(),
            "name": record.name,
            "filename": record.pathname,
            "funcName": record.funcName,
            "lineno": record.lineno,
        }
        return json.dumps(log_record)


def set_logging_level(level_name: str) -> int:
    if level_name is None:
        raise ValueError("Logging level name cannot be None")
    level_name = level_name.upper()
    level = {
        "DEBUG": logging.DEBUG,
        "INFO": logging.INFO,
        "WARNING": logging.WARNING,
        "ERROR": logging.ERROR,
        "CRITICAL": logging.CRITICAL,
    }.get(level_name, logging.INFO)

    return level


class KomPythonLogging:
    def __init__(self, name: str, log_file: str = None, level: str = "INFO", console: bool = False, json_format: bool = False):
        self.logger = self.setup_logger(name, log_file, level, console, json_format)

    def setup_logger(self, name: str, log_file: str, level: str, console: bool, json_format: bool):
        if not log_file and not console:
            raise ValueError("At least one of log_file or console must be provided for logging.")

        log_level = set_logging_level(level)
        formatter = JSONFormatter() if json_format else logging.Formatter("%(asctime)s %(levelname)s %(message)s")

        handlers = []
        if log_file:
            file_handler = logging.FileHandler(log_file)
            file_handler.setFormatter(formatter)
            handlers.append(file_handler)

        if console:
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)
            handlers.append(console_handler)

        logger = logging.getLogger(name)
        logger.setLevel(log_level)

        for handler in handlers:
            logger.addHandler(handler)

        return logger

    def set_level(self, level_name: str):
        level = set_logging_level(level_name)
        self.logger.setLevel(level)

    def debug(self, message: str):
        self.logger.debug(message)

    def info(self, message: str):
        self.logger.info(message)

    def warning(self, message: str):
        self.logger.warning(message)

    def error(self, message: str):
        self.logger.error(message)

    def critical(self, message: str):
        self.logger.critical(message)
