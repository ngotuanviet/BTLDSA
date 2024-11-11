from os import system

n = int(input("Nhap so phan tu: "))
arr = []

def insertionSort(arr):
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print(f"Vong lap {i}: {arr}")

for i in range(n):
    arr.append(int(input(f"Nhap phan tu thu {i + 1}: ")))

system("cls")
print("ket qua cua InsertionsSort \n")
print(f"Truoc khi sort: {arr}\n")
insertionSort(arr)
print(f"\nKet qua: {arr}")