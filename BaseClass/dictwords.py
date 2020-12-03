class SimpleDict:
    def __init__(self):
        self.dictionary = {}

    def get(self, letter):
        if letter == "":
            return self.dictionary.get("")
        if self.dictionary.get(letter) is None:
            self.dictionary[letter] = SimpleDict()
        return self.dictionary.get(letter)

    def include(self, letter):
        return not (self.dictionary.get(letter) is None)

    def add(self, val):
        if self.dictionary.get("") is None:
            self.dictionary[""] = []
        self.dictionary[""].append(val)

    def list(self):
        list_data = []
        list_data.extend(self.dictionary[""])
        for letter in self.dictionary:
            if letter != "":
                list_data.extend(self.dictionary[letter].list())

    def json(self):
        json_dic = {}
        for l in self.dictionary:
            if l == "":
                json_dic[""] = self.dictionary[""]
            else:
                json_dic[l] = self.dictionary[l].json()
        return json_dic


def format_word(word: str, inf: str, param: str):
    return {'inf': inf, "param": param}


class DictWords:
    def __init__(self):
        self.dictionary = SimpleDict()

    def add(self, word: str, inf: str, param):
        dic = self.dictionary
        for letter in word:
            dic = dic.get(letter)
        dic.add(format_word(word, inf, param))

    def get(self, word: str) -> list:
        dic = self.dictionary
        for letter in word:
            dic = dic.get(letter)
        return dic.get("")

    def list(self):
        list_data = []
        for letter in self.dictionary:
            list_data.extend(self.dictionary[letter].list())
        return list_data

    def json(self):
        return self.dictionary.json()

