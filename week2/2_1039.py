import sys
from collections import deque


# 문자열 s의 i번째 문자와 j번째 문자를 교환한 문자열 반환
def swap(s, i, j):
    s = list(s)
    s[i], s[j] = s[j], s[i]
    return ''.join(s)


def main():
    # 정수 N, 교환 횟수 K
    n, k = map(int, sys.stdin.readline().split())
    n = str(n)

    # 큐 생성
    q = deque()
    q.append((n, k))

    answer = -1
    while q:
        # 현재 숫자, 남은 교환 횟수
        s, k = q.popleft()

        # 교환 횟수가 0이면 최댓값 갱신
        if k == 0:
            answer = max(answer, int(s))
            continue
        # 교환 가능한 모든 경우의 수를 큐에 추가
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                # 맨 앞자리가 0이면 교환 불가
                if i == 0 and s[j] == '0':
                    continue
                # 문자열 교환
                new_s = swap(s, i, j)
                if (new_s, k - 1) not in q:
                    q.append((new_s, k - 1))

    # 정답 출력
    print(answer)


# 메인 함수 호출
if __name__ == '__main__':
    main()
