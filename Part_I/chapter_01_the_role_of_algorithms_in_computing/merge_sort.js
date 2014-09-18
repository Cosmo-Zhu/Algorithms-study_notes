/**
 * @function
 * 
 * @description
 * Merge two sorted sub-arrays
 *
 * @param {Array} `sortedArray` - To be sorted array.
 */

function merge(sortedArray, start, middle, end) {
    var leftLength = middle - start + 1,
        rightLength = end - middle,
        leftCache = [],
        rightCache = [],
        i = 0, j = 0,
        lastStart = start;

    leftCache = sortedArray.slice(start, middle + 1);
    rightCache = sortedArray.slice(middle + 1, end + 1);

    while(i < leftLength && j < rightLength) {
        if (leftCache[i] <= rightCache[j]) {
            sortedArray[lastStart] = leftCache[i];
            lastStart++;
            i++;
        } else {
            sortedArray[lastStart] = rightCache[j];
            lastStart++;
            j++;
        }
    }

    while(i < leftLength) {
        sortedArray[lastStart] = leftCache[i];
        lastStart++;
        i++;
    }

    while(j < rightLength) {
        sortedArray[lastStart] = rightCache[j];
        lastStart++;
        j++;
    }
}

function mergeSort(sortedArray, start, end) {
    if (start < end) {
        var middle = Math.floor((start + end) / 2);
        mergeSort(sortedArray, start, middle);
        mergeSort(sortedArray, middle + 1, end);
        merge(sortedArray, start, middle, end);
    }
}

var sortedArray = [41, 52, 26, 38, 57, 9, 49, 3];
console.log(sortedArray);
mergeSort(sortedArray, 0, sortedArray.length - 1);
console.log(sortedArray);