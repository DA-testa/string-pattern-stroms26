# python3


def read_input():
    input_type = input().rstrip()
    if input_type == 'I':
        pattern = input().rstrip()
        text = input().rstrip()
    elif input_type == 'F':
        with open('test.txt', 'r') as file:
            pattern = file.readline().rstrip()
            text = file.readline().rstrip()
    return pattern, text

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    p = 10**9+7
    x = 263
    m, n = len(pattern), len(text)
    h = pow(x, m-1, p)
    pattern_hash = sum(ord(pattern[i])*pow(x, i, p) for i in range(m)) % p
    text_hash = sum(ord(text[i])*pow(x, i, p) for i in range(m)) % p
    occurances = []
    for i in range(n-m+1):
        if pattern_hash == text_hash and pattern == text[i:i+m]:
            occurances.append(i)
        if i < n-m:
            text_hash = (text_hash - ord(text[i])*h) % p
            text_hash = (text_hash*x + ord(text[i+m])) % p
            text_hash = (text_hash + p) % p
    return occurances

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
