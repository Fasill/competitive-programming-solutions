
def f(left,right):
    ans = []
    for i in range(left,right+1):
        if len(str(i)) ==1:
            ans.append(i)

        else:
            b = False
            for j in range(len(str(i))):

                if  int(str(i)[j]) == 0 or i%int(str(i)[j]) != 0:
                    b = True
            if b == False:
                ans.append(i)
    return ans

print(f(1,22))