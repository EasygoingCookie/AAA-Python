# Реализация класса CountVectorizer
from collections import defaultdict


class CountVectorizer:
    """Создает для набора строк терм-документальную матрицу"""
    def __init__(self):
        self.words = None

    @staticmethod
    def find_array_of_words(text):
        """
        Создание списка слов, имеющихся во всей строках
        -------------------------------------------------
        Параметры:
        ----------
        text - спискок строк
        """
        words_array = []
        for sentence in text:
            words = [word.lower() for word in sentence.split()]
            for word in words:
                if word not in words_array:
                    words_array.append(word)
        return words_array

    def fit_transform(self, text):
        """
        Создание терм-документальной матрицы
        -------------------------------------------------
        Параметры:
        ----------
        text - спискок строк, частоту которых будем изучать
        """
        self.words = self.find_array_of_words(text)
        term_matrix = []
        for sentence in text:
            elements = [word.lower() for word in sentence.split()]
            frequency_dict = defaultdict(int)
            for element in elements:
                frequency_dict[element] += 1
            sentence_array = []
            for word in self.words:
                sentence_array.append(frequency_dict[word])
            term_matrix.append(sentence_array)
        return term_matrix

    def get_feature_names(self):
        """Выводит список слов, для которых была построена терм-матрица"""
        return self.words


if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(count_matrix)
