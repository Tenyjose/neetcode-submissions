class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        res = len(students)
        cnt = defaultdict(int)

        for student in students:
            cnt[student] += 1

        for s in sandwiches:
            if cnt[s] > 0:
                res -=1
                cnt[s] -= 1
            else:
                break

        return res

