class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        
        unordered_map <int , int> count;
        vector <int> result;

        for(int num:nums)
            count[num]++;

        vector<vector<int>> buckets(nums.size()+1);
          
        for(const auto& pair:count){
            int number = pair.first;
            int freq   = pair.second;
            buckets[freq].push_back(number);
        }
        
        for(int i = buckets.size() -1 ; i >=0 ; --i){
            for(int num:buckets[i]){
                result.push_back(num);
                if(result.size()==k)
                return result;
            }
        }
        
    }
};
