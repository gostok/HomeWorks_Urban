from runner_and_tournament import Runner, Tournament
import unittest

class TournamentTest(unittest.TestCase):

    all_results = {}

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

    def test_start_1(self):
        start_1 = Tournament(90, self.runner_1, self.runner_3)
        result = start_1.start()

        TournamentTest.all_results[len(TournamentTest.all_results) + 1] = result
        self.assertTrue(result[max(result.keys())] == self.runner_3)


    def test_start_2(self):
        start_2 = Tournament(90, self.runner_2, self.runner_3)
        result = start_2.start()

        TournamentTest.all_results[len(TournamentTest.all_results) + 1] = result
        self.assertTrue(result[max(result.keys())] == self.runner_3)

    def test_start_3(self):
        start_3 = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        result = start_3.start()

        TournamentTest.all_results[len(TournamentTest.all_results) + 1] = result
        self.assertTrue(result[max(result.keys())] == self.runner_3)


if __name__ == "__main__":
    unittest.main()
