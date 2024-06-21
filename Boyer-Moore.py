def bad_character_heuristic(pattern):
    bad_char = [-1] * 256  # 256 ASCII characters

    for i in range(len(pattern)):
        bad_char[ord(pattern[i])] = i

    return bad_char

def good_suffix_heuristic(pattern):
    m = len(pattern)
    good_suffix = [0] * m
    border_pos = [0] * (m + 1)

    i = m
    j = m + 1
    border_pos[i] = j

    while i > 0:
        while j <= m and pattern[i - 1] != pattern[j - 1]:
            if good_suffix[j - 1] == 0:
                good_suffix[j - 1] = j - i
            j = border_pos[j]
        i -= 1
        j -= 1
        border_pos[i] = j

    j = border_pos[0]
    for i in range(m):
        if good_suffix[i] == 0:
            good_suffix[i] = j
        if i + 1 == j:
            j = border_pos[j]

    return good_suffix

def boyer_moore_search(text, pattern):
    n = len(text)
    m = len(pattern)
    if m == 0:
        return []  # No pattern to search

    bad_char = bad_character_heuristic(pattern)
    good_suffix = good_suffix_heuristic(pattern)

    s = 0  # Shift of the pattern with respect to text
    occurrences = []

    while s <= n - m:
        j = m - 1

        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        if j < 0:
            occurrences.append(s)
            s += good_suffix[0]
        else:
            s += max(good_suffix[j], j - bad_char[ord(text[s + j])])

    return occurrences

# Example usage
text = "ABAAABCDABCD"
pattern = "ABCD"
result = boyer_moore_search(text, pattern)
print("Pattern found at positions:", result)
