
from typing import List


def build_prefix_suffix_array(s: str) -> List[int]:
    """
    Build the prefix/suffix indexes array.

    Example:
    Given an input string 'ABCABAD', the generated array will be:
    ['A', 'B', 'C', 'A', 'B', 'A', 'D', 'A']
    [ 0,   0,   0,   1,   2,   1,   0,   1 ]

    This function is O(n).

    Args:
        s (str):
            Text to be checked for prefixes/suffixes.

    Returns:
        List[int]:
            List of indexes.
    """
    i = 1
    j = 0
    arr = [0] * len(s)
    while i < len(s):
        if s[i] == s[j]:
            j += 1
            arr[i] = j
        else:
            if j != 0:
                j = arr[j - 1]
                i -= 1
            else:
                arr[j] = 0
        i += 1
    return arr


def kmp_search(pattern: str, text: str):
    """
    Knutt-Morris-Pratt search algorithm.

    This function is O(n) (pre-processing) + O(m) (pattern matching) -> O(m + n)

    Args:
        pattern (str)
        text (str)
    """
    
    t_len = len(text)
    t_index = 0

    p_len = len(pattern)
    p_index = 0
    pattern_index_array = build_prefix_suffix_array(pattern)

    b_found = False
    while t_index < t_len:
        if pattern[p_index] == text[t_index]: # Match - move forward one
            p_index += 1
            t_index += 1

        if p_index == p_len: # Done
            print(f'Match was found starting at index {t_index - p_index}')
            b_found = True
            p_index = pattern_index_array[p_index - 1]
        elif t_index < t_len and pattern[p_index] != text[t_index]: # Mistmatch
            if p_index != 0:
                # Go to the last position on the array because everything that has come
                # before the mismatch will always match.
                p_index = pattern_index_array[p_index - 1]
            else:
                t_index += 1

    if not b_found:
        print('No matches were found')


kmp_search('aabaabaaa', 'eeeeeeeaefefaea2w23aeiofaefeeeeeeeeeeeeeeeeaabaabaaaeaabaabaaa')
