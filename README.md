# Project Setup Guide

This guide will help you to configure and set up your local environment.

## Prerequisites
Ensure you have the following installed on your system:
- [Docker](https://www.docker.com/)
- A database client (e.g., [PgAdmin](https://www.pgadmin.org/), [DBeaver](https://dbeaver.io/))
- A code editor (e.g., [VS Code](https://code.visualstudio.com/))
- python version `">=3.9,<3.13"`

## 1. Environment Configuration

**Create a .env file** <br>
1.	Create a .env file in the project root directory:
```shell
  touch .env
```
2. Add the following content to the .env file:
 ```dotenv
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=metabase
POSTGRES_PORT=5434

DAGSTER_PORT=3001
METABASE_PORT=3000
   ```
3. Modify these values based on your local setup if needed.

## 2. Database Setup
**Create a New Database for DBT**
1. Start the postgres service:

```shell
    docker compose up -d postgres
  ```
2. Connect to the PostgreSQL database using one of the methods below:
   1. **Using a Database Client**:
   2. **Using Docker CLI**
   ```shell
    docker exec -it zen-postgres bash
    ```
   ```shell
    psql -U postgres
    ```
   ```shell
    CREATE DATABASE <db-name>;
    ```
   
## 3. DBT Configuration
1.	Navigate to the DBT profiles directory:
```shell
  cd local/dbt/profile
```
2.	Create a new file named profiles.yml:
```shell
  touch profiles.yml
```
3.  Add the following content to the profiles.yml file:
```yaml
tick:
  outputs:
    dev:
      type: postgres
      threads: 1
      host: zen-postgres  # The container name of the PostgreSQL service
      port: 5432
      user: postgres
      pass: postgres
      dbname: <db>       # The name of the database you just created
      schema: public
  target: dev
```

4. Save the file


## 4. Start All Services

**Run the following command to start all services:**
```shell
  docker compose up -d
```

## 5. Verify the Setup
1. Access services in a browser:
    - **Dagster**: [http://localhost:3001](http://localhost:3001)
    - **Metabase**: [http://localhost:3000](http://localhost:3000)
3. Test the DBT connection directly in the container:
    1. Access the container running DBT:
   ```shell
   docker exec -it zen-dagster bash
   ```
    2. Navigate to the DBT project directory in the container:
   ```shell
   cd /app/dbt/tick
   ```
    3. Run the following command to test the connection:
   ```shell
   dbt debug
   ```