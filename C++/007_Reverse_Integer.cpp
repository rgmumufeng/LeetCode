class Solution {
public:
    int reverse(int x) {
        if (x == INT_MIN) return 0;
        int q = x < 0 ? -x : x, tot = 0;
        int m = INT_MAX / 10, n = INT_MAX % 10;
        while (q != 0 and tot < m) {
            tot = tot * 10 + q % 10;
            q = q / 10;
        }
        if (q == 0) return x < 0 ? -tot : tot;
        else if (tot == m && x < 0 && q <= n+1) return -(tot*10+q);
        else if (tot == m && x > 0 && q <= n) return tot*10+q;
        else return 0;
    }
};
