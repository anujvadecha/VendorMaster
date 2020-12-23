import hashlib
import random
import string

def random_string_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_transaction_id_generator():
    transaction_new_id = random_string_generator()
    # t_id_exists = Klass.objects.filter(transaction_id=transaction_new_id).exists()
    return transaction_new_id

def otp_hash(otp):
    return int(hashlib.sha1(str(otp).encode("utf-8")).hexdigest(), 16) % (10 ** 4)

