import unittest
from course5 import tests_12_3

run_tourST = unittest.TestSuite()
run_tourST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
run_tourST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(run_tourST)