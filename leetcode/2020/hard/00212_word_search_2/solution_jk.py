class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def check_word(word, w_idx):
            check = True

            while w_idx and check:
                check = False

                idx = len(w_idx)
                i, j = w_idx[-1]

                candidate = []

                if i > 0:
                    candidate.append((i-1, j))
                if i < N - 1:
                    candidate.append((i+1, j))
                if j > 0:
                    candidate.append((i, j-1))
                if j < M - 1:
                    candidate.append((i, j+1))

                for i, j in candidate:
                    if board[i][j] == word[idx] and (i, j) not in w_idx:
                        w_idx.append((i, j))
                        check = True
                        break

                if len(w_idx) == len(word):
                    break

            return len(word) == 1 or check

        def word_search(word):
            for i, row in enumerate(board):
                for j, char in enumerate(row):
                    if word[0] == char:
                        w_idx = [(i, j)]
                        if len(word) == 1 or check_word(word, w_idx):
                            return True
            return False
        
        N = len(board)
        M = len(board[0])
        
        ans = []
        for word in words:
            if word_search(word):
                ans.append(word)
                
        return ans
