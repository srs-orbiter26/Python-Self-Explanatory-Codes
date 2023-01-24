course = "Python's for Beginners"
print(course)

print(course[2])  # Index from start
print(course[-2])  # Index from end
print(course[2:5])  # Starting from 2 and ending before 5
print(course[2:])
print(course[:5])
print(course[:])
print(course[2:-2])
another = course[:]
print(another)

course1 = '''
Hi Soumya,
Welcome
'''
print(course1)

first = 'Soumya'
last = 'Ranjan'
message = first + ' [' + last + '] is a coder.'
msg = f'{first} [{last}] is a coder.'  # Formatted string, {}->These are called place holder
print(msg)
print(message)
