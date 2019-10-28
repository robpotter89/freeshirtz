import tensorflow as tf
from helper import deprecated
from bktree import BKTree

NUM_SHIRTS = 69
SHIRT_MESSAGE = "Gimme shirt pls"
TREE = BKTree()


@deprecated
def brute_force_shirt(num_shirts=NUM_SHIRTS, shirt_message=SHIRT_MESSAGE):
    shirt_requests = []
    for i in range(num_shirts):
        shirt_requests.append(shirt_message)
    
    return shirt_requests


def ml_shirt_acquiry():
    shirt = tf.constant(SHIRT_MESSAGE)
    sess = tf.Session()
    return sess.run(shirt)


def spell_check(word):
    with open('/usr/share/dict/words') as f:
        possible_words = [w.replace('\n', '') for w in f.readlines()]


def word_path(word):
    return TREE.find_words(word)


if __name__ == '__main__':
    print(ml_shirt_acquiry())
