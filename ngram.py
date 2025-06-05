import random
import re

def preprocess_text(text):
    # Lowercase and remove non-alphanumeric characters (except spaces)
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text.lower())
    return text.split()


def generate_tokens_and_vocabulary(text):
    # Preprocess and tokenize the text
    tokens = preprocess_text(text)

    # Calculate the number of tokens
    num_tokens = len(tokens)

    # Calculate the vocabulary (set of unique tokens)
    vocabulary = set(tokens)
    num_unique_words = len(vocabulary)

    return num_tokens, num_unique_words, vocabulary


def unigram_model(words):
    # Count total words
    total_words = len(words)

    # Get the count of each word (frequency)
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    # Calculate unigram probabilities
    unigram_probs = {word: count / total_words for word, count in word_counts.items()}

    return unigram_probs, word_counts


def bigram_model(words):
    # Create bigrams (word pairs)
    bigram_counts = {}
    unigram_counts = {}

    for i in range(len(words) - 1):
        word1 = words[i]
        word2 = words[i + 1]

        # Count bigrams
        bigram = (word1, word2)
        bigram_counts[bigram] = bigram_counts.get(bigram, 0) + 1

        # Count unigrams
        unigram_counts[word1] = unigram_counts.get(word1, 0) + 1

    # Add the count of the last word in unigram counts
    unigram_counts[words[-1]] = unigram_counts.get(words[-1], 0) + 1

    # Calculate bigram probabilities
    bigram_probs = {bigram: round(count / unigram_counts[bigram[0]], 3) for bigram, count in bigram_counts.items()}

    print("\n ======================= Probailites of BiGram model ========================= \n")
    print(bigram_probs)

    return bigram_probs, unigram_counts


def generate_sentence_using_unigram(unigram_probs, starting_word, length=10):
    words = list(unigram_probs.keys())
    probabilities = list(unigram_probs.values())

    # Generate sentence by selecting words based on unigram probabilities
    sentence = [starting_word]
    for _ in range(length):
        word = random.choices(words, probabilities)[0]
        sentence.append(word)

    return ' '.join(sentence)


def generate_sentence_using_bigram(bigram_probs, start_word, length=10):
    sentence = [start_word]
    current_word = start_word

    for _ in range(length - 1):
        # Filter bigram probabilities for the current word
        next_word_candidates = {bigram[1]: prob for bigram, prob in bigram_probs.items() if bigram[0] == current_word}

        # If no candidates are found, end the sentence
        if not next_word_candidates:
            break

        # Choose the next word based on bigram probabilities
        next_words = list(next_word_candidates.keys())
        probabilities = list(next_word_candidates.values())
        next_word = random.choices(next_words, probabilities)[0]

        # Add the chosen word to the sentence
        sentence.append(next_word)
        current_word = next_word

    return ' '.join(sentence)


def main():
    # Input text
    text = """Defender Micah Richards made his England debut shortly after Eriksson left the England job in 2006 but played under the Swede
    when he took charge of Manchester City a year later. His man-management was as good as I ever experienced and it meant I could play
    my best football under him, Richards, now a pundit on the BBC, said."""


    # text = """
    # Scientists are hoping that access to more than 1.6 million brain scans collected from patients across Scotland could help predict a person’s risk of dementia.
    # A team of 20 researchers from the universities of Edinburgh and Dundee have been given unprecedented permission to view a huge number of anonymous scans gathered from across the Scottish population over a decade.
    # It is the first time scientists in the UK have had access to such large volumes of valuable data.
    # They will use artificial intelligence (AI) to analyse the scans to see if there are patterns or signs of dementia.
    # Dementia is characterised by the build-up of different types of protein in the brain, which damages brain tissue and leads to cognitive decline.
    # Molecular and cellular changes to the brain usually begin many years before any symptoms occur.
    # What is Alzheimer's and how common is it?
    # My pre-death grief over husband's dementia
    # The researchers hope that by studying such a large number of brain scans they can develop tools that will help radiologists with early detection.
    # The scientists have been given permission by NHS Scotland to use 1.6 million CT and MRI images collected during routine clinical care between 2008 and 2018.
    # Previous research has been limited by access to much smaller numbers of scans.
    # The decision to grant permission to study so many scans was taken by NHS Scotland’s Public Benefit and Privacy Panel for Health and Social Care, whose role is to make sure applicants have thought through the public benefit and privacy implications.
    # All of the scans will be anonymised so researchers know nothing about the patients whose scans they are studying.

    # """

    # Preprocess text
    words = preprocess_text(text)

    # Calculate unigram and bigram probabilities
    unigram_probs, _ = unigram_model(words)
    bigram_probs, _ = bigram_model(words)

    print("\n ======================= Tokens and Vacabulary ======================== \n")

    num_tokens, num_unique_words, vocabulary = generate_tokens_and_vocabulary(text)
    print("N: ", num_tokens)
    print("V: ", num_unique_words)

    print("\n ============= Genegrating sentences using language model ============= \n")

    start_word = random.choice(words)
    print("Choosen Starting Word: ", start_word, "\n")


    # Generate sentences
    unigram_sentence = generate_sentence_using_unigram(unigram_probs, start_word, length=10)
    bigram_sentence = generate_sentence_using_bigram(bigram_probs, start_word, length=10)

    print("Sentence generated using Unigram Model:")
    print(unigram_sentence)
    print("\nSentence generated using Bigram Model:")
    print(bigram_sentence)

if __name__ == "__main__":
    main()
