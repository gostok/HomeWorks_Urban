import time
import threading
from queue import Queue


class Table:

    def __init__(self, number):
        self.number = number
        self.is_busy = False


class Cafe:

    def __init__(self, tables):
        self.tables = tables
        self.queue = Queue()
        self.customer_current = 0
        self.customer_limit = 20

    def customer_arrival(self):
        while self.customer_current < self.customer_limit:
            time.sleep(1)
            self.customer_current += 1
            customer_number = self.customer_current
            print(f'Посетитель номер {customer_number} прибыл.')

            free_table = None
            for i in self.tables:
                if not i.is_busy:
                    free_table = i
                    break

            if free_table:
                free_table.is_busy = True
                print(f'Посетитель номер {customer_number} сел за стол {free_table.number}.')
                t1 = Customer(customer_number, self)
                t1.start()
            else:
                print(f"Посетитель номер {customer_number} ожидает свободный стол.")
                self.queue.put(customer_number)


    def serve_customer(self, customer):
        time.sleep(5)
        print(f"Посетитель номер {customer.customer_number} покушал и ушёл.")

        for i in self.tables:
            if i.is_busy:
                i.is_busy = False
                if not self.queue.empty():
                    customer_wait = self.queue.get()
                    print(f"Посетитель номер {customer_wait} сел за стол {i.number}.")
                    t2 = Customer(customer_wait, self)
                    t2.start()
                break

class Customer(threading.Thread):

    def __init__(self, customer_number, cafe):
        super().__init__()
        self.customer_number = customer_number
        self.cafe = cafe

    def run(self):
        self.cafe.serve_customer(self)



# Создаем столики в кафе
table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]

# Инициализируем кафе
cafe = Cafe(tables)

# Запускаем поток для прибытия посетителей
customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()

# Ожидаем завершения работы прибытия посетителей
customer_arrival_thread.join()