# tinh diện tích tam giác theo công thức herong
print("Nhập vào độ dài các cạnh của tam giác: ")
a = int(input("Độ dài cạnh a: " ))
b = int(input("Độ dài cạnh b: " ))
c = int(input("Độ dài cạnh c: " ))

p = (a + b+ c)*0.5 
print("nửa chu vi là: ", p)

S = (p*(p-a)*(p-b)*(p-c))**0.5
print("Diện tích tam giác theo công thức là : ",S)