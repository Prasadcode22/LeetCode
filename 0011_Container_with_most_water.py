class Solution:
    def maxArea(self, height):
        len_ = len(height)
        # max_height, max_width = 0, 0
    # for i in range(len_):
        water_container = []
        # for i in reversed(range(len_)):
        #     max_height = height[i]
        #     max_width = i-1
        #     max_volume = max_height*max_width
        #     print(max_volume)
        for i in range(len_):
            for j in reversed(range(len_)):
                height_ = min(height[i],height[j])
                print(j)
                width_ = (j)
                # print(height_*width_)

class Solution:
    def maxArea2(self, height):
        #initalize walls and starting max
        leftWall = 0
        rightWall = len(height)-1
        currMax = 0
        
        while leftWall<rightWall:

            #calculate local volume
            localVolume =  min(height[leftWall],height[rightWall]) * (rightWall - leftWall)
            
            #compare
            if localVolume > currMax:
                currMax = localVolume

            #shirnk the walls as nessassary
            if height[rightWall] > height[leftWall]:
                leftWall +=1
            else:
                rightWall -=1

        return currMax           
            
                
if __name__ == '__main__':
    num = [1,7,6,2,5,4,8,3,8]
    print(Solution().maxArea2(num))                     
