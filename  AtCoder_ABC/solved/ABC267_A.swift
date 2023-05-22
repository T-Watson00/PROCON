
let Input : String = readLine()!
let Week : [String] = ["Monday","Tuesday","Wednesday","Thursday","Friday"]
let Today : Int = Week.firstIndex(where: {$0 == Input})!
let Left_day : Int = 5 - Today
print(Left_day)