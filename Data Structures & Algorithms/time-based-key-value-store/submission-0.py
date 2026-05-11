class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp,value))


    def get(self, key: str, timestamp: int) -> str:
        left = 0
        right = len(self.store[key]) - 1
        result = ""

        while left <= right:
            mid = (left+right)//2

            mid_timestamp = self.store[key][mid][0]

            if mid_timestamp == timestamp:
                return self.store[key][mid][1]

            elif mid_timestamp < timestamp:
                result = self.store[key][mid][1]
                left = mid + 1

            else:
                right = mid -1

        return result

            

            
