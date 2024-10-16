# NO 1
nilai = int(input('masukan nilai :'))
if nilai >= 90:
    print('Excellent Performance')
elif nilai >= 80:
    print('Very Good Performance')
elif nilai >= 70:
    print('Good Performance')
elif nilai >= 60:
    print('Average Performance')



# NO 2
a = float(input('Masukan angka pertama :'))
b = float(input('Masukan angka Kedua :'))
c = float(input('Masukan angka ketiga :'))

terbesar = max(a,b,c)
print('angka terbesar adalah', terbesar)


#NO 3
def fib(n):
    a, b = 0, 1
    for n in range(n):
        print(a, end=' ')
        a, b = b, a + b

n = int(input('masukan angka fibonacci :'))
print("Fibonacci :")
fib(n)


# NO 4
ganjil = int(input('masukan nilai n untuk bilangan ganjil :'))
for i in range (1, ganjil + 1, 2):
    print (i, end= " ")


# NO 5
segit = int(input('masukan nilai n untuk segitiga :'))
for i in range(1, segit+1):
    for j in range(i):
        print (i, end=" ")
    print()