# 인사부서 : 'hong', 'kim', 'lee', 'ko'
# 경리부서 : 'seo','choi','hong','park','shin'
# 재무부서 : 'yun','kim','na','park'

# 이 경우 아래와 같이 Dictionary로 구성 가능

company = {"인사부서" : ['hong', 'kim', 'lee', 'ko' ],
            "경리부서" : ['seo','choi','hong','park','shin' ],
            "재무부서" : ['yun','kim','na','park' ]
        }

for dept in company.keys() :
    print(company.get(dept))

#다시 꺼내서 출력하기
for dept in company.keys() :
    employee_names = company.get(dept)
    print("{}의 사원 :".format(dept),end=" ")

    for j in employee_names :
        print(j,end=" ")

    print(" ")
        
