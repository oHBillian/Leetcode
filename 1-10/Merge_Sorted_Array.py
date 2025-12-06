# Example 1: Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3 Output: [1,2,2,3,5,6]

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
#Output: [1,2,2,3,5,6]
def merge(nums1, m, nums2, n):
    # โจทย์ให้ตัวเลขที่เรียงจากน้อยไปหามาก *
    # สร้าง 3 pointer 
    last_indx = m+n - 1 # ตำแหน่งสุดท้ายของ num1 ( 0 )
    p1 = m - 1 # ตัวเลขสุดท้ายของ nums1
    p2 = n - 1 # ตัวเลขสุดท้ายของ nums2
    while p2 >= 0:
        if nums1[p1] > nums2[p2] and p1 >= 0:
            nums1[last_indx] = nums1[p1]
            p1 -= 1
        else:
            nums1[last_indx] = nums2[p2]
            p2 -= 1
        last_indx -= 1
    return nums1

print(merge(nums1, m, nums2, n))