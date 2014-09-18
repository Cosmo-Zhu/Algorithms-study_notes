/**
 * @function
 * 
 * @description
 * Selection sort algorithms
 *
 * @param {} `` – .
 */
 function selectSort() {
    var A = [12, 3, 7, 9, 83, 0, 23];
    console.log(A);

    for (var i = 0; i < A.length - 1; i++) {
        var smallest = A[i],
            index = i;
        for (var j = i + 1; j < A.length; j++) {
            if (smallest > A[j]) {
                smallest = A[j];
                index = j;
            }
        }
        A[index] = A[i];
        A[i] = smallest;
    }

    console.log(A);
 }

 selectSort();