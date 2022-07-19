"""This is an example tasks module"""
from io import TextIOWrapper
from memory_profiler import profile
from prefect.tasks.core.function import FunctionTask
from typing import Any, Callable

class ProfiledFunctionTask(FunctionTask):
    def __init__(
            self,
            fn: Callable = None,
            name: str = None,
            stream: TextIOWrapper = None,
            **kwargs: Any
    ):
        # `fn` is the callable to be profiled, writing output to `stream`
        profiled_fn = profile(fn, stream=stream) if stream else profile(fn)

        # we ultimately want this to behave like a `Task`
        super().__init__(profiled_fn, name, **kwargs)


def profiled_task(
    fn: Callable = None, stream: TextIOWrapper = None, **task_init_kwargs: Any
):
    if fn is None:
        return lambda fn: ProfiledFunctionTask(
            fn=fn,
            stream=stream,
            **task_init_kwargs,
        )
    return ProfiledFunctionTask(fn=fn, stream=stream, **task_init_kwargs)