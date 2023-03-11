class Solution:

# optimized solution
    def addBinary2(self, a: str, b: str) -> str:
        return format(int(a, base=2) + int(b, base=2), 'b')   
 
 
    def addBinary(self, a: str, b: str) -> str:
        if len(a) != len(b):
            z = abs(len(a)-len(b))
            if len(a)>len(b):
                l = '0'*z
                b = l+b
            elif len(a)<len(b):
                l = '0'*z
                a = l+a
        a = a[::-1]
        b = b[::-1]
        # print(a,b)
        carry = 0
        add = 0
        arr = []
        for i in range(len(a)):
            x = a[i]
            # p,q = int(a,b)
            y = b[i]
            x = int(x)
            y = int(y)
            if (x, y,carry)== (0,0,0):
                add,carry = (0,0)
                arr.append(add)
                # break
            elif (x, y,carry)== (0,0,1):
                (add,carry) =(1,0)
                arr.append(add)
            elif (x, y,carry)== (1,1,1):
                add,carry = (1,1)
                arr.append(add)
                # break
            elif ((x, y,carry)== (1,1,0)) or (x != y and carry == 1):
                (add, carry) = (0,1)
                arr.append(add)
                # break
            # elif x != y and carry == 1:
            #     (add, carry) = (0,1)
            elif x != y and carry == 0:
                (add, carry) = (1,0)
                arr.append(add)
                # break
        if carry == 1:
            arr.append(carry)
        out = ""
        # for i in range (len(arr)):
        #     out += str(arr[i])
        for i in arr:
            out += str(i)

        return out[::-1]

    
if __name__ == '__main__':
    a = "11"
    b = "1"
    print(Solution().addBinary(a,b))
    print(Solution().addBinary2(a,b))


    