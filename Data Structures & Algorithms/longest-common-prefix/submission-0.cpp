class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string ans = "";
        sort(strs.begin(),strs.end());
        int n=strs.size();
        string left=strs[0];
        string last=strs[n-1];
        for(int i =0;i<left.size();i++){
            if(left[i]!=last[i]){
                return ans;
            }
            ans+=left[i];
        }
        return ans;
    }
};