/**     
 * @description
 * argue proposition for Exercises 2.3-7 (page 39)
 *
 * @solution
 * Let x − S = {x − y | y ∈ S}. We sort sets S and x − S and scan them to check, 
 * if some element a appears in both sets. In that case, S contains both a and x − a. 
 * Sorting takes O(n log n) time, while scanning takes O(n) time.
 */

var sort = require('./merge_sort'),
    testedArray = [41, 52, 26, 38, 12, 57, 9, 49],
    target = 109,
    result;

function argueExistence(testedArray, target) {
    var i = 0,
        j = testedArray.length - 1;

    sort.mergeSort(testedArray, 0, testedArray.length - 1);

    while (i < j) {
        if (testedArray[i] + testedArray[j] == target) {
            return true;
        } else if (testedArray[i] + testedArray[j] > target) {
            j--;
        } else {
            i++;
        }
    }

    return false;
}

result = argueExistence(testedArray, target);

console.log(result);