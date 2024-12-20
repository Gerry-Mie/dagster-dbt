from pathlib import Path

from dagster_dbt import DbtProject

tick_project = DbtProject(
    project_dir=Path(__file__).joinpath("", "..","..", "dbt", "tick").resolve(),
    # packaged_project_dir=Path(__file__).joinpath("", "..", "dbt-project").resolve(),
)
tick_project.prepare_if_dev()