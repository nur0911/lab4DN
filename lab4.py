# Task 1.1
from collections import defaultdict

user_input = 'Pulp Fiction'
created_list = [char.lower() for char in user_input]
print("Created list is:")
print(created_list)

# Task 1.2
from collections import Counter

symbol_frequency_list = list(Counter(created_list).items())

print("Code Output:")
print(symbol_frequency_list)

# Task 1.3
vowels = 'aeiou'
list_vow = [(char, count) for char, count in symbol_frequency_list if char in vowels]
list_cons = [(char, count) for char, count in symbol_frequency_list if char.isalpha() and char not in vowels]
list_symb = [(char, count) for char, count in symbol_frequency_list if not char.isalpha()]

print("Sample Output:")
print("list_vow =", list_vow)
print("list_cons =", list_cons)
print("list_symb =", list_symb)

# Task 1.4
def divide_list_into_quartiles(input_list):
    sorted_list = sorted(input_list)
    n = len(sorted_list)
    q1 = sorted_list[:n // 4]
    q2 = sorted_list[n // 4:2 * n // 4]
    q3 = sorted_list[2 * n // 4:3 * n // 4]
    q4 = sorted_list[3 * n // 4:]
    return q1, q2, q3, q4

sample_input_1 = [1, 5, 8, 7, 9, 6, 7, 5, 8, 3, 9, 10, 2, 1, 3, 4]
q1, q2, q3, q4 = divide_list_into_quartiles(sample_input_1)

print("Code Output:")
print("q1 =", q1)
print("q2 =", q2)
print("q3 =", q3)
print("q4 =", q4)

# Task 2.1
student_name = 'Adam'
assignment_scores = [82, 56, 44, 30]
test_scores = [78, 77]
lab_scores = [78.2, 77.2]

student = {
    'name': student_name,
    'assignment': assignment_scores,
    'test': test_scores,
    'lab': lab_scores
}

print("Code Output:")
print(student)

# Task 2.2
student_name = 'Adam'

student = {
    'name': student_name,
    'assignment': [82, 56, 44, 30],
    'test': [78, 77],
    'lab': [78.2, 77.2]
}

submission_check = {
    student_name: len(student.get('assignment', [])) == 4 and len(student.get('lab', [])) == 2 and len(student.get('test', [])) == 2
}

print("Sample Output:")
print(submission_check)

# Task 2.3
def calculate_final_grade(student, submission_rate):
    if submission_rate.get(student['name'], 0) >= 4:
        final_grade = 0.3 * sum(student['assignment']) + 0.5 * sum(student['lab']) + 0.2 * sum(student['test'])
        student['final_grade'] = final_grade
    else:
        student['final_grade'] = 0

student = {
    'name': 'Adam',
    'assignment': [82, 56, 44, 30],
    'test': [78, 77],
    'lab': [78.2, 77.2]
}

submission_rate = {'Adam': 6}

calculate_final_grade(student, submission_rate)
print("Sample Output:")
print(student)

# Task 2.4
student = {'name': 'Adam', 'assignment': [82, 56, 44, 30], 'test': [78, 77], 'lab': [78.2, 77.2], 'final_grade': 70.25}
student2 = {'name': 'Kevin', 'assignment': [82, 30], 'test': [], 'lab': [78.2], 'final_grade': 0}

students = {
    'Adam': student,
    'Kevin': student2
}

print("Sample Output:")
print(students)

# Task 3.1 - Register user transactions and store statistics.
from collections import defaultdict

transactions = [(1001, 2), (1001, 1), (1003, 2), (1005, 2), (1001, 3), (1007, 1), (1007, 2), (1100, 2), (1003, 2), (1001, 1)]

stats = defaultdict(lambda: {'mft': None, 'lft': None})
transaction_counts = defaultdict(lambda: defaultdict(int))

for user_id, transaction_type in transactions:
    user_stats = stats[user_id]
    user_transaction_counts = transaction_counts[user_id]

    user_transaction_counts[transaction_type] += 1

    if user_stats['mft'] is None or user_transaction_counts[transaction_type] > user_transaction_counts[user_stats['mft']]:
        user_stats['mft'] = transaction_type
    if user_stats['lft'] is None or user_transaction_counts[transaction_type] < user_transaction_counts[user_stats['lft']]:
        user_stats['lft'] = transaction_type

for user_id, user_stats in stats.items():
    user_stats.update(transaction_counts[user_id])

print("Code Output:")
print(dict(stats))