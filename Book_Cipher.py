import re

text = "We talk about social issues, political events and technological progress all the time. In other words, we wish and are witnessing our world to be a better one. Since there is a better world other than this one, it implies our world is not perfect. Is there really a more perfect world? What roles has perfection played in Descartes’ and Leibniz’s philosophical writings? Both philosophers considered God to be the “perfection.” If that is true, how do we reconcile God’s existence with issues we face daily? In this essay I attempt to analyze, examine and compared the notion of “Perfection” on both philosophers’ work. "


def get_words(text):
    text.replace(",", "")
    text.replace(".", "")
    list_of_words = list()
    words =  re.split(r'\s+', text)
    # return list_of_words
    for word in words:
        list_of_words.append(word.upper())
    return list_of_words



