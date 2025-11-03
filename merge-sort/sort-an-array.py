class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergesort(nums)


    def mergesort(self, array):
        if len(array) < 2:
            return array
        if len(array) == 2:
            if array[0] > array[1]:
                array[0], array[1] = array[1], array[0]
            return array

        m = len(array) // 2
        sub1 = self.mergesort(array[0:m])
        sub2 = self.mergesort(array[m:])

        return self.merge(sub1, sub2)

    def merge(self, sub1, sub2):
        res = []
        i, j = 0, 0

        while i < len(sub1) or j < len(sub2):
            if i == len(sub1):
                res.append(sub2[j])
                j += 1
                continue
            if j == len(sub2):
                res.append(sub1[i])
                i += 1
                continue

            if sub1[i] < sub2[j]:
                res.append(sub1[i])
                i+=1
            else:
                res.append(sub2[j])
                j += 1
        return res

            
        
        