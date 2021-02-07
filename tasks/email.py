from ..services import celery



# @celery.task()
def add_together(a, b):
    print(1111111111111111111111)
    print(celery)
    print(type(celery))
    print(2222222222222222222222222)
    return a + b
