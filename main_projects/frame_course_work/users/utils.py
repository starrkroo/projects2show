
import random
import string


def random_ssh_key():
    return ''.join(random.choice(string.ascii_letters) for _ in range(10))
