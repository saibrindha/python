fObj = open('C:\\Users\\Dell\\Downloads\\Day3\\Day3\\funTwo.py','r')
number_of_lines = 0
number_of_words = 0
number_of_characters = 0
for line in fObj:
  line = line.strip("\n")


  words = line.split()
  number_of_lines += 1
  number_of_words += len(words)
  number_of_characters += len(line)

fObj.close()

print("lines:", number_of_lines, "words:", number_of_words, "characters:", number_of_characters) 
print(f'filename--> {fObj}')