"""
Author - Adish Pathare
Description - Dynamic Programming approach to find
longest increasing subsequence length in an array
"""


def longest_increasing_subsequence(a, n):
    if n == 0:
        return 1
    s = []
    for i in range(n):
        s.append(0)
    for k in range(0, n):
        s[k] = 1
        for j in range(0, k):
            if a[j] < a[k] and s[k] < s[j] + 1:
                s[k] = s[j] + 1
    longest_increasing_subsequence_length = max(s)

    return longest_increasing_subsequence_length


def main():
    a = [2, 3, 1, 7, 4, 6, 9, 5]
    n = len(a)
    print(longest_increasing_subsequence(a, n))


if __name__ == '__main__':
    main()
