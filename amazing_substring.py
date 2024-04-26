
def amazing_ss(s):
    v = ['a','e','i','o','u']
    l = len(s)
    count = 0
    for i in range(l):
        for j in range(i+1,l+1):
            substring = s[i:j]
            print(f"outsid loop:  {substring}")
            if substring[0] in v:
                print(substring)
                count +=1
    return count



s = 'abrab'

print(amazing_ss(s))
