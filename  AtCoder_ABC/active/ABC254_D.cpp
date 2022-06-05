#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <numeric>
#include <algorithm>
using namespace std;

bool is_squere(long long N) {
    long long r = (long long)floor(sqrt((long double)N));  // 切り捨てした平方根
    return (r * r) == N;
}

int main() {
    long long N ;
    cin >> N ;
    int count = N;
    for (int i = 1 ; i <= N ; i++) {
        for (int j = i+1 ; j <= N ; j++) {
            long long ij = i*j ;
            if(is_squere(ij)) {
                count = count + 2;
            }
        }
    }
    cout << count << endl ;


    return 0 ;
}