def solution(n):
    # answer = 0
    # for i in range(1, n+1):
    #     if n % i == 0:
    #         answer += i
    # return answer

    return sum([i for i in range(1, n+1) if n % i == 0])

num = int(input())

print(solution(num))