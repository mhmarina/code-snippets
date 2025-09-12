class Solution {
    public boolean isValidSudoku(char[][] board) {
        HashSet<Character> rows = new HashSet<>();
        HashSet<Character> cols = new HashSet<>();
        HashMap<String, HashSet<Character>> block = new HashMap<>();

        //check rows:
        for(int i = 0; i < 9; i++){
            rows.clear();
            for(int j = 0; j < 9; j++){
                if(board[i][j] != '.'){
                    int tempSize = rows.size();
                    rows.add(board[i][j]);
                    if(rows.size() == tempSize){
                        System.out.println("exited at 1");
                        return false;
                    }
                }
            }
        }

        //check cols:
        for(int i = 0; i < 9; i++){
            cols.clear();
            for(int j = 0; j < 9; j++){
                if(board[j][i] != '.'){
                    int tempSize = cols.size();
                    cols.add(board[j][i]);
                    if(cols.size() == tempSize){
                        System.out.println("exited at 2");
                        return false;
                    }
                }
            }
        }     

        //check boxes:
        for(int i = 0; i < 9; i++){
            for(int j = 0; j < 9; j++){
                String currKey = "";
                if(board[i][j] != '.'){
                    currKey += i/3;
                    currKey += j/3;
                    System.out.print(currKey);
                    if(block.get(currKey) == null){
                        block.put(currKey, new HashSet<Character>());
                    }
                    int tempSize = block.get(currKey).size();
                    block.get(currKey).add(board[i][j]);
                    if(block.get(currKey).size() == tempSize){
                        System.out.println("exited at 3");
                        return false;
                    }
                }
            }
        }
        return true;
    }
}