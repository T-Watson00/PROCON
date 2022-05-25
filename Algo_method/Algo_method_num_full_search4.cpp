#include<iostream>
#include<cmath>
#include<string>
#include<vector>
#include<numeric>
using namespace std;

int gcd(int a, int b) {
    if (b==0) return a;
    else return gcd(b, a%b);
}

int main() {
    int A,B ;
    cin >> A >> B ;
    int ans ;
    ans = gcd(A,B);
    cout << ans << endl;
    return 0;
}