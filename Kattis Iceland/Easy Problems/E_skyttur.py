input()

s_string = input()
t_string = input()

new_string = ""

for index in range(len(s_string)):
    s_ind = s_string[index]
    t_ind = t_string[index]

    if s_ind == "1" and t_ind == "1":
        new_string += "0"

    elif s_ind == "0" and t_ind == "0":
        new_string += "0"
    
    elif s_ind == "0" and t_ind == "1":
        new_string += "1"
    
    elif s_ind == "1" and t_ind == "0":
        new_string += "1"

print (new_string)
    
    