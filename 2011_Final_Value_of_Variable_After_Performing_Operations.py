class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for i in range(len(operations)):
            a = operations[i]
            if a == "--X" or a == "X--":
                x -= 1
            elif a == "++X" or a == "X++":
                x += 1
        return x
            

if __name__ == '__main__':
    operations = ["--X","X++","X++"]
    print(Solution().finalValueAfterOperations(operations))