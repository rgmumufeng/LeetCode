class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> ref;
        int i = 0;
        int maxlen = 0;
        for (int j = 0; j < s.size(); j++) {
            if (ref.count(s[j]) != 0 && ref[s[j]] >= i) i = ref[s[j]]+1;
            ref[s[j]] = j;
            maxlen = max(maxlen, j-i+1);
            if (maxlen >= s.size()-i) break;
        }
        return maxlen;
    }
};


