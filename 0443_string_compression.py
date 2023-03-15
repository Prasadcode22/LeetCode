
class Solution:
    def compress(chars):
        chars.sort()
        out = []
        for i in chars:
            p = chars.count(i)
            if i not in out:
                if p == 1:
                    out.append(i)
                elif p > 9 :
                    a = p // 10
                    b = p%10
                    out.append(i)
                    out.append(str(a))
                    if b > 0:
                        out.append(str(b))
                else:
                    out.append(i)
                    out.append(str(p))
        return len(out),out

if __name__ == '__main__':
    # chars =["a","a","b","b","c","c","c"]
    # chars =["a","a","b","b","b","b","b","b","b","b","b","b","b","b","c","c","c"]
    # chars = ['a']
    print(Solution.compress(chars))

# class Solution:
#     def compress(chars):
#         out = []
#         n = 0
#         for i in chars:
#             if i not in out:
#                 out.append(i)
#                 n += 1
#             for i in out:
#                 n += 1
               

#         return(len(out), out)

# class Solution:
#     def compress(chars):
#         out = []
#         n = 0
#         for i in chars:
#             if i not in out:
#                 out.append(i)
#                 n += 1
#             for i in out:
#                 n += 1
               

#         return(len(out), out)


# def compress(chars):
# chars.sort()
# out = []
# for i in chars:
#     p = chars.count(i)
#     if i not in out:
#         if p > 9 :
#             a = p // 9
#             b = p%9
#             for j in range(a):
#                 out.append(i)
#                 out.append('9')
#             out.append(i)
#             out.append(str(b))
#         else:
#             out.append(i)
#             out.append(str(p))
# return len(out),out


# class Solution:
#     def compress(self, chars: List[str]) -> int:
#         chars.sort()
#         out = []
#         for i in chars:
#             p = chars.count(i)
#             if i not in out:
#                 if p > 9 :
#                     a = p // 9
#                     b = p%9
#                     for j in range(a):
#                         out.append(i)
#                         out.append('9')
#                     out.append(i)
#                     out.append(str(b))
#                 else:
#                     out.append(i)
#                     out.append(str(p))
#         print(out)


# if __name__ == '_main__':
#     char