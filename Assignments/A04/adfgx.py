import pprint as pp
import sys
from build_polybius import AdfgxLookup

#     A D F G X
# A | p h q g m 
# D | e a y n o 
# F | f d x k r
# G | c v s z w 
# X | b u t i l

# init and input my keyword
A = AdfgxLookup('superbad')

# build my lookup table 
lookup = A.build_polybius_lookup()

# print out my adfgx lookup table
pp.pprint(lookup)

# print out the actual matrix so I 
# know I'm not insane!
A.sanity_check()

for i in "discombobulate":
    print(lookup[i],end=" ")

B = AdfgxLookup('helloworldhowareyou')

# build my lookup table 
lookup = B.build_polybius_lookup()

# print out my adfgx lookup table
pp.pprint(lookup)

# print out the actual matrix I 
# know I'm not insane!
B.sanity_check()

message = "theattackisatdawn"
for x in message:
    print(lookup[x],end=' ')


print("")
