FROM python:3.12-slim


RUN apt-get update && apt-get install -y git && apt-get clean

ENV DAGSTER_HOME=/opt/dagster/dagster_home

RUN mkdir -p $DAGSTER_HOME

# RUN pip install dagster-webserver dagster-postgres dagster-dbt
RUN python -m pip install dbt-core dbt-postgres dagster-webserver dagster-dbt

# Copy your code and workspace to /opt/dagster/app
#COPY repo.py workspace.yaml /opt/dagster/app/

# Copy dagster instance YAML to $DAGSTER_HOME
#COPY dagster/dagster.yaml $DAGSTER_HOME/

WORKDIR /app

EXPOSE 3000

#ENTRYPOINT ["dagster-webserver", "-h", "0.0.0.0", "-p", "3000"]