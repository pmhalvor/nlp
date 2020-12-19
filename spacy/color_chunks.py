import spacy
from termcolor import colored

str1 = "In a typical application, not all requests are equal: failing a new user sign-up request is different from failing a request polling for new email in the background."
str2 = " In many cases, however, availability calculated as the request success rate over all requests is a reasonable approximation of unplanned downtime, as viewed from the end-user perspective."
str3 = " When Sebastian Thrun started working on self-driving cars at Google in 2007, few people outside of the company took him seriously."


def get_colored_chunks(text, markdown=False, color='green', norwegian=False):
    ###### EXPORT THIS TO STATE OF CLASS ######
    if norwegian: 
        nlp = spacy.load('nb_core_web_sm')
    else:
        nlp = spacy.load("en_core_web_sm")
    ###########################################
    
    doc = nlp(text)

    sentence_spans = list(doc.sents)

    for sentence in sentence_spans:
        color_sentence = sentence.text
        for chunk in sentence.noun_chunks:
            ###### EXPORT THIS TO STATE OF CLASS ######
            if markdown:
                # make sure no # get caught in mark
                pre = ''
                chunk_text = chunk.text  
                if '##' in chunk.text:
                    pre = '## '
                    chunk_text = chunk_text.strip('## ')
                elif '#' in chunk_text:
                    pre = '# '
                    chunk_text = chunk_text.strip(('# '))
                
                replacement = pre+f'<mark><span style="color:{color}">{chunk_text}</span></mark>'
            else:
                replacement = pre+colored(chunk_text, color, 'on_yellow')
            ###########################################


            color_sentence = color_sentence.replace(chunk.text, replacement)
            # still doesnt check mulitple instances of chunk in sentence
            # implement this error as a text later
        text = text.replace(sentence.text, color_sentence)
    return text


if __name__=='__main__':
    text = str1+str2
    print(get_colored_chunks(text))
