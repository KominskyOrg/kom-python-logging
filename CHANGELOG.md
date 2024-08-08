# Changelog

## [0.4] - 2024-08-07
### Added
- Configuration for Black code formatter to align with Flake8 linting styles.
- Black's `pyproject.toml` configuration file with a line length of 79 characters to match Flake8.
- Flake8's `.flake8` configuration file updated to ignore `E203` and `W503` for compatibility with Black.
- Option to enable console logging in addition to file logging in the `setup_logger` function.
- Error handling to ensure at least one logging option (file or console) is enabled.
- Sad path tests to handle invalid log levels, invalid log file paths, and missing parameters.

### Changed
- Default line length changed from 88 to 79 characters to maintain consistency with Flake8.
- `setup_logger` function updated to raise an error if both `log_file` and `console` are not provided.
- Updated test cases to include validations for new error handling.

### Fixed
- Handled `None` values in `set_logging_level` function to avoid `AttributeError`.
- Corrected the expected exception in the `test_invalid_log_file_permission` test case from `PermissionError` to `FileNotFoundError`.

## [0.3] - 2024-08-07
### Added
- `set_logging_level` function to map string level names to logging constants.
- Ability to set logging levels dynamically based on string input (e.g., "DEBUG", "INFO").
- Parametrized tests to verify logging levels and ensure correct behavior for different levels.

### Changed
- Updated `setup_logger` function to accept logging level as a parameter.

## [0.2] - 2024-08-07
### Added
- Initial setup of the logging package with `setup_logger` function.
- Basic logging configuration with file handler and formatter.
- Unit tests to verify basic logging functionality.
