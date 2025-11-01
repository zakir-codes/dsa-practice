class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
      ## solution 1: Time O(1) Space O(1)  
      times = []

        for h in range(12):
            for m in range(60):
                h1s = bin(h).count("1")
                m1s = bin(m).count("1")

                if h1s + m1s == turnedOn:
                    times.append(f"{h}:{m:02d}")
        return times
