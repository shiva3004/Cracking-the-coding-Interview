result = []


def getPerms(str, prefix):
    """
    Takes a string and returns the all the permutations of n-1 character sub strings.
    :param str: 
    :param prefix:
    :return:
    """
    if len(str) == 0:
        result.append(prefix)
    for i in range(len(str)):
        rem = str[0:i] + str[i+1:]
        getPerms(rem, prefix+str[i])

print(result)
getPerms('1234','')
for p in result:
    print(p)
