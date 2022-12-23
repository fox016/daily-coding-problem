from collections import Counter

def anagram_indices(word, s):
    solution = []
    pos = 0
    l = len(word)
    end_pos = pos+l
    word_letter_counts = Counter(word)
    window = s[pos:end_pos]
    window_letter_counts = Counter(window)
    while True:
        if word_letter_counts == window_letter_counts:
            solution.append(pos)
        if end_pos == len(s):
            break
        letter_removed = s[pos]
        letter_added = s[end_pos]
        # Update window_letter_counts to reflect letter_removed and letter_added
        if window_letter_counts[letter_removed] == 1:
            del window_letter_counts[letter_removed]
        else:
            window_letter_counts[letter_removed]-=1
        if letter_added in window_letter_counts:
            window_letter_counts[letter_added]+=1
        else:
            window_letter_counts[letter_added]=1
        # Increment window positions
        pos+=1
        end_pos+=1
    return solution

print(anagram_indices("ab", "abxaba"))
