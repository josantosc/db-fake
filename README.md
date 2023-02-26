# DIGI-FAKE-API

[![PyPI](https://img.shields.io/pypi/v/json-server.py.svg)](https://pypi.org/project/json-server.py/)

Fake REST API DIGI-SYSTEM.

Requires [Python 3.6+](https://pypi.org/project/json-server.py/), [FastApi](https://fastapi.tiangolo.com/) and [Uvicorn](https://www.uvicorn.org/)

## Cloning this whole repository

To clone this repository, run:
``` bash
$ git clone 
```
## Create virtual environment

```bash
$ python -m venv venv
$ source venv/bin/activate  # Windows: \venv\scripts\activate
```

## Install dependencies
```bash
$ pip install -r requirements.txt
```


## Run
```sh
$ python3 -m uvicorn app.main:app --port 8001 --reload  
```

Testing request:

```sh
$ curl http://localhost:8001
```