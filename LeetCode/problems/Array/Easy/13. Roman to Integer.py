class Solution:
    def romanToInt(self, s: str) -> int:
        ## solution 1
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        s = s.replace("IV","IIII").replace("IX","VIIII") # 4, 9
        s = s.replace("XL","XXXX").replace("XC","LXXXX") # 40, 90
        s = s.replace("CD","CCCC").replace("CM","DCCCC") # 400, 900

        num = 0
        for c in s:
            num += translations[c]
        return num
