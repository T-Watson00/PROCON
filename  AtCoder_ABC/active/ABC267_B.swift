import Foundation

main()

func main() {
    let S : [String] = Array(readLine()!).map {String($0)}
    if S[0] != "0" {
        print("No")
        exit(0)
    } else {
        let Pin_array : [String] = pin_stand(number_string : S)
        let Pin_string : String = Pin_array.joined(separator : "")
        if dictator(pin_string : Pin_string) {
            print("Yes")
        } else {
            print("No")
        }

    }

}

func read_Int_Array () -> [Int] {
    return readLine()!.split(separator : " " ).map {Int($0)!}
}

func pin_stand (number_string : [String]) -> [String] {
    var pin_array : [String] = ["1","1","1","1","1","1","1"]
    if number_string[6] == "0" {
        pin_array[0] = "0"
    }
    if number_string[3] == "0" {
        pin_array[1] = "0"
    }
    if number_string[1] == "0" && number_string[7] == "0" {
        pin_array[2] = "0"
    }
    if number_string[0] == "0" && number_string[4] == "0" {
        pin_array[3] = "0"
    }
    if number_string[2] == "0" && number_string[8] == "0" {
        pin_array[4] = "0"
    }
    if number_string[5] == "0" {
        pin_array[5] = "0"
    }
    if number_string[9] == "0" {
        pin_array[6] = "0"
    }
    return pin_array

}

func dictator (pin_string : String) -> Bool {
    let split_set : [String] = ["101","1001","10001","100001","1000001"]
    var flag : Bool = false
    for split_pair in split_set {
        if pin_string.contains(split_pair) {
            flag = true
            break
        }
    }
    return flag

}