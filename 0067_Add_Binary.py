class Solution:

# optimized solution
    def addBinary2(self, a: str, b: str) -> str:
        return format(int(a, base=2) + int(b, base=2), 'b')   
 
    def addBinary_1(self, a: str, b: str) -> str:
        decimal_number = int(a,2) + int(b,2)
        return f"{decimal_number:b}"
    
    def addBinary_2(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]
    
    def addBinary1_1(self, a: str, b: str) -> str:
        pos_a = len(a) - 1
        pos_b = len(b) - 1
        carry = 0
        ret = []
        while pos_a >= 0 or pos_b >= 0:
            a_val = int(a[pos_a]) if pos_a >= 0 else 0
            b_val = int(b[pos_b]) if pos_b >= 0 else 0
            sum_val = a_val + b_val + carry
            carry = sum_val // 2
            ret = [str(sum_val % 2)] + ret
            pos_a -= 1
            pos_b -= 1
        if carry > 0:
            ret = ['1'] + ret
        return ''.join(ret)

    def addBinary2_1(self, a: str, b: str) -> str:
        len_a = len(a)
        len_b = len(b)
        max_len = max(len_a, len_b)
        a = a.zfill(max_len)
        b = b.zfill(max_len)
        carry = 0
        ret = []
        for i in range(max_len - 1, -1, -1):
            if a[i] == '1':
                carry += 1
            if b[i] == '1':
                carry += 1
            if carry % 2 == 1:
                ret.append('1')
            else:
                ret.append('0')
            carry //= 2
        if carry > 0:
            ret.append('1')
        ret.reverse()
        return ''.join(ret)
    
    def addBinary3_1(self, a: str, b: str) -> str:
        x, y = int(a, 2), int(b, 2)
        while y:
            x, y = x ^ y, (x & y) << 1
        return bin(x)[2:]
    
    def addBinary(self, a: str, b: str) -> str:
        # checking len of two given binary n balancing len by adding zeros
        if len(a) != len(b):
            z = abs(len(a)-len(b))
            if len(a)>len(b):
                l = '0'*z
                b = l+b
            elif len(a)<len(b):
                l = '0'*z
                a = l+a
        # reverse the string to add the each digit of the binary
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
            # validating carry from the addition
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


    