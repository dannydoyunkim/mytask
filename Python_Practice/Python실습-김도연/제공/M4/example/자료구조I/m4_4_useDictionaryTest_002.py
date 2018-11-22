students = {}

students["Name"] = "홍길동"
students["SID"] = "s100"
students["C"] = 90
students["Python"] = 80
students["Java"] = 99

print("[Name] :%s [SID] :%s [C] :%d [Python] :%d [Java] :%d" % 
              (students["Name"], students["SID"],students["C"],
               students["Python"], students["Java"]))

students["Total"] = students["C"]+students["Python"]+students["Java"]


print("[Name] :%s [SID] :%s [C] :%d [Python] :%d [Java] :%d [Total] :%d" % 
              (students["Name"], students["SID"],students["C"],
               students["Python"], students["Java"], students["Total"]))

print("{}님의 총점은 {}입니다.".format(students["Name"], students["Total"]))
