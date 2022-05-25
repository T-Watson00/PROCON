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
    int count = 0;
    int div;
    for (int i = 1 ;i <= N ;i++) {
        div = 0 ;
        for (int j=1;j<= i; j++) {
            if (i % j == 0) div++ ;
        }
        if (div == K) count++ ;
    }
    cout << count << endl ;
    return 0;
}