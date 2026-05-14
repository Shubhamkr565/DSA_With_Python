def timeConversion(s):
    period = s[-2:]       # AM or PM
    hh = int(s[:2])       # Hour
    mm_ss = s[2:-2]       # :MM:SS

    if period == "AM":
        if hh == 12:
            hh = 0
    else:  # PM
        if hh != 12:
            hh += 12

    return "{:02d}{}".format(hh, mm_ss)

# Example usage
print(timeConversion("07:05:45PM"))  # Output: 19:05:45
print(timeConversion("12:01:00AM"))  # Output: 00:01:00
