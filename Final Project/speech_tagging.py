import numpy as np
import math

# Dictionary of tags and their corresponding words
training_dict = {}


def parse_training_data(file_name):
    print("Parsing training data...")
    with open(file_name) as file:
        text = file.read()
        # Store the sentences in a list where each element is a list of tags without whitespace
        sentences = []  # List of sentences where each sentence is a list of tags (so really a list of lists)
        for sentence in text.split("\n"):
            cur_word = sentence.rsplit('/', 1)[0]
            # Remove the words from the sentence leaving only the tags
            for word in cur_word.split():
                tag = word.rpartition('/')[2]
                # Whenever a ## is encountered, it means that the word is a new sentence
                if tag == "##":
                    sentences.append(['##'])
                else:
                    sentences[-1].append(tag)
        text = text.split()
        # Extract the tag from the word by taking everything past the rightmost slash as the tag
        for word in text:
            # Grab everything to the left of the rightmost slash as the current word
            cur_word = word.rpartition('/')[0]
            cur_tag = word.rsplit('/', 1)[1]
            # If the tag is not in the training dictionary, add it.
            # If a word is not in the tag's list of words, add it and keep track of how many times it appears
            # under that tag.
            if cur_tag not in training_dict:
                training_dict[cur_tag] = {}
                training_dict[cur_tag][cur_word] = 1
            else:
                if cur_word not in training_dict[cur_tag]:
                    training_dict[cur_tag][cur_word] = 1
                else:
                    training_dict[cur_tag][cur_word] += 1
        print("Training data parsed.")

    emission_probs = calculate_emission_probabilities()
    transition_probs = calculate_transition_probabilities(sentences)
    # Combine the transmission and emission scores into a single score estimation using log
    scores = {}
    for tag in transition_probs:
        for next_tag in transition_probs[tag]:
            transition_probs[tag][next_tag] = math.log(transition_probs[tag][next_tag], 10)
    for tag in emission_probs:
        for word in emission_probs[tag]:
            emission_probs[tag][word] = math.log(emission_probs[tag][word], 10)

    # Add all the transition probabilities for each tag to the emission probabilities for each word under that tag
    # and put them in scores
    for tag in transition_probs:
        for next_tag in transition_probs[tag]:
            scores[tag] = {}
            for word in emission_probs[tag]:
                scores[tag][word] = transition_probs[tag][next_tag] + emission_probs[tag][word]

    # Print out the scores
    # for tag in scores:
    #     print(tag, scores[tag])
    # print(scores.keys())
    viterbi_algorithm(scores, transition_probs, emission_probs, "## they can fish $$")
def calculate_emission_probabilities():
    """Calculates the emission and transition probabilities for each tag and word."""
    print("\nCalculating emission probabilities...")
    emission_probabilities = {}
    # Emission probabilities are calculated by dividing the number of times a word appears under a tag by the total
    # number of words under that tag.
    for tag in training_dict:
        emission_probabilities[tag] = {}
        total_words_in_tag = sum(training_dict[tag].values())
        for word in training_dict[tag]:
            # Calculate the probability of a word appearing under a tag and apply laplace smoothing
            # Calculation is: number of times a word appears under a tag + 1 /
            # total number of words under that tag + number of unique tags
            emission_probabilities[tag][word] = (training_dict[tag][word] + 1) / (total_words_in_tag +
                                                                                  abs(len(training_dict)))
    print("Emission probabilities calculated.")
          # Change the probabilities of the end ($$) of a sentence to be 0
    #emission_probabilities['$$']['$$'] = 0
    #print(emission_probabilities['$$']['$$'])
    return emission_probabilities


def calculate_transition_probabilities(sentences):
    """Calculates the transition probabilities for the corpus."""
    print("\nCalculating transition probabilities...")
    transition_probabilities = {}
    transition_occurrence_dict = {} # Create a dictionary of tags and the number of times each tag is followed by # every other tag
    for sentence in sentences:
        for i in range(len(sentence) - 1):
            cur_tag = sentence[i]
            next_tag = sentence[i + 1]
            if cur_tag not in transition_occurrence_dict:
                transition_occurrence_dict[cur_tag] = {}
                transition_occurrence_dict[cur_tag][next_tag] = 1
            else:
                if next_tag not in transition_occurrence_dict[cur_tag]:
                    transition_occurrence_dict[cur_tag][next_tag] = 1
                else:
                    transition_occurrence_dict[cur_tag][next_tag] += 1

    # Calculate the transition probabilities by dividing the number of times a tag is followed by another tag by the
    # total number of times that tag appears in the corpus, while applying laplace smoothing
    for tag in transition_occurrence_dict:
        transition_probabilities[tag] = {}
        total_tag_occurrences = sum(transition_occurrence_dict[tag].values())
        for next_tag in transition_occurrence_dict[tag]:
            transition_probabilities[tag][next_tag] = (transition_occurrence_dict[tag][next_tag] + 1) / (
                    total_tag_occurrences + abs(len(training_dict)))
    print("Transition probabilities calculated.")
    return transition_probabilities

def viterbi_algorithm(scores, transit_scores, emission_scores, sentence):
    # creating a dictionary based with the words and tags on the passes sentence
    Y = {}
    sentence = sentence.split()
    for word in sentence:
        for key in training_dict:
            for word_dict in training_dict[key]:
                if word == word_dict:
                    Y[word] = key

    print('Tags in the sentence:', Y.values())

    for key in Y:
        print(key)
        if key != '$$':
            vit_var_one = scores[Y[key]][key]
            print(vit_var_one)
        # V1(K) <- s1(k,diamond)
        # ok wtf is v1(k)
        # and what is s1(k,diamond)
        # how are you getting the tables
        # they is a pronoun


    for m in range(2,len(sentence)):
        for k in Y:
            pass
            #line 5
            #line 6
    #line 7
    for m in range(len(sentence)-1,1):
        pass
        # line 9
    return None





if __name__ == "__main__":
    parse_training_data("tagged_sentences.txt")
