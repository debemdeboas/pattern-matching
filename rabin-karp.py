
from functools import lru_cache


def to_val(c: str) -> int:
    # return ord(c) - 96
    return ord(c)


@lru_cache(256)
def to_hash_value(char: str, prime: int, n: int) -> int:
    return to_val(char) * pow(prime, n)


def rabin_karp_rolling_hash(text: str, old_hash: int = 0, old_char: str =  '', new_char: str = '') -> int:
    """
    Rabin-Karp rolling hash algorithm implementation.

    If the function called with no extra paremeters (except for `text`), no rolling hash is done;
    the text is hashed as-is since we have no `old_hash` from which to calculate the new hash.
    
    When this function gets called with `old_hash != 0`, we use a rolling hash algorithm similar
    to Rabin's Fingerprint:

    ```math
    m = len(text)
    new_hash = old_hash - val(old_char)
    new_hash = new_hash // prime
    new_hash = new_hash + (val(new_char) * pow(prime, m - 1))
    ```
    
    This will effectively remove the first character's value from the old hash and allow us to,
    in practice, "append" the new character's hash value to the old hash, generating a new hash.

    Args:
        text (str):
            String to be hashed.
        old_hash (int, optional):
            Old hash value (for the rolling hash). Defaults to 0.
        old_char (str, optional):
            Old character that has been removed from `old_hash`. Defaults to ''.
        new_char (str, optional):
            New character to be added to the end of the hash. Defaults to ''.

    Returns:
        int:
            Hashed `text`.
    """

    PRIME = 3 # Random prime number
    res = 0
    if old_hash == 0:
        # Calculate hash from nothing
        for i, c in enumerate(text):
            res += to_hash_value(c, PRIME, i)
    else: # Rolling hash
        return ((old_hash - to_val(old_char)) // PRIME) + \
                to_hash_value(new_char, PRIME, len(text) - 1)
    return res


def rabin_karp_pattern_match(pattern: str, text: str):
    p_len = len(pattern)
    p_hash = rabin_karp_rolling_hash(pattern)

    old_char = ''
    curr_hash = 0
    for i, c in enumerate(text):
        curr_text = text[i:i+p_len]

        if len(curr_text) != p_len:
            print('String has ended, no match was found')
            return

        curr_hash = rabin_karp_rolling_hash(curr_text, curr_hash, old_char, curr_text[-1])
        old_char = c

        if curr_hash == p_hash \
            and pattern == curr_text:
            print(f'Match was found starting at index {i} for pattern with hash {p_hash}')
            return


rabin_karp_pattern_match('eda', 'abeda')
