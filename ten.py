lengths = "227,169,3,166,246,201,0,47,1,255,2,254,96,3,97,144"
chain = list(range(256))

inn = "27,169,3,166,246,201,0,47,1,255,2,254,96,3,97,144"

#lengths = "3,4,1,5"
#chain = list(range(5))

# ll = [0, 1, 2, 3]
## index = 2
## length = 3
## index + length = 5, len(ll) == 4
def reverse(chain, index, length):
    result = chain.copy()
    chain.extend(chain)
    mods = 0
    while mods < length:
        dest_index = (index + mods) % len(result)
        result[dest_index] = chain[index + length - 1 - mods]
        mods += 1
    return result

skip = 0
index = 0

lengths = [int(n) for n in lengths.split(",")]
for length in lengths:
    print(index, length, skip)
    print(chain)
    chain = reverse(chain, index, length)
    index = (index + length + skip) % len(chain)
    skip += 1
print(chain[0] * chain[1])
