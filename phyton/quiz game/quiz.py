point = 0
print("welcome to quiz that made by agape tampan 77")
print("\nnote:if you answer with wrong spelling, you will get no point")

print("\nlets start with first question")
pertanyaan1 = input("who is the founder of america continent? ")
if pertanyaan1.lower() == "christoper colombus":
  print("+1 point you are great at this")
  point=+1 
else:
  print("get lucky next time! +0")

print("\nsecond question")
print("note: use st nd rd or th after the date")
pertanyaan2 = input("when did kurt cobain die? ")
if pertanyaan2.lower() == "april 5th 1994" or pertanyaan2 == "5th april 1994":
  print("+1 goodjob you are making your parent proud")
  point=+1 
else:
  print("get lucky next time! +0")

print("\nthird question")
pertanyaan3 = input("who is the first black skinned president in america? ")
if pertanyaan3.lower() == "barack obama":
  print("+1 some dangerous question eh?")
  point=+1 
else:
  print("get lucky next time! +0")

print("\nfourth question")
print("note: use st nd rd or th after the date")
pertanyaan4 = input("when did world war 2 started? ")
if pertanyaan4.lower() == "1st September 1939" or pertanyaan4 == "september 1st 1939":
  print("+1 some history question eh?")
  point=+1 
else:
  print("get lucky next time! +0")

print("\nfifth question")
pertanyaan4 = input("who is the richest person in the world in 2024? ")
if pertanyaan4.lower() == "elon musk":
  print("+1 good job")
  point=+1 
else:
  print("get lucky next time! +0")

ha = point * 20
print("your score is", ha)
print("thank you for playing this quiz")