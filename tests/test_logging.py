import os
import pytest
import logging
from src.logging import setup_logger, set_logging_level


@pytest.fixture
def logger():
    log_file = "test.log"
    logger = setup_logger("test_logger", log_file)
    yield logger
    if os.path.exists(log_file):
        os.remove(log_file)


def test_logging(logger):
    log_file = "test.log"
    logger.info("Test log message")
    assert os.path.exists(log_file)
    with open(log_file, "r") as f:
        content = f.read()
        assert "Test log message" in content


@pytest.mark.parametrize(
    "level_name, log_level",
    [
        ("DEBUG", logging.DEBUG),
        ("INFO", logging.INFO),
        ("WARNING", logging.WARNING),
        ("ERROR", logging.ERROR),
        ("CRITICAL", logging.CRITICAL),
        ("INVALID", logging.INFO),  # Default case for invalid level
    ],
)
def test_set_logging_level(level_name, log_level):
    assert set_logging_level(level_name) == log_level


@pytest.mark.parametrize(
    "level_name, log_message, is_in_log",
    [
        ("DEBUG", "This is a debug message", True),
        ("INFO", "This is an info message", True),
        ("WARNING", "This is a warning message", True),
        ("ERROR", "This is an error message", True),
        ("CRITICAL", "This is a critical message", True),
        ("INFO", "This debug message should not appear", False),
    ],
)
def test_logger_levels(level_name, log_message, is_in_log):
    log_file = "test.log"
    log_level = set_logging_level(level_name)
    logger = setup_logger("test_logger_level", log_file, log_level)

    if "debug" in log_message.lower():
        logger.debug(log_message)
    elif "info" in log_message.lower():
        logger.info(log_message)
    elif "warning" in log_message.lower():
        logger.warning(log_message)
    elif "error" in log_message.lower():
        logger.error(log_message)
    elif "critical" in log_message.lower():
        logger.critical(log_message)

    with open(log_file, "r") as f:
        content = f.read()
        assert (log_message in content) == is_in_log

    if os.path.exists(log_file):
        os.remove(log_file)
