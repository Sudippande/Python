# import pyttsx3
# engine = pyttsx3.init()
# # Convert text to speech
# engine.say("Hello, how are you?")
# engine.runAndWait()  # Wait until the speech is finished
# engine.say("hi I am fine and You !")
# engine.runAndWait()
# engine.say("is your name sudip !")
# engine.runAndWait()

# nums = [2, 7, 11, 15]
# target = 18
# print(len(nums))

# for i in range(len(nums)):  # Loop through each element
#     for j in range(i + 1, len(nums)):  # Loop through the remaining elements
#         if nums[i] + nums[j] == target:  # Check if their sum is equal to target
#             print(i, j)  # Print indices


class Solution(object):
    def twoSum(self, nums, target):
        n=len(nums)
        for i in range(n-1):
            for j in range(i+1,n):
                if(nums[i]+nums[j])==target:
                    return[i,j]
            
ne=Solution()
result=ne.twoSum([3,2,4],6)
print(result)
       