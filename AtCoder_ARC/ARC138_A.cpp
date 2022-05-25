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
    vector<int> A(N);
    for (int i = 0; i<N;i++) {
        cin >> A[i];
    }
    int count = N*N ;
    int a = 0;
    for(int i = 1;i<K;i++) {
        for (int j = K;j<N;j++) {
            if (A[i] < A[j]) {
                a = j-i ;
                count = min(count,a);
            }
        }
    }
    if (count == N*N){
        cout << -1 << endl;
    }
    else {
        cout << count << endl;
    }


    return 0;
}

