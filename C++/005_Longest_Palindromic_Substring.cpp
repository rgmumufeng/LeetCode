class Solution {
public:
    string longestPalindrome(string s) {
        int center = 0;
        string palin = "";
        while (center >= 0 && center < s.size() && s.size()-center >= palin.size()/2) {
            int i=center, j=center;
            while (j+1 < s.size() && s[j+1] == s[j]) j++;
            center = j + 1;
            while (i-1 >= 0 && j+1 < s.size() && s[i-1] == s[j+1]) {i--; j++;}
            if (j-i+1 > palin.size()) palin = s.substr(i, j-i+1);

        }
        return palin;
    }
};
