"""
public class Solution {

    public int solution(int m, int n, int[][] cityMap) {

        // MOD 연산을 위한 상수
        int MOD = 20170805;

        // dp[i][j][k]: 좌표 (i, j) 에서 방향 k에 따라 각각 갈 수 있는 경우의 수
        int[][][] dp = new int[m + 1][n + 1][2];

        // (0, 0)에서 가로, 세로로 진행할 수 있는 경우의 수는 각각 1
        dp[1][1][0] = 1;
        dp[1][1][1] = 1;

        // 0: 가로, 1: 세로
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                // 값이 0이면, 가로, 세로로 진행할 수 있음
                if (cityMap[i - 1][j - 1] == 0) {
                    int toAdd = dp[i - 1][j][1] + dp[i][j - 1][0];
                    // 가로로 진행할 수 있는 경우의 수
                    dp[i][j][0] += toAdd;
                    // 세로로 진행할 수 있는 경우의 수
                    dp[i][j][1] += toAdd;
                }
                // 값이 2이면 오던 방향으로만 진행할 수 있음
                else if (cityMap[i - 1][j - 1] == 2) {
                    dp[i][j][0] = dp[i][j - 1][0];
                    dp[i][j][1] = dp[i - 1][j][1];
                }

                // MOD 연산
                dp[i][j][0] %= MOD;
                dp[i][j][1] %= MOD;
            }
        }

        // (m - 1, n - 1)까지 가는 경우의 수
        return (dp[m - 1][n][1] + dp[m][n - 1][0]) % MOD;
    }
}
"""
