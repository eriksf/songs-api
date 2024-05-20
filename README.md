# Songs API with FastAPI + SQLModel + Alembic

An API for Songs built with [FastAPI🚀](https://fastapi.tiangolo.com/) and [SQLModel](https://sqlmodel.tiangolo.com/).

## Prerequisites

- Docker/Docker Compose

## For development

1. Install [Poetry](https://python-poetry.org/):

    ```console
    > curl -sSL https://install.python-poetry.org | python3 -
    ```

    This will install poetry in its own virtual environment using whichever version of python3 you specify.

2. Clone this repo:

    ```console
    > git clone https://github.com/eriksf/songs-api.git
    > cd songs-api
    > poetry install
    ```

3. Set up database variables:

    ```console
    > cp project/.env.dev.sample project/.env
    ```

    then edit the variables.

4. Create and spin up the Docker containers:

    ```console
    > docker compose up -d --build
    ```

5. To view logs:

    ```console
    > docker compose logs web
    ```

    or

    ```console
    > docker compose logs db
    ```

6. Run the database migrations:

    ```console
    > docker compose exec web alembic upgrade head
    ```

7. Navigate to the docs at [http://localhost:8004](http://localhost:8004).

## For production

1. Clone this repo:

    ```console
    > git clone https://github.com/eriksf/songs-api.git
    > cd songs-api
    ```

2. Set up database variables:

    ```console
    > cp project/.env.prod.sample project/.env
    ```

    then edit the variables.

3. Create and spin up the web container:

    ```console
    > docker compose -f docker-compose-prod.yml up -d --build
    ```

4. To view logs:

    ```console
    > docker compose logs web
    ```
