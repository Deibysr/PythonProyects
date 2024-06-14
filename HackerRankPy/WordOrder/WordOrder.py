import sys
from collections import OrderedDict

def main():
    # Read the number of words
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    words = data[1:]
    
    # Dictionary to keep track of word counts while maintaining order
    word_count = OrderedDict()
    
    # Count the occurrences of each word
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    # Output the number of distinct words
    print(len(word_count))
    
    # Output the counts of each word in the order of their first appearance
    print(' '.join(map(str, word_count.values())))

if __name__ == "__main__":
    main()