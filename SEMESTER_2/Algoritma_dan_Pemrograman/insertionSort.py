arr = [10, 7, 8, 5, 1, 6]


def insertionSort(arr):
    print(f"Array awal: {arr}")
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1
        print(f"\nMenyisipkan {temp} pada indeks {i}")

        # Geser elemen yang lebih besar dari temp ke kanan
        while j >= 0 and arr[j] > temp:
            print(f"  {arr[j]} > {temp}, geser {arr[j]} ke indeks {j + 1}")
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = temp
        print(f"{temp} ditempatkan pada indeks {j + 1}")
        print(f"Array setelah menyisipkan {temp}: {arr}")
    return arr


print("Array belum diurutkan:", arr)
sorted_arr = insertionSort(arr)
print("\nArray setelah diurutkan:", sorted_arr)
