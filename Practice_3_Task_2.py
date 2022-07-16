# Practice_3_Task_2.Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
def FindDuplicates(my_list,listItem):
    counter=my_list.count(listItem)
    return counter

def ListChecking(my_list,target_item):
    lenght=len(my_list)
    counter=0
    for i in range (0,lenght):
        if my_list[i]!=target_item:#если текущий элемент не равен требуемому, то пропускаем цикл, чтобы не тратить время
            continue
        else:
            counter=counter+1#считаем общее кол-во исколого элемента
        if counter==2:
            result=i
    return result,counter

my_str=input("Enter your list. Use the whitespace to separate elements.: ")
target_str=input("Enter the target string: ")
my_list=my_str.split()
print(f"The entered list is {my_list}.\nThe target item is {target_str}.")
if 0<FindDuplicates(my_list,target_str)<2:
    print("The entered list doesn't contain duplicates of the target string!")
elif FindDuplicates(my_list,target_str)==0: 
    print("The entered list doesn't contain the target string! Please check your input.")
else:
    result={}
    result=ListChecking(my_list,target_str)
    print(f"The target string '{target_str}' occurs {result[1]} times in the entered list. \nThe position of the second appearance of the target string is {result[0]}.")
