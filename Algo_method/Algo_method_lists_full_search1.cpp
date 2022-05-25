#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <numeric>
#include <algorithm>
using namespace std;

int main() {
    int N,M ;
    cin >> N >> M ;
    vector<int> A(N),B(M) ;
    int count = 0 ;
    for (int i = 0 ; i < N; i++) {
        cin >> A[i] ;
    }
    for (int i = 0 ; i < M; i++) {
        cin >> B[i] ;
    }
    for (int i = 0 ; i < N; i++) {
        for (int j = 0 ; j < M; j++) {
            if (A[i] > B[j]) {
                count++ ;
            }
        }
    }
    cout << count << endl;

    return 0;
}