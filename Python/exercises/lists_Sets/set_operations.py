'''
 Program to perform different set operations like in mathematics
 union,intersection,difference,symmetric difference
# define three sets
    E = {0, 2, 4, 6, 8};
    N = {1, 2, 3, 4, 5};
'''


E = {0, 2, 4, 6, 8}
N = {1, 2, 3, 4, 5}

# performing union : i.e. sum of both
print(E.union(N)) #shorthand --> |

# performing intersection : i.e. common in both
print(E.intersection(N)) #shorthand --> &

# performing difference : i.e. 1st - 2nd
print(E.difference(N)) # shorthand --> -

# symmetric difference : i.e. ele except which are common in both
print(E.symmetric_difference(N)) #shorthand --> ^

 