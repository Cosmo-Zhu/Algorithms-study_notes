/**     
 * @description
 * Binary adding algorithms
 */
var A = [1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0],
    B = [0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1],
    C = [],
    bound = A.length,
    carry = 0;

for (var i = 1; i <= bound; i++) {
    if ((A[bound - i] + B[bound - i] + carry) == 2) {
        C.unshift(0);
        carry = 1;
    }
    else if ((A[bound - i] + B[bound - i] + carry == 3)) {
        C.unshift(1);
        carry = 1;
    }
    else {
        var result = A[bound - i] + B[bound - i] + carry;
        C.unshift(result);
        carry = 0;
    }
}

if (carry != 0) {
    C.unshift(1);
}

console.log(C);