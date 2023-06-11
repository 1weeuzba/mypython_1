a ="Stroke on my, lick on my, suck on my cock"
b ="It's the first time for you, so here's what you do"
c="Unzip me, and strip me, and show me you care"
d="Don't go rippin' out my pubic hair"
e="Reach for my, grab for my, pull out my cock"
f="You can do it with ease, just get on your knees"
g="Start licking and slurping, my dick will get firm"
h="Soon you'll be tasting sperm"
i_="Do it right now, and don't bite now"
j="Drag your tongue across my meat"

try:
   for i in range(1,10+1,1):
      with open(f"C:\\Users\\(user)\\Desktop\\random_text_files\\text_{i}.txt","w") as file:
         if i == 1:
            file.write(a)
         elif i == 2:
            file.write(b)
         elif i==3:
            file.write(c)
         elif i== 4:
            file.write(d)
         elif i== 5:
            file.write(e)
         elif i== 6:
            file.write(f)
         elif i== 7:
            file.write(g)
         elif i== 8:
            file.write(h)
         elif i== 9:
            file.write(i_)
         elif i== 10:
            file.write(j)
except PermissionError:
   print("Dumb ahh computer")
