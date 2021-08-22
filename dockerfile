FROM python:3.8-slim

ENV PIP_DISABLE_PIP_VERSION_CHECK=on \
    POETRY_VIRTUALENVS_CREATE=false \
    PIP_NO_CACHE_DIR=off \
    POETRY_VERSION=1.1.8

WORKDIR /src

COPY ./src /src/src
COPY pyproject.toml poetry.lock /src/

RUN pip install "poetry==$POETRY_VERSION"
RUN poetry install --no-dev

CMD ["python", "src/main.py"]