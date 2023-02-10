score = 0
height = 1.8
isWinning = True

#f-String
print(f"Your score is {score}, your height is {height}, you are winning is {isWinning}")
print("Your score is", score, ", your height is", height, ", you are winning is", isWinning)
a = 4
a /= 2
print(a)

#파이썬 출력 방법

#기본 출력 방법
a, b, c = 1, 2, 3
print("a는:", a, "b는:",b , "c는:", c)
print("a는:" + str(a), "b는:" + str(b) , "c는:" + str(c))

#% operator 방식 (옛날 방식)
print("a: %d, b: %d, c: %d"%(a, b, c))

#str.foramt 방식 (파이썬 3.0 이상부터 지원)
print("a: {}, b: {}, c: {}".format(a, b, c))

#f-string 방식 (파이썬 3.6 이상부터 지원)
print(f"a: {a}, b: {b}, c: {c}")