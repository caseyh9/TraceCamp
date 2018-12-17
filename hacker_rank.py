# Hacker Rank exercises

#1
#!/bin/python
# Given
N = int(raw_input())
# Written
if (N % 2 == 0) and ((N >= 2 and N <= 5) or (N > 20)):
    print("Not Weird")
else:
    print("Weird")

#2
# Given
if __name__ == '__main__':
    n = int(raw_input())
# Written
num = 0
while (num < n):
    print(num**2)
    num += 1

#3
# Given
if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
# Written
avg = 0
for i in student_marks[query_name]:
    avg += i
avg = '{0:.2f}'.format(avg / 3)
print(avg)
