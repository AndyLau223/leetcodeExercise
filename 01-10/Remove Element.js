/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function(nums, val) {
    let index = 0;
    for (let i =0; i < nums.length; i ++){
        if (nums[i] != val) {
            nums[index++] = nums[i];
        }
    }
    return index;
};

/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement2 = function(nums, val) {
    let left = 0;
    let right = nums.length;
    while(left < right) {
        if (nums[left] == val) {
            nums[left] = nums[right -1]
            right--;
        } else {
            left++;
        }
    }
    return left;
};