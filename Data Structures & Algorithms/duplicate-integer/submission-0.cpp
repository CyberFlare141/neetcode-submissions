class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> singleNumberVector ;
        for(int num:nums){
            if(singleNumberVector.count(num)>0)
                 return true;

            singleNumberVector.insert(num);
        }
        
     return false;   

    }
};


