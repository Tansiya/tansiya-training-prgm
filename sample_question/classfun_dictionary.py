import json
class task():
    def inp_check(s):
        if s[-1]==',' and s[0]==',':
            print("yes both")
            list = s.split(',')[:-1][:0]
            new_list=[]
            for num in list:
                new_list.append(int(num))
            return new_list
        elif s[-1]==',':
            print("yes after")
            list = s.split(',')[:-1]
            new_list=[]
            for num in list:
                new_list.append(int(num))
            return new_list
        elif s[0]==',':
            print("yes before")
            list = s.split(',')[:0]
            new_list=[]
            for num in list:
                new_list.append(int(num))
            return new_list
        else:
            list = s.split(',')
            new_list=[]
            for num in list:
                new_list.append(int(num))
            return new_list

    
    def odd_even(list):
        out = {}
        even_list = []
        odd_list  = []
        for num in list:
            if num%2==0:
                even_list.append(num)

            else:
                odd_list.append(num)
        out["even_num"] = even_list
        out["odd_num"]  = odd_list

        return out


    def sum_of_list(list):
        sum = 0
        for num in list:
            sum = sum + num

        return sum

    def find_digits(list):
        dict_digits = {}
        list_dig_1 =[]
        list_dig_2 =[]
        list_dig_3 =[]
        list_dig_4 =[]
        list_dig_5 =[]
        list_dig_more_5 =[]
        for num in list:
            if len(str(num)) == 1:
                list_dig_1.append(num)
            elif len(str(num)) == 2:
                list_dig_2.append(num)
            elif len(str(num)) == 3:
                list_dig_3.append(num)
            elif len(str(num)) == 4:
                list_dig_4.append(num)
            elif len(str(num)) == 5:
                list_dig_5.append(num)
            else:
                list_dig_more_5.append(num)

        dict_digits["one_digit"] = list_dig_1
        dict_digits["two_digit"] = list_dig_2
        dict_digits["three_digit"] = list_dig_3
        dict_digits["four_digit"] = list_dig_4
        dict_digits["five_digit"] = list_dig_5
        dict_digits["five_more_digit"] = list_dig_more_5

        return dict_digits

    def div_7(list):
        store={}
        sum_list=[]
        for num in list:
            if num%7 == 0:
                sum_list.append(num)

        store["div_7"] = sum_list
        store["sum_div_7"] = task.sum_of_list(sum_list)
        return store

    def center_values(list):
        center_list = []
        f_len=len(list) % 2
        if f_len == 0:
            disha = int(len(list)/2)
            center = disha-1
            center.two = disha
            center_list.append(list[center])
            center_list.append(list[center.two])
        else:
            save = int(len(list)/2)
            center_list.append(list[save])

        return center_list


print("enter numbers with comma (,) separated")
s = input()
list = task.inp_check(s)
result = {}
oddeven = task.odd_even(list)
result["total_items"] = len(list)
result["center_item"] = task.center_values(list)
result["total_sum"]   = task.sum_of_list(list)
result["even"]  = oddeven["even_num"]
result["odd"]   = oddeven["odd_num"]
result["biggest"]  = max(list)
result["smallest"] = min(list)
result["asending"] = sorted(list, key=int)
result["desending"] = sorted(list, key=int, reverse=True)
digit = task.find_digits(list)
result["1_digits"] = digit["one_digit"]
result["2_digits"] = digit["two_digit"]
result["3_digits"] = digit["three_digit"]
result["4_digits"] = digit["four_digit"]
result["5_digits"] = digit["five_digit"]
result["5_more_digits"] = digit["five_more_digit"]
sss = task.div_7(list)
result["divisible_7"] = sss["div_7"]
result["sum_divisible_7"] = sss["sum_div_7"]

with open('divi.json', 'w')as task:

    json.dump(result,task)


print(result)







    



