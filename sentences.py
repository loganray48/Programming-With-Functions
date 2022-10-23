# Program which generates simple sentences
import random


def main():
    quantity = [1, 2]
    tense = ["past", "present", "future"]
    for q in quantity:
        for t in tense:
            word = get_determiner(q)
            noun = get_noun(q)
            verb = get_verb(q, t)
            propostion_phrase = get_propostion_phrase(quantity)
            print(word.capitalize(), noun, verb, propostion_phrase)


def get_determiner(quantity):
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    word = random.choice(words)
    return word


def get_noun(quantity):
    if quantity == 1:
        noun = ["bird", "boy", "car", "cat", "child",
                "dog", "girl", "man", "rabbit", "woman"]
    else:
        noun = ["birds", "boys", "cars", "cats", "children",
                "dogs", "girls", "men", "rabbits", "women"]

    noun = random.choice(noun)

    return noun


def get_verb(quantity, tense):
    if tense == "past":
        verb = ["drank", "ate", "grew", "laughed", "thought",
                "ran", "slept", "talked", "walked", "wrote"]

    if tense == "present" and quantity == 1:
        verb = ["drinks", "eats", "grows", "laughs", "thinks",
                "runs", "sleeps", "talks", "walks", "writes"]

    if tense == "present" and quantity != 1:
        verb = ["drink", "eat", "grow", "laugh", "think",
                "run", "sleep", "talk", "walk", "write"]

    if tense == "future":
        verb = ["will drink", "will eat", "will grow", "will laugh", "will think",
                "will run", "will sleep", "will talk", "will walk", "will write"]

    verb = random.choice(verb)

    return verb


def get_propostition(propostion):
    propostion = ["about", "above", "across", "after", "along",
                  "around", "at", "before", "behind", "below",
                  "beyond", "by", "despite", "except", "for",
                  "from", "in", "into", "near", "of",
                  "off", "on", "onto", "out", "over",
                  "past", "to", "under", "with", "without"]

    propostion = random.choice(propostion)

    return propostion


def get_propostion_phrase(quantity):

    word = get_determiner(quantity)
    noun = get_noun(quantity)
    propostion = get_propostition(quantity)
    propostional_phrase = propostion + ' ' + word + ' ' + noun

    return propostional_phrase


main()
