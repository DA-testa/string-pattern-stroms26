def read_input():
    input_type = input().rstrip()

    if input_type == 'I':
        return read_user_input()
    elif input_type == 'F':
        filename = "06"
        return read_file(filename)
    else:
        raise ValueError(f"Invalid input type: {input_type}")

def read_file(filename):
    try:
        with open(f"./tests/{filename}") as f:
            pattern = f.readline().rstrip()
            text = f.readline().rstrip()
            return pattern, text
    except FileNotFoundError:
        raise FileNotFoundError(f"File {filename} not found")
    except: 
        raise ValueError(f"Error reading {filename}")

def read_user_input():
    pattern = input().rstrip()
    text = input().rstrip()
    
    return pattern, text
    

def print_occurrences(output):
    output = sorted(output)
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    prime = 10**9 + 7
    base = 256

    pattern_len, text_len = len(pattern), len(text)
    pattern_hash = compute_hash(pattern, prime, base)
    text_hash = compute_hash(text[:pattern_len], prime, base)
    occur = set()
    if pattern_hash == text_hash and pattern == text[:pattern_len]:
        occur.add(0)
    for i in range(1, text_len - pattern_len + 1):
        
        text_hash = ((text_hash * base) % prime + ord(text[i + pattern_len -1]) - (ord(text[i -1]) * pow(base, pattern_len, prime)) % prime) % prime
        if pattern_hash == text_hash and pattern == text[i:i + pattern_len]:
            occur.add(i)
    return occur

def compute_hash(text, prime, base):
    hash_val = 0
    for char in text:
        hash_val = (hash_val * base + ord(char)) % prime
    return hash_val

# this part launches the functions
if __name__ == '__main__':
    pattern, text = read_input()
    occurrences = get_occurrences(pattern, text)
    print_occurrences(occurrences)
