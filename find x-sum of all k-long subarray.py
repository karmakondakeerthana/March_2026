class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        freq = Counter()
        result = []
        for i in range(k):
            freq[nums[i]] += 1
        def get_x_sum(freq):
            heap = [(-count, -num) for num, count in freq.items()]
            heapq.heapify(heap)
            chosen = []
            for _ in range(min(x, len(heap))):
                count, num = heapq.heappop(heap)
                count, num = -count, -num
                chosen.append((num, count))
            total = 0
            for num, count in chosen:
                total += num * count
            return total
        result.append(get_x_sum(freq))
        for i in range(k, n):
            out_num = nums[i - k]
            in_num = nums[i]
            freq[out_num] -= 1
            if freq[out_num] == 0:
                del freq[out_num]
            freq[in_num] += 1
            result.append(get_x_sum(freq))
        
        return result
