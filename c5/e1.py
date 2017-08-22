import time
t=time.time() #total seconds
seconds=t%60
t=t//60 #total minutes
minutes=t%60
t=t//60 #total hours
hours=t%24
t=t//24 #total days
days=t
print(days,"days",hours,"h",minutes,"m",seconds,"s")
