#1330번: 두 수 비교하기
a, b = input().split()
if int(a)>int(b):
	print(">")
elif int(a)<int(b):
	print("<")
else:
	print("==")
