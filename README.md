# Songs API with FastAPI + SQLModel + Alembic

## Prerequisites

- Docker/Docker Compose

## Usage

1. Clone this repo:

    ```bash
    $ git clone https://github.com/eriksf/songs-api.git
    $ cd songs-api

2. Set up database variables:

    ```bash
    $ cp project/.env.sample project/.env
    ```
    then edit the variables.

3. Create and spin up the Docker containers:

    ```bash
    $ docker compose --env-file=project/.env up -d --build
    ```

4. Navigate to the docs at http://localhost:8004/docs.
