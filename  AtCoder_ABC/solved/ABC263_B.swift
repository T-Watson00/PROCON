func read_Int_Array() -> [Int] {
    return readLine()!.split(separator : " ").map{Int($0)!}
}
let N : Int = Int(readLine()!)!
var count : Int = 1
let people : [Int] = read_Int_Array()
var index : Int = N - 2
while people[index] > 1 {
    index = people[index] - 2
    count += 1
}
print(count)
