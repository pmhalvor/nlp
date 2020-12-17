import spacy
from spacy import displacy

nlp = spacy.load('en_core_web_sm')

str1 = "In a typical application, not all requests are equal: failing a new user sign-up request is different from failing a request polling for new email in the background."
str2 = " In many cases, however, availability calculated as the request success rate over all requests is a reasonable approximation of unplanned downtime, as viewed from the end-user perspective."
str3 = " When Sebastian Thrun started working on self-driving cars at Google in 2007, few people outside of the company took him seriously."


doc = nlp(str1+str2+str3)


for token in doc: 
    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
            token.shape_, token.is_alpha, token.is_stop)

    

## Visualizing
# options = {
#     'compact': True,
#     # 'add_lemma': True,
# }


sentence_spans = list(doc.sents)

displacy.serve(sentence_spans, style='dep', options= options)
# opens on 0.0.0.0:5000 