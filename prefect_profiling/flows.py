"""This is an example flows module"""
from prefect import flow

from prefect_profiling.tasks import (
    goodbye_prefect_profiling,
    hello_prefect_profiling,
)


@flow
def hello_and_goodbye():
    """
    Sample flow that says hello and goodbye!
    """
    print(hello_prefect_profiling)
    print(goodbye_prefect_profiling)
