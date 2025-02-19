s = print("xin nhap chuoi ki tu bat ki:")
print(type(s))
print("chuoi ki. tu vua nhapla :",s)

a=float(input("nhap 1 so thuc:"))
print(type(a))
print(a)

a =int(input("nhap chieu rong:"))
b = int(input("nhap chieu dai:"))
chuvi= 2*(a+b)
dientich =  a*b
print(chuvi,dientich)

#B1:nhap
s=input("nhap 3 so:")
#B2: tach 2 so ra
a= s.split()
print(a)
#B3:  su  dung ham map  de ep cac phan tu  trong list
x , y , z = map(int, a)

        