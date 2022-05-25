#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <numeric>
#include <algorithm>
using namespace std;

int main() {
    int N,M,K ;
    cin >> N >> M >> K;
    vector<int> A(N),B(M) ;
    for (int i=0;i<N;i++) {
        cin >> A[i];
    }
    for (int i=0;i<M;i++) {
        cin >> B[i];
    }
    int count = 0 ;
    for (int i=0; i<N;i++) {
        for (int j=0; j<M; j++) {
            if (A[i]+B[j]== K) {
                count++ ;
            }
        }
    }
    cout << count << endl;


    return 0;
}