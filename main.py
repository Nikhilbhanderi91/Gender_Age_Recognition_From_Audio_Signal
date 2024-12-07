#include <iostream>
using namespace std;

// Recursive binary search function
int binarySearchRecursive(int arr[], int low, int high, int target) {
    // Base case: if the range is invalid
    if (low > high) {
        return -1; // Target not found
    }

    // Calculate the middle index
    int mid = low + (high - low) / 2;

    // Check if the target is at the middle
    if (arr[mid] == target) {
        return mid;
    }
    // If the target is smaller, search the left subarray
    else if (target < arr[mid]) {
        return binarySearchRecursive(arr, low, mid - 1, target);
    }
    // If the target is larger, search the right subarray
    else {
        return binarySearchRecursive(arr, mid + 1, high, target);
    }
}

int main() {
    int array[] = {2, 4, 6, 8, 10, 12, 14};
    int size = sizeof(array) / sizeof(array[0]);
    int target = 10;

    // Call the recursive binary search function
    int result = binarySearchRecursive(array, 0, size - 1, target);

    if (result != -1) {
        cout << "Element " << target << " found at index " << result << endl;
    } else {
        cout << "Element " << target << " not found in the array" << endl;
    }

    return 0;
}
