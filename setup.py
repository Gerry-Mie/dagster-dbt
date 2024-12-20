from setuptools import find_packages, setup

setup(
    name="bigdata",
    version="0.0.1",
    packages=find_packages(),
    package_data={
        "bigdata": [
            "dbt-project/**/*",
        ],
    },
    install_requires=[
        "dagster",
        "dagster-cloud",
        "dagster-dbt",
        "dbt-postgres<1.9",
        "dbt-postgres<1.9",
    ],
    extras_require={
        "dev": [
            "dagster-webserver",
        ]
    },
)