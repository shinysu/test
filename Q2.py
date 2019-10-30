def is_multiples(l):
    return [(((num % 3) == 0) or ((num % 5) == 0)) for num in l]


def is_multiple(n):
    if ((n % 3) == 0) and ((n % 5) == 0):
        return "GraphQL"
    elif (n % 3) == 0:
        return "Graph"
    elif (n % 5) == 0:
        return "QL"


print(is_multiples([1,2,3,4]))
print(is_multiple(3))
print(is_multiple(5))
print(is_multiple(15))