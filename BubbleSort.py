from os import system

n = int(input("Nhap so phan tu: "))
arr = []

def bubbleSort(arr):
    for i in range(n):
        print(f"Vong lap {i + 1}: {arr}")
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

for i in range(n):
    arr.append(int(input(f"Nhap phan tu thu {i + 1}: ")))

system("cls")
print(f"Truoc khi sort: {arr}\n")
bubbleSort(arr)
print(f"\nKet qua: {arr}")