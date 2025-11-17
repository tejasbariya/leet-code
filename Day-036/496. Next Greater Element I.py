class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(len(nums1)):
            flag = False
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    temp = nums2[j]
                    for k in range(j+1, len(nums2)):
                        if temp < nums2[k]:
                            temp = nums2[k]
                            break
                    if temp == nums2[j]:
                        break
                    res.append(temp)
                    flag = True
                    break
            if not flag:
                res.append(-1)
        return res
