class Solution {
    String res;
    public String countAndSay(int n) {
        backTrack(1,n,"1");
        return res;
    }
    public void  backTrack(int curr, int target, String str){
        if(curr == target){
            res = str;
        }
        else{
            int i = 0;
            String newStr = "";
            while(i < str.length()){
                int length = 0;
                char currNum = str.charAt(i);
                while(str.charAt(i) == currNum){
                    length++;
                    i++;
                    if(i >= str.length()){
                        break;
                    }
                }
                newStr += length;
                newStr += currNum;
            }
            backTrack(curr+1, target, newStr);
        }
    }
}