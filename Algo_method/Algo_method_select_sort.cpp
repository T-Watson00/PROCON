#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <numeric>
#include <algorithm>
using namespace std;


int main() {
    int N ;
    cin >> N ;
    vector<int> A(N) ;
    for (int i = 0 ;i < N ; i++) cin >> A[i] ;
    for (int j =0 ;j < N-1 ; j++) {
        vector<int>::iterator min_iterator = min_element(A.begin()+j, A.end());
        size_t A_part_min_index = distance(A.begin(), min_iterator);
        if (A[j] > A[A_part_min_index]) {
            int tmp = A[j];
            A[j] = A[A_part_min_index];
            A[A_part_min_index] = tmp ;
        }
        for (int i = 0 ; i < N ; i++) cout << A[i] << " " ;
        cout << endl ;
    }



    return 0;
}