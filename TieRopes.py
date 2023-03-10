def solution(K, A):
    acc_length = 0
    count = 0
    for rope in A:
        acc_length += rope
        if acc_length >= K:
            count += 1
            acc_length = 0
    return count
