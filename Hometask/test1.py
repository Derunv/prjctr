start_string = "SnakeCaseText"
end_string =  ''
a = 0
while len(start_string) > a:
    if start_string[a].isupper() and a == 0:
        print(start_string[a].lower())
  #      end_string = end_string[a].lower
   # elif start_string[a].isupper():
   #     end_string = '_' + end_string[a].lower
   # else:
    #    end_string = end_string + start_string[a]

    a += 1
print(end_string)