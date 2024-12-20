from dagster import AssetExecutionContext
from dagster_dbt import DbtCliResource, dbt_assets

from .project import tick_project


@dbt_assets(manifest=tick_project.manifest_path)
def tick_dbt_assets(context: AssetExecutionContext, dbt: DbtCliResource):
    yield from dbt.cli(["build"], context=context).stream()
    