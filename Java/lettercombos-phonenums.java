class Solution {
    HashMap<Integer, char[]> numList = new HashMap<>();
    ArrayList<String> result;
    int size;

    public List<String> letterCombinations(String digits) {
        char[] two = {'a','b','c'}; //0
        char[] three = {'d', 'e', 'f'}; //1
        char[] four = {'g', 'h', 'i'}; //2
        char[] five = {'j', 'k', 'l'}; //3
        char[] six = {'m', 'n', 'o'}; //4
        char[] seven = {'p','q','r', 's'}; //5
        char[] eight = {'t','u','v'}; //6
        char[] nine = {'w','x','y','z'}; //7

        numList.put(2, two);
        numList.put(3, three);
        numList.put(4, four);
        numList.put(5, five);
        numList.put(6,six);
        numList.put(7,seven);
        numList.put(8, eight);
        numList.put(9, nine);

        result = new ArrayList<>();
        size = digits.length();
        if(size == 0){
            return new ArrayList<>();
        }
        generate("", 0, digits);
        return result;
    }

    void generate(String res, int index, String digits){
        if(res.length() == size){
            result.add(res);
            return;
        }
        char[] chars = numList.get((int)digits.charAt(index)-'0');
        for(int i = 0; i < chars.length; i++){
            generate(res + chars[i], index+1, digits);
        }
    }
}