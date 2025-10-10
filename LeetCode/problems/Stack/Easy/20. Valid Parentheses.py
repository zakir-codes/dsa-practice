class Solution:
    def isValid(self, s: str) -> bool:

        ## solution 1
        map_br = {"]":"[",")":"(","}":"{"}
        open_br =map_br.values()
        stack = []
        for br in s:
            if br in open_br:
                stack.append(br)
            else:
                if not stack:
                    return False
                if map_br[br]!=stack.pop():
                    return False
        return not stack
