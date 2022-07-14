from prefect import flow
from prefect_memory_profiling.tasks import profiled_task

@profiled_task(name='My Profiled Task', stream=open('logfile.txt', 'a+'))
def resource_intensive_task(n: int = 100):
    a = [n**n for n in range(2*n)]
    b = [n**n for n in range(4*n)]
    c = [n**n for n in range(n**2)]
                
    return sum(a + b + c)

@flow
def testing():
    resource_intensive_task()