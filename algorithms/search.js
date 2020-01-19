/**
 * Implement these two search algorithms.
 */

/**
 * Search for the number in the sorted list with the linear search algorithm
 * and return the index of the element.
 *
 * Optional: print out how many comparision was needed to find the number
 *
 * @param {number} number The number to search for
 * @param {array} list Ascending list of numbers
 * @returns {number|null} Index of the element or null
 */
function linear_search(number, list) {
    for (let index = 0; index < list.length; index++) {
        if (list[index] == number) {
            console.log("Compared: " + (index + 1) + " times")
            return index
        }
    }

    return null;
}

/**
 * Search for the number in the sorted list with the binary search algorithm
 * and return the index of the element.
 *
 * Optional: print out how many comparision was needed to find the number
 *
 * @param {number} number The number to search for
 * @param {array} list Ascending list of numbers
 * @returns {number|null} Index of the element or null
 */
function binary_search(number, list) {
    let compared = 0;
    let low_bound = 0;
    let high_bound = list.length - 1;
    let middle_bound;
    while(low_bound <= high_bound){
        middle_bound = Math.floor((low_bound + high_bound) / 2);
        console.log(middle_bound)
        compared++;
        if(list[middle_bound] === number){
            console.log("Compared: " + compared + " times");
            return middle_bound
        }
        else if(list[middle_bound] > number){
            high_bound = middle_bound - 1;
        }
        else{
            low_bound = middle_bound + 1;
        }
    }
    return null;
}

function print_result(search, index) {
    let result = search + ' search ';

    if (index === null) {
        result += 'did not find it.'
    } else {
        result += `found it on index ${index}.`
    }

    console.log(result);
}


function main() {
    let numbers = [3, 6, 8, 11, 18, 23, 24, 33, 36, 45, 46, 51, 56, 60, 69, 72, 83, 90, 93, 97];
    let searched_number = Number(prompt('What is the number you are looking for? (0-100)'));

    print_result('Linear', linear_search(searched_number, numbers));
    print_result('Binary', binary_search(searched_number, numbers));
}

main();

