from BaseClass.dictwords import DictWords


def inf_form(word: str) -> list:
    """
    return list of possible infinitives
    first call will take some time, next time it will execute immediately
    :param word:
    :return: list of str
    """
    d = UkWordDictionary()

    res = []
    for w in d.get(word):
        if w['inf'] not in res:
            res.append(w['inf'])
    return res


def word_info(word: str) -> list:
    """
    return list of possible infinitives
    first call will take some time, next time it will execute immediately
    :param word:
    :return: list of dict {'inf', 'param'}
    """
    d = UkWordDictionary()
    return d.get(word)


class UkWordDictionary(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(UkWordDictionary, cls).__new__(cls)

            cls.dict_words = DictWords()
            f = open("dict_ext/dict_corp_lt.txt", encoding="UTF-8", mode="r")
            i = 0
            print("Loading dictionary")
            while True:
                i += 1
                line = f.readline()
                if not line:
                    break
                word, inf, param = line[:-1].split(" ")
                cls.dict_words.add(word, inf, param)
                if i % 100000 == 0:
                    print(i)
            f.close()
            print("Loading dictionary successful!")
        return cls.dict_words
