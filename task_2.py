#  данная программа проверяет истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
print('x y z')
for x in range(0,2):
   for y in range(0,2):
      for z in range(0,2):
         a = not(x or y or z) == (not(x) and not(y) and not(z))
         print(x, y, z, a)
            