import random
from collections import defaultdict
5
tokens = ["I", "try", "to", "learn", "something", "new", "every", "day"]

graph = defaultdict(list)

print (graph)
graph["word"].append("hello")
print (graph["word"])  
for i,token in enumerate(tokens):
    print (i,token)
for i in range(5):
    print(random.choice(tokens))