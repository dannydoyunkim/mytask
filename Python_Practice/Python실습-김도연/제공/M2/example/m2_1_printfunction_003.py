#m2_printfunction_003.py

#다양한 option을 정수 형에 적용한 예
print(" 1 :{0:7d}".format(12))
print(" 2 :{0:#x}".format(12))
print(" 3 :{0:#o}".format(12))
print(" 4 :{0:+7d}".format(12))
print(" 5 :{0:+7d}".format(-12))
print(" 6 :{0:<7d}".format(12))
print(" 7 :{0:>7d}".format(12))
print(" 8 :{0:+7d}".format(12))
print(" 9 :{0:+7d}".format(-12))
print(" 8 :{0:-7d}".format(12))
print(" 9 :{0:-7d}".format(-12))
print("10 :{0:^7d}".format(12))
print("11 :{0: d}".format(12))
print("12 :{0: d}".format(-12))
print("13 :{0:,d}".format(1234500))
print("14 :{0:0=10d}".format(15))
print("15 :{0:0=10d}".format(-15))
print("16 :{0:@=10d}".format(15))
print("17 :{0:@=10d}".format(-15))

#다양한 option을 실수 형에 적용한 예
print("18 :{0:,.2f}".format(12345.12))
print("19 :{0:-7.2f}".format(1.2))
print("20 :{0:-7.2f}".format(-1.2))
print("21 :{0:+7.2f}".format(1.2))
print("22 :{0:+7.2f}".format(-1.2))
print("23 :{0: 7.2f}".format(1.2))
print("24 :{0: 7.2f}".format(-1.2))
print("25 :{0:^15.2f}".format(1.2))
print("26 :{0:,.2f}".format(1234500.12))
print("27 :{0:0=10.2f}".format(1.2))
print("28 :{0:0=10.2f}".format(-1.2))
print("29 :{0:@=10.2f}".format(1.2))
print("30 :{0:@=10.2f}".format(-1.2))

