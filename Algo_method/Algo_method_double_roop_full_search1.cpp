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
    for (int i = 0 ; i < N ; i++) cin >> A[i] ;
    int count = 0;
    bool flag;

    for (int i=0; i<N ;i++) {
        flag = true;
        if (A[i] == 1) flag = false;
        for (int j=1; j<= sqrt(A[i]);j++) {
            if (j==1) continue ;
            if (A[i] % j == 0) {
                flag = false ;
                break;
            }
        }
        if (flag) count++;
    }
    cout << count << endl;
    return 0;
}
