from os import system

n = int(input("Nhap so phan tu: "))
arr = []

def bubbleSort(arr):
    count = 0

    for i in range(n):
        count += 1
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

        print(f"Vong lap {count}: {arr}")

for i in range(n):
    arr.append(int(input(f"Nhap phan tu thu {i+1}: ")))

system("cls")
print(f"Truoc khi sort: {arr}\n")
bubbleSort(arr)
print(f"\nKet qua: {arr}")