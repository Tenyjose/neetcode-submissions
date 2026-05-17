class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        # we have to setup the hashmap first
        tasks_map = defaultdict(int)
        for task in tasks:
            tasks_map[task] += 1

        # now we have to setup the max-heap as we need the top count tasks at each point
        max_heap = [-count for count in tasks_map.values()]
        heapq.heapify(max_heap)

        time = 0
        queue = deque()

        while max_heap or queue:
            time += 1

            if max_heap:
                count = heapq.heappop(max_heap)
                count += 1
                if count < 0:
                    queue.append([count,time+n])

            if queue and queue[0][1] == time:
                count,_ = queue.popleft()
                heapq.heappush(max_heap,count)
            

        return time



        