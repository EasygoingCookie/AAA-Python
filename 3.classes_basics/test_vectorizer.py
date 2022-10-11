from sklearn.feature_extraction.text import CountVectorizer
from vectorizer import CountVectorizer as MyVectorizer


def test_can_get_feature_names():
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    sk_vectorizer = CountVectorizer()
    sk_count_matrix = sk_vectorizer.fit_transform(corpus)
    my_vectorizer = MyVectorizer()
    my_count_matrix = my_vectorizer.fit_transform(corpus)
    assert set(sk_vectorizer.get_feature_names()) == set(my_vectorizer.get_feature_names()), (
        "get_feature_names() works incorrectly"
    )


def test_can_fit_transform():
    corpus2 = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste',
        'pasta pasta boil boil pizza pizza PIZZA omg',
        'pot pot pot pot pot pot pot pot pot pot pot',
        'pasta never pizza',
        'Ilon Mask wants to kill my cat',
        'Ilon Ilon Ilon wants to eat my pasta'
    ]
    sk_vectorizer = CountVectorizer()
    sk_count_matrix = sk_vectorizer.fit_transform(corpus2)
    my_vectorizer = MyVectorizer()
    my_count_matrix = my_vectorizer.fit_transform(corpus2)
    for a, b in zip(sk_count_matrix.toarray(), my_count_matrix):
        assert sorted(a) == sorted(b), (
        "fit_transform() works incorrectly"
    )
