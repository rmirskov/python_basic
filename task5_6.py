import re

educ_subjects = {}
with open('data5_6.txt', 'r') as f:
    for line in f:
        subject = re.match(r'[а-яА-Я ]+(?=:)', line)
        number_of_classes = sum([int(elem) for elem in re.findall(r'\d+', line)])
        if subject.group() in educ_subjects.keys():
            educ_subjects[subject.group()] += number_of_classes
        else:
            educ_subjects[subject.group()] = number_of_classes
print(educ_subjects)
