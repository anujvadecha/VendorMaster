import hashlib

def otp_hash(otp):
    return int(hashlib.sha1(str(otp).encode("utf-8")).hexdigest(), 16) % (10 ** 4)