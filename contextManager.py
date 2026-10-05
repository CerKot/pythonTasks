import time

class ourManager:

    def __enter__(self):
        print('начали использовать')
        self.start = time.time()

        return self

    def __exit__(self,exc_type, exc_val, exc_tb):
        if exc_type:
           if exc_type == ValueError:
               print('яки-та ошибкачка')
               return True


        end = time.time()
        print(f"{end-self.start} с работал наш менеджер")
        print("Закончили")
        return False

with ourManager() as tM:
    float('a')
    time.sleep(3)
