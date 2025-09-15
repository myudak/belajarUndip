arr = [10, 7, 8, 5, 1, 6]


def bubbleSort(arr):
    print(f"Array awal: {arr}")
    n = len(arr)
    for i in range(n):
        swapped = False
        print(f"\nIterasi {i + 1}:")
        for j in range(0, n - i - 1):
            print(f"  Membandingkan {arr[j]} dan {arr[j + 1]}")
            if arr[j] > arr[j + 1]:
                print(f"  {arr[j]} > {arr[j + 1]}, tukar posisi")
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
            else:
                print(f"  {arr[j]} <= {arr[j + 1]}, tidak perlu tukar")
        print(f"Array setelah iterasi {i + 1}: {arr}")
        if not swapped:
            print("Tidak ada pertukaran, array sudah terurut.")
            break
    return arr
