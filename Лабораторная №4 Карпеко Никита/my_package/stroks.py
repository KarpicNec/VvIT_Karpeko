def reverse_str(s):
    return s[::-1]


def is_palindrom(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

