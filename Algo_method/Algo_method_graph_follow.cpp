#include <iostream>
#include <vector>
#include <tuple>
#include <algorithm>

using std::cin;
using std::cout;
using std::endl;



int main() {
    int N,M ;
    cin >> N >> M;
    std::vector<std::tuple<int,int>> follow_arrow(M);
    for (int i=0;i<M;i++) cin >> std::get<0>(follow_arrow[i]) >> std::get<1>(follow_arrow[i]);
    std::sort(follow_arrow.begin(),follow_arrow.end());
    int turtle = 0;
    for (int i=0;i<M;i++) {
        while (turtle != std::get<0>(follow_arrow[i])) {
            turtle++;
            cout << endl ;
        }
        cout << std::get<1>(follow_arrow[i]) << "  ";
    }


    return 0;
}