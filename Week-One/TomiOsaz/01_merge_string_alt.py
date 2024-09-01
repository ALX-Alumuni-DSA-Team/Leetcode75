# Q1

def mergeAlternately(string1, string2):
    i, j = 0, 0
    merged_string = []

    while i < len(string1) and j < len(string2):
        merged_string.append(string1[i])
        merged_string.append(string2[j])
        i += 1
        j += 1

    # Append the remaining characters from the longer string
    merged_string.append(string1[i:])
    merged_string.append(string2[j:])

    return ''.join(merged_string)

# Trial run 1
print(mergeAlternately("Casfcto", "lsiiain"))  # Output: "Classification"

# Trial run 2
print(mergeAlternately("McieLann n ersin", "ahn erigadRgeso"))
