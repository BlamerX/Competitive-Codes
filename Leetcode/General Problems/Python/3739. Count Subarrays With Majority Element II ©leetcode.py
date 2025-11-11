class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        counts={0:1}
        score=0
        total=0

        prefix=0

        for i in nums:
            old_score=score

            if i==target:
                score+=1
            else:
                score-=1

            if score>old_score:
                prefix+=counts.get(old_score,0)
            else:
                prefix-=counts.get(old_score-1,0)

            total+=prefix
            counts[score]=counts.get(score,0)+1

        return total