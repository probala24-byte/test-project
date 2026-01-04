from datetime import datetime as dt
import datetime


now = dt.now()
current_time  = now.time()
formatted_time = now.strftime("%H:%M")

print(formatted_time)