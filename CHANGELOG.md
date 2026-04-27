# Changelog

## [1.0.0] - Initial Release

### Added
* FastAPI application with the following endpoints:
  * `POST /mean` to compute the mean of a list of numbers
  * `POST /stddev` to compute the population standard deviation
  * `GET /health` for service health checks
* Pydantic*based request validation with custom validation for non*empty lists
* Structured logging
* Rounding of responses to 3 decimal places

### Docker & DevOps
* Dockerfile for containerizing the application
* Docker Compose configuration for local orchestration
* Environment variable support via `.env`
* Runtime configuration using `PORT` environment variable
* `run.sh` script for building and running the container

### Testing
* Pytest test suite covering:
  * Accurate endpoints
  * Error handling

### Project Setup
* Virtual environment (`venv`) support for local development
* Clean `.ignore` files for Python and Docker artifacts
* Dependency management via `requirements.txt`

### Documentation
* Comprehensive `README.md` including:
  * Setup instructions
  * API usage examples
  * Environment configuration
  * Design decisions and assumptions
