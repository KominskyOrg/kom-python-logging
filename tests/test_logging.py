import os
import pytest
from src.logging import setup_logger

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
