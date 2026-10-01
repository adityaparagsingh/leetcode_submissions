/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    const res = arr.flatMap((nums , i) => {
        if(fn(nums,i)){
            return nums
        }
        else{
            return []
        }
    })
    return res
};