def main(arr, alpha):
    result = [arr[0]]
    for i in range(1, len(arr)):
        result.append(alpha * arr[i] + (1-alpha) * result[i-1])
    return result

print(main([41, 48, 53, 40, 51, 50, 39, 38, 47, 55, 46, 52, 49, 61, 64, 54, 67, 65, 63, 70], 0.17))
