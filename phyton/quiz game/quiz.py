point = 0
print("welcome to quiz that made by agape tampan 77")
print("\nnote:if you answer with wrong spelling, you will get no point")

print("lets start with first question")
pertanyaan1 = input("who is the founder of america continent? ")
if pertanyaan1.lower() == "christoper colombus":
  print(point + 1 ,"+1 point you are great at this")
else:
  print("get lucky next time! +0")

print("\nsecond question")
print("\nnote: use st nd rd or th after the date")
pertanyaan2 = input("when did kurt cobain die? ")
if pertanyaan2.lower() == "april 5th 1994" or pertanyaan2 == "5th april 1994":
  print(point + 1 ,"+1 goodjob you are making your parent proud")
else:
  print("get lucky next time! +0")

print("third question")
pertanyaan3 = input("who is the first black skinned president in america? ")
if pertanyaan3.lower() == "barack obama":
  print(point + 1 ,"+1 some dangerous question eh?")
else:
  print("get lucky next time! +0")

print("fourth question")
print("\nnote: use st nd rd or th after the date")
pertanyaan4 = input("when did world war 2 started? ")
if pertanyaan4.lower() == "1st September 1939" or pertanyaan4 == "september 1st 1939":
  print(point + 1 ,"+1 some history question eh?")
else:
  print("get lucky next time! +0")

print("fifth question")
pertanyaan4 = input("who is the richest person in the world in 2024? ")
if pertanyaan4.lower() == "elon musk":
  print(point + 1 ,"+1 some dangerous question eh?")
else:
  print("get lucky next time! +0")

print("your point is", point * 20)
print("thank you for playing this quiz")