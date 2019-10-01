import tensorflow as tf

NUM_SHIRTS = 69
SHIRT_MESSAGE = "Gimme shirt pls"


def brute_force_shirt(num_shirts=NUM_SHIRTS, shirt_message=SHIRT_MESSAGE):
    for i in range(num_shirts):
        print(shirt_message)


def ml_shirt_acquiry():
    shirt = tf.constant("Gimme a t-shirt")
    sess = tf.Session()
    return sess.run(shirt)


if __name__ == '__main__':
    print(ml_shirt_acquiry())
