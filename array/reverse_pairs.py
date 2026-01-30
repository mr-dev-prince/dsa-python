class Solution:
    def reversePairs(self, nums):
        def mergeSort(arr):
            if len(arr) <= 1:
                return arr, 0

            mid = len(arr) // 2
            left, cntL = mergeSort(arr[:mid])
            right, cntR = mergeSort(arr[mid:])

            # count cross pairs
            cnt = cntL + cntR
            j = 0
            for i in range(len(left)):
                while j < len(right) and left[i] > 2 * right[j]:
                    j += 1
                cnt += j

            # merge sorted arrays
            merged = []
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1

            merged.extend(left[i:])
            merged.extend(right[j:])

            return merged, cnt

        _, result = mergeSort(nums)
        return result
