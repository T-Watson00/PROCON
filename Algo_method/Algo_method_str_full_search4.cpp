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
    string S,T ;
    cin >> S >> T ;
    int count = 0 ;
    for (int i = 0 ; i < N ; i++) {
        if (S[i] != T[i]) {
            count++ ;
        }
    }
    cout << count << endl ;


    return 0;
}