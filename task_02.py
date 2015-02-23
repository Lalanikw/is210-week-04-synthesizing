#!/user/bin/env python
# _*_ coding: utf-8 _*_
"""if study."""
print "What day is it? "

dy = raw_input()
dy = dy.lower()
print "What time is it?"
time = raw_input()
if (dy == "sat" or dy == "saturday" or dy == "sun" or dy == "sunday" or dy < 600):
    SNOOZE = True
else:
    SNOOZE = False
if SNOOZE != True:
print "BEEP! BEEP! BEEP! BEEP! BEEP!"
