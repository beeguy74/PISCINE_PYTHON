from datetime import datetime as dt

time = dt.now()
secs = time.timestamp()
print(
    f"Seconds since January 1, 1970: {secs:,.4f} or {secs:.2e}" +
      " in scientific notation\n" +
      time.strftime("%b %-d %Y")
    )
