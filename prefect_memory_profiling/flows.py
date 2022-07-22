from decimal import Decimal
from prefect import flow, get_run_logger
from tasks import profiled_task

@profiled_task(name='My Profiled Task')
def resource_intensive_task(n: int = 100):
    a = [n**n for n in range(2*n)]
    b = [n**n for n in range(4*n)]
    c = [n**n for n in range(n**2)]
                
    return sum(a + b + c)

@flow
def my_profiled_flow():
    logger = get_run_logger()
    
    my_really_big_sum = resource_intensive_task()
    
    logger.info(f'my_really_big_sum = {Decimal(my_really_big_sum):.3E}')
    
if __name__ == "__main__":
    my_profiled_flow()