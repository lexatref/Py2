import unittest
from py2 import CountVectorizer


class MyTestCase(unittest.TestCase):
    def test_fit_transform(self):
        corpus = [
            'Crock Pot Pasta Never boil pasta again',
            'Pasta Pomodoro Fresh ingredients Parmesan to taste'
        ]

        vectorizer = CountVectorizer()
        count_matrix = vectorizer.fit_transform(corpus)
        self.assertEqual(count_matrix, [[1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]])
    def get_feature_names(self):
        corpus = [
            'Crock Pot Pasta Never boil pasta again',
            'Pasta Pomodoro Fresh ingredients Parmesan to taste'
        ]

        vectorizer = CountVectorizer()
        count_matrix = vectorizer.fit_transform(corpus)
        res = vectorizer.get_feature_names()
        self.assertEqual(res, ['crock', 'pot', 'pasta', 'never', 'boil', 'again', 'pomodoro', 'fresh', 'ingredients',
                               'parmesan', 'to', 'taste'])


if __name__ == '__main__':
    unittest.main()
