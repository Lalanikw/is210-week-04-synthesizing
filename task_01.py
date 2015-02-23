#!/user/bin/env python
# -*- coding: utf-8 _*_
"""if study."""
print "Which base color, Seattle Gray or Manatee?"
inp = raw_input()
if( inp == "Seattle Gray"):
    BASE = inp
    print "Which accent color,  Ceramic Glaze or Manatee?"
    inp = raw_input()
    if( inp == "Ceramic Glaze"):
        ACCENT = inp
        print "Which highlight color,  Basically White or white?"
        inp = raw_input()
        if( inp == "Basically White"):
            HIGHLIGHT = inp        
        elif(inp =="WHITE):
            HIGHLIGHT = inp
        else:
             print "Error color is not recognized"
             return
    elif(inp ==" Cumulus Nimbus):
         ACCENT = inp
    else:
         print "Error color is not recognized"
         return
elif( inp == "Manatee"):
    BASE = inp
else:
    print "Error color is not recognized"
elif( inp == "Manatee"):
    BASE = inp
else:
    print "Error color is not recognized"
    return
print "Your selected colors are, %s, %s, and %s".format(BASE,ACCENT,HIGHLIGHT)
