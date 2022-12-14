import unittest
from python_ds_solution_lesson_2 import CountVectorizer
from python_ds_solution_lesson_2_dict import CountVectorizerDict


class MyTestCase(unittest.TestCase):
    def test_fit_transform(self):
        corpus = [
            'Crock Pot Pasta Never boil pasta again',
            'Pasta Pomodoro Fresh ingredients Parmesan to taste'
        ]

        vectorizer = CountVectorizer()
        count_matrix = vectorizer.fit_transform(corpus)
        self.assertEqual(count_matrix, [[1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                                        [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]])

    def test_get_feature_names(self):
        corpus = [
            'Crock Pot Pasta Never boil pasta again',
            'Pasta Pomodoro Fresh ingredients Parmesan to taste'
        ]

        vectorizer = CountVectorizer()
        vectorizer.fit_transform(corpus)
        res = vectorizer.get_feature_names()
        self.assertEqual(res, ['crock', 'pot', 'pasta', 'never', 'boil',
                               'again', 'pomodoro', 'fresh', 'ingredients',
                               'parmesan', 'to', 'taste'])

    def test_fit_transform_dict(self):
        corpus = [
            'Crock Pot Pasta Never boil pasta again',
            'Pasta Pomodoro Fresh ingredients Parmesan to taste'
        ]

        vectorizer = CountVectorizerDict()
        count_matrix = vectorizer.fit_transform(corpus)
        self.assertEqual(count_matrix, [[1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                                        [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]])

    def test_get_feature_names_dict(self):
        corpus = [
            'Crock Pot Pasta Never boil pasta again',
            'Pasta Pomodoro Fresh ingredients Parmesan to taste'
        ]

        vectorizer = CountVectorizerDict()
        vectorizer.fit_transform(corpus)
        res = vectorizer.get_feature_names()
        self.assertEqual(res, ['crock', 'pot', 'pasta', 'never', 'boil',
                               'again', 'pomodoro', 'fresh', 'ingredients',
                               'parmesan', 'to', 'taste'])


if __name__ == '__main__':
    unittest.main()
