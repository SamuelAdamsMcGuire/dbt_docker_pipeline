## Example dbt pipeline in Docker

#### how to use

- install docker and docker-compose
- clone repo
- get free account at: https://exchangeratesapi.io/
- save api key in `.env` file in the root repo directory as `API_KEY`
- execute `docker-compose up` in the root directory
- the dbt models will be created
- leaving the containers running you can now access metabase at `http://localhost:3000`
- sign up and regisiter you running postgres db
    - host = mypg
    - port = 5432
    - db = exchange

#### To Dos

- fix `.env` so it will also hold the postgres and other secret data (had problems with DBT resolving the postgres credentials)
- add tests in DBT
- add macros in DBT
- add documentation in DBT

