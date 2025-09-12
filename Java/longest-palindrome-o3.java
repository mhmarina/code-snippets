class Solution {
    public String longestPalindrome(String s) {
        //pseudocode:
        // i = start
        // j = end
        // if s[j] == s[i]: cache j
        // enter another while s[j] == s[i]

        int longest = -1;
        String longestPal = "";

        for(int i = 0; i < s.length(); i++){
            for(int j = s.length() - 1; j >= i; j--){
                if(s.charAt(i) == s.charAt(j)){
                    int right = j;
                    int left = i;
                    while(s.charAt(right) == s.charAt(left)){
                        right--;
                        left++;
                        if(right <= left){
                            if(j-i > longest){
                                longest = j-i;
                                longestPal = s.substring(i,j+1);
                            }
                            break;
                        }
                    }
                }
            }
        }
        return longestPal;
    }
}