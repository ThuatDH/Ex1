_noProblem = int(input())
Implement = 0
i = 0
while i < _noProblem:
    s= str(input())
    if s.count('1') >= 2:
        Implement += 1
        i += 1
    else:
        i +=1
print(Implement)

