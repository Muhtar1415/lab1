import re
with open("row.txt") as f:
    s = f.read()

#task1
mathches=re.findall(r"a.*b", s)
print(mathches)

#task2
mathches=re.findall("abb+|abbb+", s)
print(mathches)

#task3
mathches=re.findall(r"[a-z]+_[a-z]+", s)
print(mathches)

#task4
mathches=re.findall(r"[A-Z]+[a-z]+", s)
print(mathches)

#task5
mathches=re.findall(r"a.*b$", s)
print(mathches)

#task6
mathches=re.sub(r"\s",":", s)
print(mathches)

#task7
def snake_to_camel(snake_case):
    return re.sub(r'_([a-z])', lambda x: x.group(1).upper(), snake_case)

snake = "how_are_you"
camel_case = snake_to_camel(snake)

print(f"Camel case: {camel_case}")

#task8
def split_at_uppercase(input_string):
    result = re.findall('[A-Z][^A-Z]*', input_string)
    return result

#task9
def capital_letters(input_string):
    res = re.sub(r'([a-z])([A-Z])', r'\1 \2', input_string)
    return res

#task10
def camel_to_snake(camel_case):
    res = re.sub(r'([a-z])([A-Z])', r'\1_\2', camel_case)
    return res.lower()

camel = "howareyou"
snake_case = camel_to_snake(camel)

print(f"Camel case: {snake_case}")