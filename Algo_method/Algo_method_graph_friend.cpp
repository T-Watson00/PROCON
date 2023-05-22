#include <iostream>
#include <string>
#include <vector>

using std::cin;
using std::cout;
using std::endl;


int main() {
    int N,A,B ;
    cin >> N >> A >> B ;
    std::vector<std::string> friend_or_not(N);
    std::string A_friend;
    for (int i=0;i<N;i++) {
        cin >> friend_or_not[i];
        if (i == A) {
            A_friend = friend_or_not[i];
        }
    }

    char  Yes_sign = 'o';
    if (A_friend[B] == Yes_sign){
        cout << "Yes" << endl;
    }
    else {
        cout << "No" << endl;
    }


    return 0;
}