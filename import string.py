import string

counts = 0                          
dictionary_counts = dict()
lst = list()

lineinput = input("Enter the string ")

for n in lineinput:
    n = n.translate(str.maketrans('', '', string.digits))
    n = n.translate(str.maketrans('', '', string.punctuation))
    n = n.lower()
    words = n.split()
    for word in words:
        for letter in word:
            counts += 1
            if letter not in dictionary_counts:
                dictionary_counts[letter] = 1
            else:
                dictionary_counts[letter] += 1

for key, val in list(dictionary_counts.items()):
    lst.append((val, key)) 

lst.sort(reverse=True)         

for key, val in lst:
    print(key, val) 