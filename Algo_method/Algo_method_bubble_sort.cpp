#include <iostream>
#include <vector>
#include <cmath>
#include <numeric>
#include <algorithm>
using namespace std;

int main() {
    int N ;

    cin >> N ;
    vector<int> A(N) ;
    for (int i=0; i<N; i++) cin >> A[i];
    bool flag = false ;
    while (flag == false) {
        flag = true ;
        for (int i=1; i<N; i++) {
            if (A[i-1]> A[i]) {
                int temp = A[i] ;
                A[i] = A[i-1] ;
                A[i-1] = temp ;
                flag = false ;
            }
        }
        if (flag == false) {
            for (int i=0 ; i<N; i++ ) cout << A[i] << " " ;
            cout << endl ;
        }

    }






    return 0;
}