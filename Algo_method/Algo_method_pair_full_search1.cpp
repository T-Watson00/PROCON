#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <numeric>
#include <algorithm>
using namespace std;

int main() {
    int N,K ;
    cin >> N >> K ;
    vector<int> A(N) ;
    for (int i=0 ; i<N ; i++) {
        cin >> A[i] ;
    }
    int count = 0 ;
    for (int i=0 ; i<N-1 ; i++) {
        for (int j=i+1; j<N ; j++) {
            if (A[i]+A[j]<=K) {
                count++ ;
            }
        }
    }
    cout << count << endl;
    return 0;
}