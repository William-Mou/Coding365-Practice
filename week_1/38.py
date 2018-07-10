teacher_name = []
student_name = []

student_dict = {}
teacher_dict = {}

people_num = 0

student_list = []
teacher_list = []

ans = {}

first = input().split(',')
for i in first:
    teacher_name.append(i)
    people_num += 1
student_list = [first]

for i in range(people_num - 1):
    n = input().split(',')
    student_list.append(n)

for j in range(people_num):
    n = input().split(',')
    teacher_list.append(n)

for j in teacher_list[0]:
    student_name.append(j)
student_name = sorted(student_name)
teacher_name = sorted(teacher_name)

j = 0
for i in student_name:
    student_dict[i] = student_list[j]
    j += 1

j = 0
for i in teacher_name:
    teacher_dict[i] = teacher_list[j]
    j += 1


#print(student_dict)
#print(teacher_dict)

# order   = 志願序位 int
# todo    = 待排學生 list
# teacher = 空餘教授 list
def find(order, todo, teacher):
    #print("order",order,"todo",todo,"teacher",teacher,sep = '\n')
    #print("-----------")
    #print(teacher_name)
    order_num = {}
    next_todo = todo
    for stu in todo:
        # stu 學生， 第 order 個志願序
        if student_dict[stu][order] in order_num:
            order_num[student_dict[stu][order]][0] += 1
            order_num[student_dict[stu][order]][1].append(stu)
        else:
            order_num[student_dict[stu][order]] = [1, [stu]]
    
    #print("order_num",order_num,sep = '\n')
    for teach in order_num:
        #print("-----------")
        #print(teacher_name)
        #print(teach,order_num[teach])
        if teach in teacher:
            if order_num[teach][0] == 1:
                    ans[order_num[teach][1][0]] = teach
                    next_todo.remove(order_num[teach][1][0])
                    #print(teach,order_num[teach])
                    #print(teach, teacher)
                    teacher.remove(teach)
                    
            else:
                flag = 0
                for j in teacher_dict[teach]:
                    for k in range(len(order_num[teach][1])):
                        if j == order_num[teach][1][k] :
                            ans[order_num[teach][1][k]] = teach
                            next_todo.remove(order_num[teach][1][k])
                            #print(teach,order_num[teach])
                            #print(j,k,order_num[teach][1][k])
                            #print(teach, teacher)
                            teacher.remove(teach)
                            flag = 1
                            break
                    if flag == 1:
                        break
    if len(next_todo) != 0:
        find(order+1, next_todo, teacher)
    else:
        #print(student_name)
        for student in student_name:
            print(student,ans[student],sep = '->')

find(0, student_name.copy(), teacher_name.copy())
# 100 finish