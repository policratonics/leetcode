from collections import deque
from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # count_circular = students.count(0)
        # count_square = students.count(1)
        # for sandwich in sandwiches:
        #     if sandwich == 0:
        #         if count_circular > 0:
        #             count_circular -= 1
        #         else:
        #             break
        #     else:
        #         if count_square > 0:
        #             count_square -= 1
        #         else:
        #             break
        # return count_square + count_circular

        q_students = deque()
        q_sandwiches = deque()
        for i in students:
            q_students.append(i)
        for i in sandwiches:
            q_sandwiches.append(i)
        while q_students:
            rotation = 0
            while rotation < len(q_students):
                if  q_students[0] == q_sandwiches[0]:
                    q_students.popleft()
                    q_sandwiches.popleft()
                    # rotation = 0
                    break
                else:
                    student = q_students.popleft()
                    q_students.append(student)
                    rotation += 1
            if rotation == len(q_students):
                break
        return len(q_students)


if __name__ == '__main__':
    t = Solution().countStudents(students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1])
    print(t)