# Title: Time Based Key-Value Store
# Link: https://neetcode.io/problems/time-based-key-value-store
# Difficulty: Medium 
# Tags: Binary Search

class TimeMap:

    def __init__(self):
        self.data = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        vals = self.data[key]
        result = "" # Track the best result so far

        # Given key doesn't have any value
        if not vals:
            return result

        left_p, right_p = 0, len(vals) - 1
        VAL_IDX, TS_IDX = 0, 1


        while left_p <= right_p:
            mid_p = (left_p + right_p) // 2
            mid = vals[mid_p][TS_IDX]

            if mid <= timestamp:
                # A timestamp <= target timestamp is valid
                result =  vals[mid_p][VAL_IDX]
                
                # But there is still a possibility of
                # finding the target timestamp or a timestamp
                # that is greater than the current timestamp i.e.
                # closer to the target timestamp than the
                # current one
                left_p = mid_p + 1
                
            else:
                right_p = mid_p - 1

        return result