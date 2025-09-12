class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int[] res = new int[m + n];
        int j = 0; //iterate over nums1
        int k = 0; //iterate over nums2
        for(int i = 0; i < res.length; i++){
            int currMin = -1;
            int mVal = Integer.MAX_VALUE;
            int nVal = Integer.MAX_VALUE;
            if(j < m){
                mVal = nums1[j];
            }
            if(k < n){
                nVal = nums2[k];
            }
            if(mVal < nVal){
                currMin = mVal;
                j++;
            }
            else{
                currMin = nVal;
                k++;
            }
            res[i] = currMin;
        }
        for(int i = 0; i < m+n; i++){
            nums1[i] = res[i];
        }
    }
}