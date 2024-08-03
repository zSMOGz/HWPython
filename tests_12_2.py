import pprint
import unittest as ut

import tests_12.runner_and_tournament as runner


class TournamentTest(ut.TestCase):
    is_frozen = True

    def setUpClass(cls=runner.Tournament):
        cls.all_results = ()

    def setUp(self):
        runners = []
        husein = runner.Runner('Усэйн', 10)
        runners.append(husein)
        andrei = runner.Runner('Андрей', 9)
        runners.append(andrei)
        nick = runner.Runner('Ник', 3)
        runners.append(nick)
        self.runners = runners

    def tearDownClass(cls=runner.Tournament):
        pprint.pprint(cls.all_results)

    @ut.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_tournament1(self):
        tournament = runner.Tournament(90,
                                       self.runners[0], self.runners[2])
        results = tournament.start()
        self.assertTrue(list(results)[-1], self.runners[-1].name)

    @ut.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_tournament2(self):
        tournament = runner.Tournament(90,
                                       self.runners[1], self.runners[2])
        results = tournament.start()
        self.assertTrue(list(results)[-1], self.runners[-1].name)

    @ut.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_tournament3(self):
        tournament = runner.Tournament(90,
                                       self.runners[0], self.runners[1], self.runners[2])
        results = tournament.start()
        self.assertTrue(list(results)[-1], self.runners[-1].name)

    @ut.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_tournament4(self):
        tournament = runner.Tournament(90,
                                       self.runners[2], self.runners[1], self.runners[0])
        results = tournament.start()
        self.assertTrue(list(results)[-1], self.runners[-1].name)

    @ut.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_tournament5(self):
        tournament = runner.Tournament(90,
                                       self.runners[2], self.runners[1], self.runners[0])
        results = tournament.start()
        self.assertTrue(list(results.values())[0].speed, max(results.values()))

    @ut.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_tournament6(self):
        tournament = runner.Tournament(90,
                                       self.runners[2], self.runners[1], self.runners[0])
        results = tournament.start()
        self.assertTrue(list(results.values())[-1].speed, min(results.values()))
