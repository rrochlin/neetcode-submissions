/*
Sorting algorithms are going to give us O(nlogn) complexity. Making a max/min heap of the elements takes
O(n) and then ejecting elements until we get to k will take O(klog(n)) operations. This is scaling relative
to k instead of n but worst case would still be like midway throuhg n i.e. k = n/2 so scales to n....
not strictly faster than sorting in time complexity land but it is in terms of practical use.
*/

#include <algorithm>
#include <iostream>
#include <vector>

class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        std::make_heap(nums.begin(), nums.end());
        for (int i=1; i<k; i++) {
            std::pop_heap(nums.begin(), nums.end());
            nums.pop_back();
        }
        return nums.front();
    }
};
