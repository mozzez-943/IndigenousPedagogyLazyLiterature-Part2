import random

# Load English and Babine texts
with open('english.txt', 'r') as file:
    english_text = file.readlines()
with open('babine.txt', 'r') as file:
    babine_text = file.readlines()


# Function to generate random 1-gram sentences
def generate_1gram_text(text, n):
    sentences = []
    for _ in range(n):
        sentence = ''
        for _ in range(10):
            sentence += random.choice(text)
        sentences.append(sentence)
    return sentences


# def generate_1gram_sentences(text, num_sentences=5):
#     words = [word for sentence in text for word in sentence.split()]
#     sentences = []
#     for _ in range(num_sentences):
#         sentence = ' '.join(random.choice(words) for _ in range(random.randint(3, 7)))
#         sentences.append(sentence)
#     return sentences

# # Generate and compare English and Babine sentences
# english_sentences = generate_1gram_sentences(english_text)
# babine_sentences = generate_1gram_sentences(babine_text)

# print("Generated English Sentences:")
# for sentence in english_sentences:
#     print(sentence)

# print("\nGenerated Babine Sentences:")
# for sentence in babine_sentences:
#     print(sentence)
