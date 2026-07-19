# This has nothing to do with the actual CTF itself, its just to validate answers.

import sys, hashlib

flag_hashes = {
    "puzzle 1": "fe6a30203e4f5f5a94ab8fb6f8535e2630926f242b6fbd5aae296922a2beaa53",
    "puzzle 2": "0cab9f8f148cd25ad7c109957421adcdd439e533c196016052b0530307931039"
}

try:
    userguess = sys.argv[1]
    guess_hash = hashlib.sha256(userguess.encode()).hexdigest()

    flag = next((k for k, v in flag_hashes.items() if v == guess_hash), None)

    if flag:
        print(f"Well done, you found the flag for {flag} ({userguess})!")
    else:
        print(f"{userguess} doesn't match any flag")

except IndexError:
    print("Incorrect usage (eg, \"python3 check.py flag{EXAMPLE}\")")

# Thank you for trying!!!
