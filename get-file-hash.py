import os
import hashlib

def run(path):
    path = os.path.expanduser(path)
    path = os.path.expandvars(path)
    if os.path.isabs(path):
        final_output = md5(path)
        return final_output


def md5(file_path):
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return(hash_md5.hexdigest())
