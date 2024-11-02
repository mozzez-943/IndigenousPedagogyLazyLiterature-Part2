import random

# Replace text with the text file you want to use
with open('add_excerpt_name.txt', 'r') as file:
    babine_text = file.readlines()
with open('eg1_eng.txt', 'r') as file:
    english_text = file.readlines()

# Generate 1-gram sentences
def generate_1gram(text, n):
    sentences = []
    # Generate n sentences
    for _ in range(n):
        sentence = ''
        for _ in range(10):
            sentence += random.choice(text)
        sentences.append(sentence)
    return sentences