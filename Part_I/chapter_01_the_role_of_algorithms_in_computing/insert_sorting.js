/**
 * @function
 * 
 * @description
 * Insert sort algorithm
 *
 * @param {boolean} `isOrderByDesc` – A flag that indicate the sorting order.
 */
function insertSorting(isOrderByDesc) {
    var rawInput = [31, 41, 59, 26, 41, 58];
    console.log(rawInput);
    console.log('\n');

    if (isOrderByDesc) {
        for (var j = 1; j < rawInput.length; j++) {
            var key = rawInput[j];
            // Insert rawInput[j] into the sorted sequence rawInput[0..j - 1].
            var i = j - 1;
            while (i > -1 && rawInput[i] < key) {
                rawInput[i + 1] = rawInput[i];
                i--;
            }
            rawInput[i + 1] = key;
            console.log(rawInput);
        }
    } else {
        for (var j = 1; j < rawInput.length; j++) {
            var key = rawInput[j],
                i = j - 1;

            while (i > -1 && rawInput[i] > key) {
                rawInput[i + 1] = rawInput[i];
                i--;
            }
            rawInput[i + 1] = key;
            console.log(rawInput);
        }
    }
}

var isOrderByDesc = false;
insertSorting(isOrderByDesc);
// insertSorting(true);