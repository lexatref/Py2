
class CountVectorizer:
    def __init__(self):
        self.features = []

    def find_feature_names(self, text: list[str]):
        self.features.clear()
        for text_string in text:
            words = text_string.lower().split(' ')
            for word in words:
                if not (word in self.features):
                    self.features.append(word)

    def fit_transform(self, text: list[str]) -> list[list[int]]:
        self.find_feature_names(text)
        result = []
        for text_string in text:
            result_string = [0] * len(self.features)
            words = text_string.lower().split(' ')
            for word in words:
                for i, feature in enumerate(self.features):
                    if word == feature:
                        result_string[i] += 1
                        break
            result.append(result_string)
        return result

    def get_feature_names(self) -> list[str]:
        return self.features


def main():
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]

    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)

    print(vectorizer.get_feature_names())

    print(count_matrix)


if __name__ == '__main__':
    main()
