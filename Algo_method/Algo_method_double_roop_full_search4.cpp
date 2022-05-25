#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <cmath>
#include <numeric>
#include <algorithm>
using namespace std;

int main() {
    string S;
    cin >> S;
    set<char> s;
    for (int i=0; i<S.size(); i++) {
        s.insert(S[i]);
    }
    cout << s.size() << endl;
    return 0;
}