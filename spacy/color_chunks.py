import spacy
from termcolor import colored

str1 = "In a typical application, not all requests are equal: failing a new user sign-up request is different from failing a request polling for new email in the background."
str2 = " In many cases, however, availability calculated as the request success rate over all requests is a reasonable approximation of unplanned downtime, as viewed from the end-user perspective."
str3 = " When Sebastian Thrun started working on self-driving cars at Google in 2007, few people outside of the company took him seriously."


def get_colored_chunks(text, markdown=False, color='green', norwegian=False):
    if norwegian: 
        nlp = spacy.load('nb_core_web_sm')
    else:
        nlp = spacy.load("en_core_web_sm")
    
    doc = nlp(text)

    sentence_spans = list(doc.sents)

    ### need to handle mutliple sentences
    ### need to replace only current chunk
    ### need to stay as general as possible

    for chunk in doc.noun_chunks:
        if markdown:
            replacement = f'<mark><span style="color:{color}">{chunk.text}</span></mark>'
        else:
            replacement = colored(chunk.text, 'green')
            # text = text.replace(chunk.root.text, colored(chunk.root.text, 'yellow', 'on_green'))
        
        text = text.replace(chunk.text, replacement)
    return text


if __name__=='__main__':
    text = str1+str2
    print(get_colored_chunks(text))
