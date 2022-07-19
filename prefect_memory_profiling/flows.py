from prefect import Flow
from tasks import profiled_task

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