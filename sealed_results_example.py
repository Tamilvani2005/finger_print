import base64
import os

from dotenv import load_dotenv

from fingerprint_pro_server_api_sdk.sealed import unseal_event_response, DecryptionKey, DecryptionAlgorithm

load_dotenv()

sealed_result = base64.b64decode(os.environ["BASE64_SEALED_RESULT"])
key = base64.b64decode(os.environ["BASE64_KEY"])

try:
    event_response = unseal_event_response(sealed_result, [DecryptionKey(key, DecryptionAlgorithm['Aes256Gcm'])])
    print("\n\n\nEvent response: \n", event_response.products)
except Exception as e:
    print("Exception when calling unsealing events response: %s\n" % e)
    exit(1)

print("Unseal successful!")

exit(0)
