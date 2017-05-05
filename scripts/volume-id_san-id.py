import base64
import uuid

name = input("Enter Id within quotes......")

uuid_str = name.replace("-", "")
vol_uuid = uuid.UUID('urn:uuid:%s' % uuid_str)
vol_encoded = base64.urlsafe_b64encode(vol_uuid.bytes)

print(vol_encoded[:19])
