import uuid
import hashlib

print(uuid.uuid4())
print(uuid.uuid4().hex)

print(hashlib.md5(b"555"))
print(hashlib.md5(b"555").hexdigest())
