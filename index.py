import logging

log_path = "logs/index.log"
logging.basicConfig(filename=log_path, level=logging.INFO, format="%(levelname)s:%(asctime)s %(message)s")

class Logging_Info:
    def __init__(self, inner_m):
        self.__inner_m = inner_m
        
    def __call__(self, *args, **kwargs):
        logging.info(f"The invoked method is {self.__inner_m.__name__.upper()}")        
        return self.__inner_m(*args, **kwargs)

@Logging_Info
def add(*args):
    return sum(args)

add(1, 2, 3)

