import logging
def my_logger(original_function):
    logging.basicConfig(filename='{}.log'.format(original_function.__name__), level=logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info('ran with args: {} and kwargs: {}'.format(args, kwargs))
        return original_function(*args, **kwargs)

    return wrapper

def my_timer(original_function):
    import time
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = original_function(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(original_function.__name__, t2))
        return result

    return wrapper


import time

@my_timer
def displaytime():
    time.sleep(1)
displaytime()

# @my_logger
# def display_info(name, age):
#     print(name, age)

# display_info("umer", 22)