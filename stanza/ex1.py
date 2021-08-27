import stanza

stanza.download('en')  # English model

nlp = stanza.Pipeline('en')

doc = nlp("Barack Obama was born in Hawaii.")  # get annotations for sentence

print(doc)
