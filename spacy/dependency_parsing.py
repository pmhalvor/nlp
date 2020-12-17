import spacy

str1 = "In a typical application, not all requests are equal: failing a new user sign-up request is different from failing a request polling for new email in the background."
str2 = " In many cases, however, availability calculated as the request success rate over all requests is a reasonable approximation of unplanned downtime, as viewed from the end-user perspective."
str3 = " When Sebastian Thrun started working on self-driving cars at Google in 2007, few people outside of the company took him seriously."



nlp = spacy.load("en_core_web_sm")
doc = nlp(str1)

print('root.dep_', '|', 'text', '|','root.text','|', 
            'root.head.text', '\n')

for chunk in doc.noun_chunks:
    print(chunk.root.dep_, '|', chunk.text, '|',chunk.root.text,'|', 
            chunk.root.head.text, '\n')
