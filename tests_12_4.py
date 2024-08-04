import logging as log
import unittest as ut

import tests_12.rt_with_exceptions as r


class RunnerTest(ut.TestCase):
    is_frozen = False

    def setUpClass(cls=r.Runner):
        log.basicConfig(level=log.INFO,
                        filemode="r",
                        filename='runner_tests.log',
                        encoding='utf-8',
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    @ut.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        """
        Test for function walk class Runner
        :return:
        """
        try:
            current_runner = r.Runner('Great Cucumber', -7)
            for i in range(0, 10):
                current_runner.walk()
            self.assertEqual(current_runner.distance, 50)
            log.info('"test_walk" выполнен успешно')
        except ValueError as v:
            log.warning('Неверная скорость для Runner')

    @ut.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        """
        Test for function run class Runner
        :return:
        """
        try:
            current_runner = r.Runner(23, 2)
            for i in range(0, 10):
                current_runner.run()
            self.assertEqual(current_runner.distance, 100)
            log.info('"test_run" выполнен успешно')
        except TypeError as t:
            log.warning('Неверный тип данных для объекта Runner')

    @ut.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        """
        Test for function run and walk class Runner
        :return:
        """
        great_runner = r.Runner('Great Cucumber')
        simple_runner = r.Runner('Simple Cucumber')

        for i in range(0, 10):
            great_runner.run()
            simple_runner.walk()

        self.assertNotEqual(great_runner.distance, simple_runner.distance)
