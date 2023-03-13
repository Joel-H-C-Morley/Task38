import spacy
nlp = spacy.load('en_core_web_md')

# Examples from the PDF
'''word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))'''

# Own examples, wanted to see how low I could make the similarity coefficient
word1 = nlp("syringe")
word2 = nlp("sun")
word3 = nlp("malaise")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

'''tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))'''

sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)

################################################################
#                Notes for task questions                      #
################################################################

# a cat is half as related to a banana than a monkey is to a banana
# a cat is 3 times more related to a monkey than a banana