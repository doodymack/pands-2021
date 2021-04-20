# histograms.py
# basic histograms in python
# author: PaulMcGrath
#https://realpython.com/lessons/pure-python-histograms/

a = [0,1,1,1,2,3,7,7,23]


def count_elements(seq) -> dict:
    hist = {}
    for i in seq:
        hist[i] = hist.get(i, 0) + 1
    return hist

counted = count_elements(a)
print (counted)