import logging
import unittest
from course6.rt_with_exceptions import Runner

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='utf-8',
                        format='%(levelname)s | %(message)s')


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            walk = Runner('Test walk', -5)
            walk.walk()
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.exception('Неверная скорость для Runner')
            pass


    def test_run(self):
        try:
            run = Runner(12345, 5)
            run.run()
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.exception('Неверный тип данных для объекта Runner')
            pass


    def test_run_valid(self):
        runner = Runner('Valid Runner', 10)
        runner.run()
        self.assertEqual(runner.distance, 20)
        logging.info('"test_run_valid" выполнен успешно')

    def test_walk_valid(self):
        runner = Runner('Valid Walker', 5)
        runner.walk()
        self.assertEqual(runner.distance, 5)
        logging.info('"test_walk_valid" выполнен успешно')




if __name__ == "__main__":
    unittest.main()