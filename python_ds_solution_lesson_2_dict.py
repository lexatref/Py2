
class CountVectorizerDict:
    def __init__(self):
        self.features = {}

    def find_feature_names(self, text: list[str]):
        self.features.clear()
        i = 0
        for text_string in text:
            words = text_string.lower().split(' ')
            for word in words:
                if not (word in self.features):
                    self.features[word] = i
                    i += 1

    def fit_transform(self, text: list[str]) -> list[list[int]]:
        self.find_feature_names(text)
        result = []
        for text_string in text:
            result_string = [0] * len(self.features)
            words = text_string.lower().split(' ')
            for word in words:
                i = self.features[word]
                result_string[i] += 1
            result.append(result_string)
        return result

    def get_feature_names(self) -> list[str]:
        return list(self.features)


def main():
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]

    vectorizer = CountVectorizerDict()
    count_matrix = vectorizer.fit_transform(corpus)

    print(vectorizer.get_feature_names())

    print(count_matrix)


if __name__ == '__main__':
    main()
