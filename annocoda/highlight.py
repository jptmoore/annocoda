
class Highlight:
    def __init__(self):
        pass
    
    def __markup_worker(self, term, keyword_list):
        if term.lower() in keyword_list:
            return f"<b>{term}</b>"
        else:
            return term

    def markup(self, search_value, text):
        search_terms = search_value.split()
        keywords = map(lambda t: t.lower(), search_terms)
        keyword_list = list(keywords)
        words = text.split()
        marked_up = map(lambda t: self.__markup_worker(t,keyword_list), words)
        result = ' '.join(marked_up)
        return result


data = [{'key': 'https://miiifystore.s3.eu-west-2.amazonaws.com/diamond_jubilee_of_the_metro/c/3/f88e6e3a-177b-4fec-a15d-7e3f8300c993', 'value': 'Harrow-on-the-Hill, crowned by church and school, is the capital of this Riding of Metro-land ; Ruislip and Northwood are its lake district; Eastcote and Ickenham, Harefield and Pinner are its rustic townships. London is at your very door, if you needs must keep in touch with London, but it is always pure country at the corner of the lane beyond your garden fence. The town has stained the country less here than in Essex, Kent or Surrey, at the same radius of ten or twenty miles from Charing Cross.', 'frag_selector': (324, 2125, 1057, 374)}]

h = Highlight()
result = h.markup("cat mat", "the cat sat on the mat")
print(result)
