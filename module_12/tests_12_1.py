import unittest
from runner import Runner


class RunnerTest(unittest.TestCase):

    def test_walf(self):
        walk = Runner('Test walk')

        for _ in range(10):
            walk.walk()

        self.assertEqual(walk.distance, 50)

    def test_run(self):
        run = Runner('Test run')

        for _ in range(10):
            run.run()

        self.assertEqual(run.distance, 100)

    def test_challenge(self):
        ch1 = Runner('Test ch1')
        ch2 = Runner('Test ch2')

        for _ in range(10):
            ch1.run()
            ch1.walk()
            ch2.run()
            ch2.walk()

        self.assertNotEqual(ch1.run(), ch1.walk() != ch2.run(), ch2.walk())


if __name__ == "__main__":
    unittest.main()