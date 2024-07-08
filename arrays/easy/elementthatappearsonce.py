class Solution {
public:
    int singleNumber(vector<int>& a) {
        int x=0;
        int n=a.size();
        for(int i:a){
            x^=i;
        }
        return x;
        
        
    }
};
