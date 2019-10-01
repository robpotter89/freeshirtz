import tensorflow as tf
from helper import deprecated

NUM_SHIRTS = 69
SHIRT_MESSAGE = "Gimme shirt pls"


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


if __name__ == '__main__':
    print(ml_shirt_acquiry())
