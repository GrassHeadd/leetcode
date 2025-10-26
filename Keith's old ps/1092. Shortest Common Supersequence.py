class Solution:
    def shortestCommonSupersequence(self, name1, name2):
        m, n = len(name1), len(name2)
        
        # Initialize dp table
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Fill the table
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0:
                    dp[i][j] = j  # If first string is empty, take all chars from name2
                elif j == 0:
                    dp[i][j] = i  # If second string is empty, take all chars from name1
                elif name1[i - 1] == name2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1])
        
        # Reconstruct the shortest supersequence
        i, j = m, n
        supersequence = []
        
        while i > 0 and j > 0:
            if name1[i - 1] == name2[j - 1]:
                supersequence.append(name1[i - 1])
                i -= 1
                j -= 1
            elif dp[i - 1][j] < dp[i][j - 1]:
                supersequence.append(name1[i - 1])
                i -= 1
            else:
                supersequence.append(name2[j - 1])
                j -= 1
        
        # If any characters left in name1 or name2, add them
        while i > 0:
            supersequence.append(name1[i - 1])
            i -= 1
        while j > 0:
            supersequence.append(name2[j - 1])
            j -= 1
        
        # The supersequence was built backwards, so reverse it
        supersequence.reverse()
        
        return ''.join(supersequence)
    
print(Solution().shortestCommonSupersequence("thequickbrownfoxjumpsoverthelazydog", "thequickcyanfoxhidesoverthelazycat"))  # For CS3230 PA2 test case