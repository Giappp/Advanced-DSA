# Phương pháp sắp xếp đếm phân phối hoạt động bằng cách
# đếm số lượng phần tử trong mảng ban đầu, sau đó
# sử dụng mảng đếm để xây dựng lại mảng đã sắp xếp.


# arr = { 1, 4, 1, 2, 7, 1, 2, 5, 3, 6 }
def counting_sort(arr):
    # Bước 1: Tìm giá trị lớn nhất của mảng
    max_val = max(arr)

    # Khởi tạo Mảng tần suất với kích thước là giá trị lớn nhất của mảng + 1
    count_array = [0] * (max_val + 1)

    # Cập nhật mảng tần suất: count_array[i] là tần suất xuất hiện của i trong mảng ban đầu
    for i in arr:
        count_array[i] += 1
    # Bước 4: Tạo mảng kết quả đã sắp xếp
    sorted_arr = []
    for i in range(len(count_array)):
        sorted_arr.extend([i] * count_array[i])

    return sorted_arr, count_array


def find_mode(count):
    max_count = max(count)
    mode = [i for i, c in enumerate(count) if c == max_count]
    return mode


def find_median(sorted_arr):
    n = len(sorted_arr)
    if n % 2 == 1:
        return sorted_arr[n // 2]
    else:
        return (sorted_arr[n // 2 - 1] + sorted_arr[n // 2]) / 2


arr = [1, 4, 1, 2, 7, 1, 2, 5, 3, 6]

sorted_A, count_A = counting_sort(arr)

mode_A = find_mode(count_A)

median_A = find_median(sorted_A)

# Kết quả
print("Mảng sau khi sắp xếp:", sorted_A)
print("Mốt của mảng A:", mode_A)
print("Trung vị của mảng A:", median_A)

print("Mảng đếm:", count_A)
