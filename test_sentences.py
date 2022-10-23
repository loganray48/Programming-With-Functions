from sentences import get_determiner, get_noun, get_verb, get_propostition, get_propostion_phrase
import random
import pytest


def test_get_determiner():
    # 1. Test the single determiners.

    single_determiners = ["a", "one", "the"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_determiner(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners


def test_get_noun():
    single_determiners = ["bird", "boy", "car", "cat", "child",
                          "dog", "girl", "man", "rabbit", "woman"]

    for _ in range(5):
        noun = get_noun(1)

        assert noun in single_determiners

    plural_determiners = ["birds", "boys", "cars", "cats", "children",
                          "dogs", "girls", "men", "rabbits", "women"]

    for _ in range(8):
        noun = get_noun(2)

        assert noun in plural_determiners


def test_get_verb():
    past_determiners = ["drank", "ate", "grew", "laughed", "thought",
                        "ran", "slept", "talked", "walked", "wrote"]

    for _ in range(7):
        verb = get_verb(1, 'past')

        assert verb in past_determiners

    present_determiners = ["drinks", "eats", "grows", "laughs", "thinks",
                           "runs", "sleeps", "talks", "walks", "writes"]

    for _ in range(6):
        verb = get_verb(1, 'present')

        assert verb in present_determiners

    present_plural = ["drink", "eat", "grow", "laugh", "think",
                      "run", "sleep", "talk", "walk", "write"]

    for _ in range(7):
        verb = get_verb(2, 'present')

        assert verb in present_plural

    future_determiners = ["will drink", "will eat", "will grow", "will laugh", "will think",
                          "will run", "will sleep", "will talk", "will walk", "will write"]

    for _ in range(7):
        verb = get_verb(1, 'future')

        assert verb in future_determiners


def test_get_proposition():
    determiners = ["about", "above", "across", "after", "along",
                   "around", "at", "before", "behind", "below",
                   "beyond", "by", "despite", "except", "for",
                   "from", "in", "into", "near", "of",
                   "off", "on", "onto", "out", "over",
                   "past", "to", "under", "with", "without"]

    for _ in range(8):
        propostion = get_propostition(1)

        assert propostion in determiners


def test_get_propostion_phrase():
    # word
    single_determiners = ["a", "one", "the"]
    plural_determiners = ["some", "many", "the"]
    # noun
    single_noun_determiners = ["bird", "boy", "car", "cat", "child",
                               "dog", "girl", "man", "rabbit", "woman"]
    plural_noun_determiners = ["birds", "boys", "cars", "cats", "children",
                               "dogs", "girls", "men", "rabbits", "women"]
    # propostion
    determiners = ["about", "above", "across", "after", "along",
                   "around", "at", "before", "behind", "below",
                   "beyond", "by", "despite", "except", "for",
                   "from", "in", "into", "near", "of",
                   "off", "on", "onto", "out", "over",
                   "past", "to", "under", "with", "without"]

    prop_phrase = get_propostion_phrase(1)

    prop_phrase = prop_phrase.split()
    assert prop_phrase[1] in single_determiners
    assert prop_phrase[2] in single_noun_determiners
    assert prop_phrase[0] in determiners

    for _ in range(7):
        prop_phrase = get_propostion_phrase(2)
        prop_phrase = prop_phrase.split()

        assert prop_phrase[1] in plural_determiners
        assert prop_phrase[2] in plural_noun_determiners
        assert prop_phrase[0] in determiners

# propostional_phrase = propostion + ' ' + word + ' ' + noun + '.'
        # 0         1      2         3          4                 5

pytest.main(["-v", "--tb=line", "-rN", __file__])

