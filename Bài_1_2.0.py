def cong(a,b):
    phepcong = a + b
    return phepcong
def nhan(a,b):
    phepnhan = a * b
    return phepnhan
while True:
    try:
        x = float(input("Nhập số thứ nhất:"))
        y = float(input("Nhập số thứ hai:"))
        break
    except:
        print("bạn đã nhập sai")
        continue
Q = cong(x,y)
W = nhan(x,y)
print("Kết quả cộng là",Q);
print("Kết quả nhân là",W);