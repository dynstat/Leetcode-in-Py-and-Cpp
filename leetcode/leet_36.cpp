// # Code
// # Testcase
// # Test Result
// # Test Result
// # 36. Valid Sudoku
// # Medium
// # Topics
// # Companies
// # Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

// # Each row must contain the digits 1-9 without repetition.
// # Each column must contain the digits 1-9 without repetition.
// # Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
// # Note:

// # A Sudoku board (partially filled) could be valid but is not necessarily solvable.
// # Only the filled cells need to be validated according to the mentioned rules.

// # Example 1:

// # Input: board =
// # [["5","3",".",".","7",".",".",".","."]
// # ,["6",".",".","1","9","5",".",".","."]
// # ,[".","9","8",".",".",".",".","6","."]
// # ,["8",".",".",".","6",".",".",".","3"]
// # ,["4",".",".","8",".","3",".",".","1"]
// # ,["7",".",".",".","2",".",".",".","6"]
// # ,[".","6",".",".",".",".","2","8","."]
// # ,[".",".",".","4","1","9",".",".","5"]
// # ,[".",".",".",".","8",".",".","7","9"]]
// # Output: true
// # Example 2:

// # Input: board =
// # [["8","3",".",".","7",".",".",".","."]
// # ,["6",".",".","1","9","5",".",".","."]
// # ,[".","9","8",".",".",".",".","6","."]
// # ,["8",".",".",".","6",".",".",".","3"]
// # ,["4",".",".","8",".","3",".",".","1"]
// # ,["7",".",".",".","2",".",".",".","6"]
// # ,[".","6",".",".",".",".","2","8","."]
// # ,[".",".",".","4","1","9",".",".","5"]
// # ,[".",".",".",".","8",".",".","7","9"]]
// # Output: false
// # Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

// # Constraints:

// # board.length == 9
// # board[i].length == 9
// # board[i][j] is a digit 1-9 or '.'.

#include <string>
#include <vector>
#include <unordered_map>
#include <iostream>
#include <set>
#include <map>
#include <stack>
#include <queue>

using namespace std;

class Solution
{
public:
    bool isValidSudoku(vector<vector<char>> &board)
    {
        unordered_map<int, set<int>> row;
        unordered_map<int, set<int>> col;
        unordered_map<int, set<int>> box;

        for (int i = 0; i < 9; i++)
        {
            for (int j = 0; j < 9; j++)
            {
                char curr = board[i][j];
                if (curr == '.')
                {
                    continue;
                }

                int curr_int = int(curr);
                int box_index = (i / 3) * 3 + (j / 3);
                if (row[i].find(curr_int) != row[i].end() || col[j].find(curr_int) != col[j].end() || box[box_index].find(curr_int) != box[box_index].end())
                {
                    return false;
                }

                row[i].insert(curr_int);
                col[j].insert(curr_int);
                box[box_index].insert(curr_int);
            }
        }
        return true;
    }
};

int main()
{
    vector<vector<char>> board = {
        {'5', '3', '.', '.', '7', '.', '.', '.', '.'},
        {'6', '.', '.', '1', '9', '5', '.', '.', '.'},
        {'.', '9', '8', '.', '.', '.', '.', '6', '.'},
        {'8', '.', '.', '.', '6', '.', '.', '.', '3'},
        {'4', '.', '.', '8', '.', '3', '.', '.', '1'},
        {'7', '.', '.', '.', '2', '.', '.', '.', '6'},
        {'.', '6', '.', '.', '.', '.', '2', '8', '.'},
        {'.', '.', '.', '4', '1', '9', '.', '.', '5'},
        {'.', '.', '.', '.', '8', '.', '.', '7', '9'}};

    Solution sol;
    bool isValid = sol.isValidSudoku(board);
    if (isValid)
    {
        cout << "The Sudoku board is valid." << endl;
    }
    else
    {
        cout << "The Sudoku board is NOT valid." << endl;
    }

    return 0;
}
