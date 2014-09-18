/**
 * @function
 * 
 * @description
 * Binary search algorithm. Solution to Exercise 2.3-5.
 *
 * @param {boolean} `isOrderByDesc` – A flag that indicate the sorting order.
 */
function binarySearchByOffset(haystack, needle, baseIndex, finded){
    if (haystack.length < 1) {
        return finded ? baseIndex : null;
    }

    var midPoint = Math.floor(haystack.length / 2),
        middle = haystack[midPoint];

    if (needle == middle) {
        finded = true;
        return baseIndex + midPoint;
    } else if (needle < middle) {
        haystack = haystack.slice(0, midPoint);
        return binarySearchByOffset(haystack, needle, baseIndex, finded);
    } else {
        haystack = haystack.slice(midPoint + 1);
        baseIndex = baseIndex + midPoint + 1;
        return binarySearchByOffset(haystack, needle, baseIndex, finded);
    }
}

function binarySearchByRecursive(haystack, needle, low, high) {
    if (low > high) {
        return null;
    }

    var mid = Math.floor((low + high) / 2);

    if (needle == haystack[mid]) {
        return mid;
    } else if (needle > haystack[mid]) {
        return binarySearchByRecursive(haystack, needle, mid + 1, high);
    } else {
        return binarySearchByRecursive(haystack, needle, low, mid - 1);
    }
}

function binarySearchByIterative(haystack, needle, low, high) {
    while (low <= high) {
        var mid = Math.floor((low + high) / 2);

        if (needle == haystack[mid]) {
            return mid;
        } else if (needle > haystack[mid]) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }

    return null;
}

var haystack = [10, 26, 30, 31, 41, 42, 43, 58, 59],
    needle = 30,
    index;

// index = binarySearchByIterative(haystack, needle, 0, haystack.length);

index = binarySearchByRecursive(haystack, needle, 0, haystack.length);

// var finded = false,
//     baseIndex = 0;
// index = binarySearchByOffset(haystack, needle, baseIndex, finded);
console.log(index);