func read_Int_Array() -> [Int] {
    return readLine()!.split(separator :" ").map {Int($0)!}
}


let N_M : [Int] = read_Int_Array()
let N : Int = N_M[0]
let M : Int = N_M[1]
var U_V_Array :[(U:Int,V:Int)] = []
var U_V : [Int]

for _ in 0 ..< M {
    U_V = read_Int_Array()
    U_V_Array.append((U_V[0],U_V[1]))
}
U_V_Array.sort {$0 < $1}
print(U_V_Array)
