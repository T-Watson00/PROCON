let Year : Int = Int(readLine()!)!
let Next_World_Cup : Int = ((6 - (Year % 4)) % 4) + Year
print(Next_World_Cup)