# Source kata:
# https://www.codewars.com/kata/5667e8f4e3f572a8f2000039?utm_source=newsletter

def accum(s):
    # i = 0
    # for c in input:
    #     sections.append(c.upper() + c.lower() * (i-1))
    #     i += 1
    # return '-'.join(sections)

    # return '-'.join([c.upper() + c.lower()*i for i, c in enumerate(s)])
    return '-'.join([(c * (i + 1)).title() for i, c in enumerate(s)])


print(accum('abcd'))
print(accum("RqaEzty"))
print(accum("cwAt"))
print(accum('A'))
print(accum(''))
