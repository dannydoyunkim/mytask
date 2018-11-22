s1 = " Hello LGCNS "
s2 = "010 8790 1234"
s3 = "010--8769"
s4 = "010-5793-8769"

print("s1 = ", s1)
splitList1 = s1.split()
print("s1.split() = ", splitList1)

print("\ns2 = ", s2)
splitList2 = s2.rsplit()
print("s2.rsplit() = ", splitList2)

print("\ns3 = ", s3)
splitList3 = s3.split('-')
print("s3.split('-') = ", splitList3)

print("\ns3 = ", s4)
splitList4 = s4.split('-')
print("s4.split('-') = ", splitList4)






