from common_imports import *

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        remove_R = 0
        remove_D = 0
        c = Counter(senate)
        q = deque(senate)

        while q:
            senator = q.popleft()
            if senator == 'R':
                if remove_R > 0:
                    remove_R -= 1
                    continue
                if c['D'] == 0:
                    return 'Radiant'
                else:
                    remove_D += 1
                    c['D'] -= 1
                    q.append(senator)
            else:
                if remove_D > 0:
                    remove_D -= 1
                    continue
                if c['R'] == 0:
                    return 'Dire'
                else:
                    remove_R += 1
                    c['R'] -= 1
                    q.append(senator)


        return ""