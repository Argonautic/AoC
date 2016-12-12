import re

def triangle_count(triangle_text):
    result = 0
    set_of_three = []
    triangle_list = re.findall('\d+',triangle_text)
    triangle_list = triangle_list[0::3] + triangle_list[1::3] + triangle_list[2::3]
    while triangle_list:
        set_of_three.append(int(triangle_list.pop(0)))
        if len(set_of_three) == 3:
            if is_triangle(set_of_three[0],set_of_three[1],set_of_three[2]):
                result += 1
            set_of_three = []
    return result

def is_triangle(a,b,c):
    if a < b + c and b < a + c and c < a + b:
        return True
    else:
        return False
