func read_Ints_Array() -> [Int] {
    return readLine()!.split(separator:" ").map {Int($0)!}
}

var Cards : [Int] = read_Ints_Array()
Cards.sort {$0 < $1}
if Cards[0] == Cards[1] && Cards[1] == Cards[2] && Cards[2] != Cards[3] && Cards[3] == Cards[4]{
    print("Yes")
} else if Cards[0] == Cards[1] && Cards[1] != Cards[2] && Cards[2] == Cards[3] && Cards[3] == Cards[4]{
    print("Yes")
} else {
    print("No")
}



