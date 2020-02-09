#2884번: 알람 시계
H, M = input().split()
if (int(M)-45)<0:
    if(int(H)==0):
        print(23, 60+int(M)-45)
    else:
        print(int(H)-1, 60+int(M)-45)
else:
    print(H, int(M)-45)
