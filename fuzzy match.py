actual = 'woomaan'
expected = 'wwoman'

expected_list = list(expected)
actual_list = list(actual)
count = 0
flag = True
i = 0
while i < len(actual_list):
    if expected_list and expected_list[0] == actual_list[i]:
        temp = expected_list.pop(0)
        i +=1
    elif actual_list[i] == temp:
        i +=1
    else:
        flag = False
        break