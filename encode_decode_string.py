

def encode(self, strs: list[str]) -> str:
    encoded_string = str()

    for i in strs:
        encoded_string += str(len(i)) + "#" + i

    return encoded_string

def decode(self, s: str) -> list[str]:
    decoded_string, i = [], 0

    while i < len(s):
        j = i
        # Find the position of the delimiter
        while s[j] != "#":
            j += 1

        # Extract the length of the next string
        length = int(s[i:j])
        
        # Move i to the start of the actual string
        i = j + 1

        # Extract exactly 'length' characters
        # Fix: use i as the base for the slice
        decoded_string.append(s[i : i + length])
        
        # Move i to the start of the next length-prefix
        i += length

    return decoded_string