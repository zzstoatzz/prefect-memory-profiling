"""This is an example tasks module"""
from io import TextIOWrapper
from memory_profiler import profile
from prefect import flow, task
from prefect.tasks import Task
from typing import Any, Callable


class ProfiledTask(Task):
    def __init__(
            self,
            fn: Callable = None,
            stream: TextIOWrapper = None,
            name: str = None,
            **kwargs: Any
    ):        
        
        # `fn` is the callable to be profiled, writing output to `stream`        
        profiled_fn = profile(fn, stream=stream) if stream else profile(fn)

        # we ultimately want this to behave like a `Task`
        super().__init__(profiled_fn, name, **kwargs)


def profiled_task(
    fn: Callable = None, **task_init_kwargs: Any
):
    if fn is None:
        return lambda fn: ProfiledTask(
            fn=fn,
            **task_init_kwargs,
        )
    return ProfiledTask(fn=fn, **task_init_kwargs)

@profiled_task(name='My Profiled Task', stream=open('logfile.txt', 'a+'))
def resource_intensive_task(n: int = 100):
    a = [n**n for n in range(2*n)]
    b = [n**n for n in range(4*n)]
    c = [n**n for n in range(n**2)]
                
    return sum(a + b + c)

@flow
def testing():
    resource_intensive_task()
    
if __name__ == "__main__":
    testing()