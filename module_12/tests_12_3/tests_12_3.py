import unittest
from course2.runner import Runner
from course3.runner_and_tournament import Runner, Tournament


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, '')
    def test_walf(self):
        walk = Runner('Test walk')

        for _ in range(10):
            walk.walk()

        self.assertEqual(walk.distance, 50)

    @unittest.skipIf(is_frozen, '')
    def test_run(self):
        run = Runner('Test run')

        for _ in range(10):
            run.run()

        self.assertEqual(run.distance, 100)

    @unittest.skipIf(is_frozen, '')
    def test_challenge(self):
        ch1 = Runner('Test ch1')
        ch2 = Runner('Test ch2')

        for _ in range(10):
            ch1.run()
            ch1.walk()
            ch2.run()
            ch2.walk()

        self.assertNotEqual(ch1.run(), ch1.walk() != ch2.run(), ch2.walk())



class TournamentTest(unittest.TestCase):

    all_results = {}
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_1 = Runner('Усэйн', 10)
        self.runner_2 = Runner('Андрей', 9)
        self.runner_3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for key in sorted(cls.all_results.keys()):
            result = {place: str(runner) for place, runner in cls.all_results[key].items()}
            print(result)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_start_1(self):
        start_1 = Tournament(90, self.runner_1, self.runner_3)
        result = start_1.start()

        TournamentTest.all_results[len(TournamentTest.all_results) + 1] = result
        self.assertTrue(result[max(result.keys())] == self.runner_3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_start_2(self):
        start_2 = Tournament(90, self.runner_2, self.runner_3)
        result = start_2.start()

        TournamentTest.all_results[len(TournamentTest.all_results) + 1] = result
        self.assertTrue(result[max(result.keys())] == self.runner_3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_start_3(self):
        start_3 = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        result = start_3.start()

        TournamentTest.all_results[len(TournamentTest.all_results) + 1] = result
        self.assertTrue(result[max(result.keys())] == self.runner_3)

if __name__ == "__main__":
    unittest.main()