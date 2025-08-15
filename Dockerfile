FROM python:3.12-slim AS requirements-stage

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /tmp

RUN pip install poetry

COPY ./pyproject.toml ./poetry.lock* /tmp/

RUN poetry self add poetry-plugin-export
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /search-app

COPY --from=requirements-stage /tmp/requirements.txt /requirements.txt

RUN pip install --no-cache-dir --upgrade -r /requirements.txt

COPY . .

#CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

