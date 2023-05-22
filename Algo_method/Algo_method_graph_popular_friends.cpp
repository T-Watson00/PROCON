#include <iostream>
#include <tuple>
#include <vector>

using std::cin;
using std::cout;
using std::endl;

struct sort_by_size {
    bool operator() (const std::tuple<int,std::vector<int>>& a,const std::tuple<int,std::vector<int>>& b) const noexcept {
        return std::tie(std::get<1>(a).size(),-std::get<0>(a)) > std::tie(std::get<1>(b).size(),-std::get<0>(b))
    }
}

int main() {
    int N,M ;
    cin >> N >> M;
    std::vector<std::tuple<<int,std::vector<int>>> friends_vector(M);
    int A,B ;
    for (int i=0;i<M;i++) {
        std::get<0>(friends_vector[i]) = i;
        cin >> A >> B ;
        std::get<1>(friends_vector[A]).emplace_back(B);
        std::get<1>(friends_vector[B]).emplace_back(A);
    }
    std::sort(friends_vector.begin(),friends_vector.end(),sort_by_size{});
    std::sort(std::get<1>(friends_vector.back()).begin(),std::get<1>(friends_vector.back()).end())
    for (int i=0;i<std::get<1>(friends_vector.back()).size();i++) {
        cout << std::get<1>(friends_vector.back())[i] << " ";
    }
    cout << endl;
    return 0;
}