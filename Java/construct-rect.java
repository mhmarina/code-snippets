class Solution {
    public int[] constructRectangle(int area) {
        int length = 0;
        int width = 0;
        int diff = Integer.MAX_VALUE;
        for(int i = area; i >= 1; i--){
            if(area % i == 0){
                int div = area / i;
                if(Math.abs(div-i) < diff){
                    length = Math.max(i,div);
                    width = Math.min(i,div);
                    diff = length - width;
                }
            }
        }
        int[] res = {length, width};
        return res;
    }
}