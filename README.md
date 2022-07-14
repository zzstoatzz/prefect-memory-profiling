# prefect-profiling

## Welcome!

A collection of Prefect Tasks for different varieties of profiling

## Getting Started

### Python setup

Requires an installation of Python 3.7+.

We recommend using a Python virtual environment manager such as pipenv, conda or virtualenv.

These tasks are designed to work with Prefect 2.0. For more information about how to use Prefect, please refer to the [Prefect documentation](https://orion-docs.prefect.io/).

### Installation

Install `prefect-profiling` with `pip`:

```bash
pip install prefect-profiling
```

### Write and run a flow

```python
from prefect import flow
from prefect_profiling.tasks import (
    goodbye_prefect_profiling,
    hello_prefect_profiling,
)


@flow
def example_flow():
    hello_prefect_profiling
    goodbye_prefect_profiling

example_flow()
```

## Resources

If you encounter any bugs while using `prefect-profiling`, feel free to open an issue in the [prefect-profiling](https://github.com/zzstoatzz/prefect-profiling) repository.

If you have any questions or issues while using `prefect-profiling`, you can find help in either the [Prefect Discourse forum](https://discourse.prefect.io/) or the [Prefect Slack community](https://prefect.io/slack).

## Development

If you'd like to install a version of `prefect-profiling` for development, clone the repository and perform an editable install with `pip`:

```bash
git clone https://github.com/zzstoatzz/prefect-profiling.git

cd prefect-profiling/

pip install -e ".[dev]"

# Install linting pre-commit hooks
pre-commit install
```
