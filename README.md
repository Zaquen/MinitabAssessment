# Minitab Assessment Web App README

## Description

This project is a simple REST API built with FastAPI that provides basic statistical calculations.

The service exposes endpoints to compute:
* Mean of a list of numbers
* Population standard deviation of a list of numbers

The application includes input validation, structured logging, containerization via Docker, and a pytest test suite.

## Setup

### ENV

The application is configured to use an `.env` file for configurations.
An `.env.example` file is provided, and can be copied to create a  `.env` file:
```bash
cp .env.example .env
```

The app currently allows for Port configuration in the `.env` file.
Without the `.env` file overriding anything, the port is set to default to 8000, both locally and through docker.

### Local

1. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\Activate.ps1
```

2. Install Dependencies
```bash
pip install -r requirements.txt
```

3. Run App
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

* To exit the virtual environment, run:
```bash
deactivate
```

### Docker 
* Requires that Docker is installed and running locally

The app can be built and run using the provided script:
```bash
./run.sh
```

* If needed, ensure that the script is executable:
```bash
chmod +x run.sh
```

Configuration files:
* `Dockerfile` - container image definition
* `docker-compose.yaml` - service orchestration

## Using the app
The app will by default be available at:
http://localhost:8000

Interactive API documentation is available at:
http://localhost:8000/docs

If the port is changed in the `.env` file, the app will be available at that port instead.

The API accepts and returns JSON for clarity and extensibility.

Statistical requests must include a `numbers` field containing a list of numeric values.

A `/health` endpoint is provided to ensure availability and responsiveness.

### Example Requests & Responses

#### PowerShell (Windows) users:
Powershell aliases `curl` to `Invoke-WebRequest`, which uses a different syntax.
You can either:
1. Use native `Invoke-WebRequest` (Recommended):
```PowerShell
$body = @{
    numbers = @(1,2,3,4,5)
} | ConvertTo-Json

Invoke-RestMethod `
  -Uri "http://localhost:8000/stddev" `
  -Method POST `
  -Body $body `
  -ContentType "application/json"
```
2. Use `curl.exe` with new formatting:
```PowerShell
curl.exe --% -X POST http://localhost:8000/mean -H "Content-Type: application/json" --data-raw "{\"numbers\":[1,2,3,4,5]}"
```

#### Mean

Request:
```bash
curl http://localhost:8000/mean -X POST -d '{"numbers":[1,2,3,4,5]}' -H "Content-Type: application/json"
```
Response:
```json
{"mean": 3}
```

#### Stddev

Request:
```bash
curl http://localhost:8000/stddev -X POST -d '{"numbers":[1,2,3,4,5]}' -H "Content-Type: application/json"
```
Response:
```json
{"stddev": 1.414}
```

## Testing

The pytest suite can be run with the following:
```bash
pytest
```
