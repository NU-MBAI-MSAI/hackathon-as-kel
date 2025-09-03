'''Authors: Sneha Basu, Anisha Salunkhe'''

def countchars():
    st = input()
    exclude_set = {" ", ".", "!", ","}
    count = 0
    for char in st:
        if char not in exclude_set:
            count += 1
    return count

if __name__ == '__main__':
    print(countchars())