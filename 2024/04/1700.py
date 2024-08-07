# 1700. Number of Students Unable to Eat Lunch
# Easy
# The school cafeteria offers circular and square sandwiches at lunch break, referred to by numbers 0 and 1 respectively. All students stand in a queue. Each student either prefers square or circular sandwiches.
# The number of sandwiches in the cafeteria is equal to the number of students. The sandwiches are placed in a stack. At each step:
# If the student at the front of the queue prefers the sandwich on the top of the stack, they will take it and leave the queue.
# Otherwise, they will leave it and go to the queue's end.
# This continues until none of the queue students want to take the top sandwich and are thus unable to eat.
# You are given two integer arrays students and sandwiches where sandwiches[i] is the type of the i​​​​​​th sandwich in the stack (i = 0 is the top of the stack) and students[j] is the preference of the j​​​​​​th student in the initial queue (j = 0 is the front of the queue). Return the number of students that are unable to eat.


from collections import deque
from collections import Counter


def countStudents(students, sandwiches):
    students_deque = deque(students)
    sandwiches_deque = deque(sandwiches)

    i = 0
    while (students_deque or sandwiches_deque) and i < len(students_deque):
        if students_deque[0] == sandwiches_deque[0]:
            students_deque.popleft()
            sandwiches_deque.popleft()
            i = 0
        else:
            students_deque.append(students_deque.popleft())
            i += 1
    return len(students_deque)


# Example 1:
students = [1, 1, 0, 0]
sandwiches = [0, 1, 0, 1]
ans = 0
print("Pass" if countStudents(students, sandwiches) == ans else "Fail")
# Explanation:
# - Front student leaves the top sandwich and returns to the end of the line making students = [1,0,0,1].
# - Front student leaves the top sandwich and returns to the end of the line making students = [0,0,1,1].
# - Front student takes the top sandwich and leaves the line making students = [0,1,1] and sandwiches = [1,0,1].
# - Front student leaves the top sandwich and returns to the end of the line making students = [1,1,0].
# - Front student takes the top sandwich and leaves the line making students = [1,0] and sandwiches = [0,1].
# - Front student leaves the top sandwich and returns to the end of the line making students = [0,1].
# - Front student takes the top sandwich and leaves the line making students = [1] and sandwiches = [1].
# - Front student takes the top sandwich and leaves the line making students = [] and sandwiches = [].
# Hence all students are able to eat.
# Example 2:
students = [1, 1, 1, 0, 0, 1]
sandwiches = [1, 0, 0, 0, 1, 1]
ans = 3
print("Pass" if countStudents(students, sandwiches) == ans else "Fail")
# Constraints:
# 1 <= students.length, sandwiches.length <= 100
# students.length == sandwiches.length
# sandwiches[i] is 0 or 1.
# students[i] is 0 or 1.


def countStudents(students, sandwiches):
    students_count = Counter(students)

    res = len(students)
    for s in sandwiches:
        if students_count[s] > 0:
            students_count[s] -= 1
            res -= 1
        else:
            break
    print(res)
    return res


# Example 1:
students = [1, 1, 0, 0]
sandwiches = [0, 1, 0, 1]
ans = 0
print("Pass" if countStudents(students, sandwiches) == ans else "Fail")
# Example 2:
students = [1, 1, 1, 0, 0, 1]
sandwiches = [1, 0, 0, 0, 1, 1]
ans = 3
print("Pass" if countStudents(students, sandwiches) == ans else "Fail")


def countStudents(students, sandwiches):
    N = len(sandwiches)

    z = students.count(0)
    o = students.count(1)

    for i, s in enumerate(sandwiches):
        if s == 1 and o > 0:
            o -= 1
        elif s == 0 and z > 0:
            z -= 1
        else:
            return N - i

    return 0


# Example 1:
students = [1, 1, 0, 0]
sandwiches = [0, 1, 0, 1]
ans = 0
print("Pass" if countStudents(students, sandwiches) == ans else "Fail")
# Example 2:
students = [1, 1, 1, 0, 0, 1]
sandwiches = [1, 0, 0, 0, 1, 1]
ans = 3
print("Pass" if countStudents(students, sandwiches) == ans else "Fail")
