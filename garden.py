# garden.py

import spacy

# Load the English NLP model
nlp = spacy.load("en_core_web_sm")

# List of garden path sentences
gardenpathSentences = [
    "The old man the boat.", # Garden path sentence example 1
    "The horse raced past the barn fell.", # Garden path sentence example 2
    "Mary gave the child a Band-Aid.", # Provided sentence 1
    "That Jill is never here hurts.", # Provided sentence 2
    "The cotton clothing is made of grows in Mississippi." # Provided sentence 3
]

# Tokenize and perform named entity recognition on each sentence
for sentence in gardenpathSentences:
    doc = nlp(sentence)
    print(f"Sentence: {sentence}")
    for token in doc:
        print(f"Token: {token.text}, POS: {token.pos_}, DEP: {token.dep_}")

    # Check for named entities in the sentence
    if doc.ents:
        for ent in doc.ents:
            print(f"Entity: {ent.text}, Label: {ent.label_}, Explanation: {spacy.explain(ent.label_)}")
    else:
        print("No named entities found.")
    print("\n")

# Example of looked up entities
print("Entity Lookup Examples:")
print("GPE:", spacy.explain("GPE"))
print("ORG:", spacy.explain("ORG"))

# Comment about looked up entities
"""
1. GPE: Stands for Geopolitical Entity. It refers to countries, cities, states. It makes sense as it's commonly used to identify locations in a text.
2. ORG: Stands for Organization. It includes companies, agencies, institutions. This entity makes sense as it helps in recognizing organizations mentioned in a sentence.
"""
