#!/usr/bin/python

# The Mayan Long Count[2] calendar is a counting of days with these units: "* 
# The Maya name for a day was k'in. Twenty of these k'ins are known as a winal 
# or uinal. Eighteen winals make one tun. Twenty tuns are known as a k'atun. 
# Twenty k'atuns make a b'ak'tun.*". Essentially, we have this pattern:
# 1 kin = 1 day
# 1 uinal = 20 kin
# 1 tun = 18 uinal
# 1 katun = 20 tun
# 1 baktun = 20 katun
# The long count date format follows the number of each type, from longest-to-shortest time 
# measurement, separated by dots. As an example, '12.17.16.7.5' means 12 baktun
# , 17 katun, 16 tun, 7 uinal, and 5 kin. This is also the date that 
# corresponds to January 1st, 1970. Another example would be December 21st, 2012
# : '13.0.0.0.0'. This date is completely valid, though shown here as an 
# example of a "roll-over" date.
# Write a function that accepts a year, month, and day and returns the Mayan 
# Long Count corresponding to that date. You must remember to take into account 
# leap-year logic, but only have to convert dates after the 1st of January, 1970
# .
# Author: skeeto
# 

import datetime

utc = datetime.date(1970,1,1)
kin = 1
uinal = 20 * kin
tun = 18 * uinal
katun = 20 * tun
baktun = 20 * katun
days_utc = 12 * baktun + 17 *katun + 16*tun + 7*uinal + 5* kin

def convert_to_myan(date):
  delta = date - utc
  days = delta.days + days_utc
  mayan_long_count = []
  for m in [baktun,katun,tun,uinal,kin]:
    (l,days) = divmod(days,m)
    mayan_long_count.append(str(l))
  return ".".join(mayan_long_count)

def mayan_to_date(mayan):
  mayan_long_count = mayan.split(".")
  days = 0
  for (m,b) in zip(mayan_long_count,[baktun,katun,tun,uinal,kin]):
    days += (int(m) * b)
  days -= days_utc
  return str(datetime.timedelta(days=days) + utc)

def main():
  num_dates = int(raw_input())
  dates = []
  for d in range(num_dates):
    inp = raw_input().split()
    (day,month,year) = (int(x) for x in inp)
    dates.append(datetime.date(year,month,day))

  for date in dates:
    print convert_to_myan(date)
  print mayan_to_date("14.0.0.0.0")
if __name__ == "__main__":
  main()
