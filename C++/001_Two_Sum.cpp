class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> ref;
        vector<int> res;
        for (int i = 0; i < nums.size(); i++) {
	        auto it = ref.find(target-nums[i]);
	        if (it != ref.end()) {
		        res.push_back(it->second);
		        res.push_back(i);
		    break;
	        }
	        else ref[nums[i]] = i;
        }
        return res;
    }
};

