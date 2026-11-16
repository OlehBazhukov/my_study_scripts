count = 0
a = 0
for i in range(1, 11):
      a = a + 1
      for j in range(1,11):
            print(j * a, end=" ")
            count += 1
            if count == 10:
                  print(end="\n")
                  count = 0
