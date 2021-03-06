import spacy
from termcolor import colored

str1 = "In a typical application, not all requests are equal: failing a new user sign-up request is different from failing a request polling for new email in the background."
str2 = " In many cases, however, availability calculated as the request success rate over all requests is a reasonable approximation of unplanned downtime, as viewed from the end-user perspective."
str3 = " When Sebastian Thrun started working on self-driving cars at Google in 2007, few people outside of the company took him seriously."


def get_colored_chunks(text):
    text = str1+str2
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)

    for chunk in doc.noun_chunks:
        text = text.replace(chunk.text, colored(chunk.text, 'green'))
        # text = text.replace(chunk.root.text, colored(chunk.root.text, 'yellow', 'on_green'))
    return text



text = str1+str2
print(get_colored_chunks(text))
