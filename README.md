# prefect-memory-profiling

## Welcome!

A collection of Prefect Tasks for memory profiling in Prefect 1.0.

## Getting Started

### Python setup

Requires an installation of Python 3.7+.

We recommend using a Python virtual environment manager such as `pipenv`, `conda` or `virtualenv`.

For more information about how to use Prefect, please refer to the [Prefect documentation](https://docs.prefect.io/).

### Installation

Install `prefect-memory-profiling` with `pip`:

```bash
pip install prefect-memory-profiling
```

### Write and run a flow

```python
from prefect import Flow
from prefect_memory_profiling.tasks import profiled_task

@profiled_task(name='My Profiled Task', stream=open('logfile.txt', 'a+'))
def resource_intensive_task(n: int = 100):
    a = [n**n for n in range(2*n)]
    b = [n**n for n in range(4*n)]
    c = [n**n for n in range(n**2)]
                
    return sum(a + b + c)

with Flow('Memory Profiled Flow') as flow:
    resource_intensive_task()
    
if __name__ == "__main__":
    flow.run(run_on_schedule=False)
```

## Resources

If you encounter any bugs while using `prefect-memory-profiling`, feel free to open an issue in the [prefect-memory-profiling](https://github.com/zzstoatzz/prefect-memory-profiling) repository.

If you have any questions or issues while using `prefect-memory-profiling`, you can find help in either the [Prefect Discourse forum](https://discourse.prefect.io/) or the [Prefect Slack community](https://prefect.io/slack).

## Development

If you'd like to install a version of `prefect-memory-profiling` for development, clone the repository and perform an editable install with `pip`:

```bash
git clone https://github.com/zzstoatzz/prefect-memory-profiling.git

cd prefect-memory-profiling/

pip install -e ".[dev]"

# Install linting pre-commit hooks
pre-commit install
```
