from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # n = len(temperatures)  # Get the number of days
        # result = [0] * n  # Initialize the result array with zeros
        # stack = []  # Monotonic decreasing stack (stores indices)
        #
        # for current_day in range(n):  # Iterate through each day
        #     # Check if the current temperature is warmer than the last stored temperature
        #     while stack and temperatures[current_day] > temperatures[stack[-1]]:
        #         previous_day = stack.pop()  # Get the last day index from the stack
        #         result[previous_day] = current_day - previous_day  # Calculate days until warmer day
        #     stack.append(current_day)  # Push the current day onto the stack
        #
        # return result
                n = len(temperatures)
                ans = [0] * n
                stack = []

                for current_day in range(n):
                    current_temp = temperatures[current_day]
                    while stack and temperatures[stack[-1]] < current_temp:
                        prev_day = stack.pop()
                        ans[prev_day] = current_day - prev_day
                    stack.append(current_day)

                return ans

if __name__ == '__main__':
    t = Solution().dailyTemperatures(temperatures = [73,74,75,71,69,72,76,73])
    print(t)