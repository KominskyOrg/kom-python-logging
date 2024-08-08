# Changelog

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
