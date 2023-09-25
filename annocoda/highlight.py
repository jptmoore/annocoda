class Highlight:
    def __init__(self):
        pass

    def __markup_worker(self, term, keyword_list):
        if term.lower() in keyword_list:
            return f"**{term}**"
        else:
            return term

    def __markup(self, search_value, text):
        search_terms = search_value.split()
        keywords = map(lambda x: x.lower(), search_terms)
        keyword_list = list(keywords)
        words = text.split()
        marked_up = map(lambda x: self.__markup_worker(x, keyword_list), words)
        result = " ".join(marked_up)
        return result

    def __run_worker(self, search_value, dictionary):
        dict_value = dictionary["value"]
        marked_value = self.__markup(search_value, dict_value)
        dictionary |= {"value": marked_value}
        return dictionary

    def run(self, search_value, annotations):
        result = map(lambda x: self.__run_worker(search_value, x), annotations)
        return list(result)

