from collections import Counter


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        seq = ""
        letters = Counter(s)
        while letters:
            sorted_letters = sorted(letters.keys())
            largest_letter = sorted_letters[-1]
            if len(seq) == 0 or seq[-1] != largest_letter:
                letter_count = letters[largest_letter]
                if letter_count > repeatLimit:
                    letters[largest_letter] -= repeatLimit
                    seq += largest_letter*repeatLimit
                else:
                    del letters[largest_letter]
                    seq += largest_letter*letter_count
            else:
                if len(sorted_letters) >= 2:
                    prev_largest_letter = sorted_letters[-2]
                    letters[prev_largest_letter] -= 1
                    seq += prev_largest_letter
                    if letters[prev_largest_letter] == 0:
                        del letters[prev_largest_letter]
                else:
                    break
        return "".join(seq)


if __name__ == '__main__':
    s = "aababab"
    repeatLimit = 2
    print(Solution().repeatLimitedString(s, repeatLimit))