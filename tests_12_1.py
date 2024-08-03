import unittest as ut

import tests_12.runner as runner


class RunnerTest(ut.TestCase):
    def test_walk(self):
        """
        Test for function walk class Runner
        :return:
        """
        current_runner = runner.Runner('Great Cucumber')
        for i in range(0, 10):
            current_runner.walk()
        self.assertEqual(current_runner.distance, 50)

    def test_run(self):
        """
        Test for function run class Runner
        :return:
        """
        current_runner = runner.Runner('Great Cucumber')
        for i in range(0, 10):
            current_runner.run()
        self.assertEqual(current_runner.distance, 100)

    def test_challenge(self):
        """
        Test for function run and walk class Runner
        :return:
        """
        great_runner = runner.Runner('Great Cucumber')
        simple_runner = runner.Runner('Simple Cucumber')

        for i in range(0, 10):
            great_runner.run()
            simple_runner.walk()

        self.assertNotEqual(great_runner.distance, simple_runner.distance)

