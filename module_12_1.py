import Runner as runner # Вызываем модуль
from unittest import TestCase # Импортируем TestCase из unittest

class RunnerTest(TestCase): # Создаем тестовый класс RunnerTest, наследуем его от TestCase

    def test_walk(self): # Создаем тестовый метод test_walk
        runner_1 = runner.Runner('1') # Создаем экземпляр runner_1 с именем '1'
        for i in range(10):  # Проходимся циклом 10 раз
            runner_1.walk()
        self.assertEqual(runner_1.distance, 50) # Проверяем

    def test_run(self): #
        runner_2 = runner.Runner('2')
        for i in range(10): # Выполняем 10 проходов
            runner_2.run()
        self.assertEqual(runner_2.distance, 100) # Проверяем

    def test_challenge(self):  # Создаем тестовый метод test_challenge
        runner_1 = runner.Runner('1') # Создаем экземпляр runner_1 с именем '1'
        runner_2 = runner.Runner('2') # Создаем экземпляр runner_2 с именем '2'
        for i in range(10): # Проходимся циклом 10 раз
            runner_1.run()
        for i in range(10):  # Проходимся циклом 10 раз
            runner_2.walk()
        self.assertNotEqual(runner_1.distance, runner_2.distance)


RunnerTest()
# Тестируем
