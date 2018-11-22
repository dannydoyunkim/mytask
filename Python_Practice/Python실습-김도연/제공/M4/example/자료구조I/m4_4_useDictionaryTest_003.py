students = {}

students["Name"] = "홍길동"
students["SID"] = "s100"
students["C"] = 90
students["Python"] = 80
students["Java"] = 99

for key in students.keys(): 
    print("{:<6s} : {:<5}".format(key, students[key]))

if "Total" not in students:
    students["Total"] = students["C"]+students["Python"]+students["Java"]

print("{}님의 평균은 {}입니다.".format(students["Name"], students["Total"]))

if "Python" in students:
    students["Python"] += 5

for key in students.keys(): 
    print("{:<6s} : {:<5}".format(key, students[key]))

# students.pop("Total") # Total이 삭제되어서 error남
# print("{}님의 총점은 {}입니다.".format(students["Name"], students["Total"]))

# 추가로 리스트화 하기
student1= {}
student1["Name"] = "홍길동"
student1["SID"] = "s100"
student1["C"] = 90
student1["Python"] = 80
student1["Java"] = 99

student2= {}
student2["Name"]="김유신"
student2["SID"]="s310"
student2["C"]=90
student2["Python"]=80
student2["Java"]=99

student3 = {"Name":"김유신","SID":"s310","C":90,"Python":80,"Java":99}

school = [ student1, student2, student3 ]

print(school)

school1 = [{"Name":"홍길동","SID":"s310","C":90,"Python":80,"Java":99},
            {"Name":"김유신","SID":"s310","C":90,"Python":80,"Java":99},
            {"Name":"길동이","SID":"s310","C":90,"Python":80,"Java":99}]

print(school1)

for i in range(len(school)) :
    for key in school[i].keys() :
        print("[{}]:{}".format(key,school[i].get(key)),end=" ")
    print("")


# 정답###
for stu in school1 :
    for key in stu.keys() :
        print("[{}]:{}".format(key,stu[key]),end=" ")
    print("")