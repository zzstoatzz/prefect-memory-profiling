from prefect import flow

from prefect_profiling.tasks import (
    goodbye_prefect_profiling,
    hello_prefect_profiling,
)


def test_hello_prefect_profiling():
    @flow
    def test_flow():
        return hello_prefect_profiling()

    flow_state = test_flow()
    task_state = flow_state.result()
    assert task_state.result() == "Hello, prefect-profiling!"


def goodbye_hello_prefect_profiling():
    @flow
    def test_flow():
        return goodbye_prefect_profiling()

    flow_state = test_flow()
    task_state = flow_state.result()
    assert task_state.result() == "Goodbye, prefect-profiling!"
