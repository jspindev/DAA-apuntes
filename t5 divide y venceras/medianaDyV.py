from random import randint


def median(elements):
    med = len(elements)//2

    return kthSmallestElement(med,elements)

def kthSmallestElement(k,elements):
    mid = len(elements) // 2
    pivot = elements[mid]

    low = [x for x in elements if x < pivot]
    if k < len(low):
        return kthSmallestElement(k,low)
    k -= len(low)
    equal = [x for x in elements if x == pivot]
    if k < len(equal):
        return pivot

    k -= len(equal)
    high = [x for x in elements if x > pivot]
    return  kthSmallestElement(k,high)


def test():
    print("Testing ..", end = "")
    for i in range(200):
        n = randint(1,10)
        a = [randint(0,99) for i in range(n)]
        print(a)
        copy = a[:]
        copy.sort()
        #print("sorted: ", copy)

        m = median(a)
        expected = copy[(len(copy)) // 2]
        assert m == expected
        print("Done")


test()