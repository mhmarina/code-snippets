class Solution {
    public String breakPalindrome(String palindrome) {
        String res = palindrome;
        if(palindrome.length() == 1){
            return "";
        }

        else{
            int i = 0;
            while(i < (res.length() / 2) && res.charAt(i) == 'a'){
                i ++;
            }
            char[] charArray = res.toCharArray();
            if(i < (res.length() / 2)){
                charArray[i] = 'a';
                res = String.valueOf(charArray);
            }
            else{
                charArray[charArray.length - 1] = 'b'; 
                res = String.valueOf(charArray);
            }
        }
        return res;
    }
}