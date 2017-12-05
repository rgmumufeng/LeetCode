class Solution1 {
public:
    string convert(string s, int numRows) {
        if (numRows <= 1) return s;
        string res;
        int k = numRows-1, ind = -1;
        for (int step = k; step >= 0; step--) {
        	for (int i = 0; i <= s.size()/(k*2); i++) {
        		int center = k + k * 2 * i;
        		int inds[2] = {center-step, center+step};
        		for (int j = 0; j < 2; j++) {
        			if (inds[j] != ind && inds[j] < s.size()) {
        				ind = inds[j];
        				res.push_back(s[ind]);
        			}
        		}
        	}
        }
        return res;
    }
};

class Solution2 {
public:
    string convert(string s, int numRows) {
        if (numRows <= 1) return s;
        string *l = new string[numRows];
        int direction = 1, row = 0;
        for (int i = 0; i < s.size(); i++) {
        	l[row].push_back(s[i]);
        	row += direction;
        	if (row == 0 || row == numRows-1) direction = -direction;
        }
        string res;
        for (int i = 0; i < numRows; i++) res.append(l[i]);
        delete[] l;
        return res;
    }
};
