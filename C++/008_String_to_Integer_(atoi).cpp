class Solution {
public:
    int myAtoi(string str) {
    	int i = str.find_first_not_of(' ');
    	if (i == str.length()) return 0;

    	int sign = 1;
    	if (str[i] == '-') {sign = -1; i++;}
    	else if (str[i] == '+') i++;

    	int tot = 0;
    	int m = INT_MAX / 10, n = INT_MAX % 10;
    	while (i < str.length() && str[i] >= '0' && str[i] <= '9') {
    		int digit = str[i] - '0';
    		if (sign == 1 && (tot > m || (tot == m && digit > n)))
    			return INT_MAX;
    		else if (sign == -1 && (tot > m || (tot == m && digit > n+1)))
    			return INT_MIN;
    		else tot = tot * 10 + digit;
    		i++;
    	}
    	return tot * sign;
    }
};
