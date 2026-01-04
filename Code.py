from datetime import datetime as dt
import datetime


now22 = dt.now()
current_time  = now22.time()
formatted_time = now22.strftime("%H:%M")

print(formatted_time)