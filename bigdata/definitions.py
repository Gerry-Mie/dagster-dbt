from dagster import Definitions
from dagster_dbt import DbtCliResource
from .assets import tick_dbt_assets
from .project import tick_project
from .schedules import schedules

defs = Definitions(
    assets=[tick_dbt_assets],
    schedules=schedules,
    resources={
        "dbt": DbtCliResource(project_dir=tick_project),
    },
)