FROM python:3.11.8-bookworm as poetry
ENV POETRY_VERSION = "1.8.3"

RUN pip install "poetry==${POETRY_VERSION}"

# Set working directory
WORKDIR /usr/src/app

COPY pyproject.toml poetry.lock ./

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes --with=dev

FROM python:3.11.8-bookworm
LABEL maintainer="Erik Ferlanti <eferlanti@tacc.utexas.edu>"

# Update OS
RUN apt-get update && apt-get install -y \
    netcat-traditional \
    gcc \
    postgresql \
    vim-tiny \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Set environment variables for Python/Pip
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONFAULTHANDLER=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

WORKDIR /usr/src/app

COPY --from=poetry /usr/src/app/requirements.txt .

# Install python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Add app
COPY . .
