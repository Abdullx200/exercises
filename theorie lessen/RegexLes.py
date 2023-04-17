#deze les hebben we geleerd over Regex, Regex is een manier om dingen te zoeken
#exact zoals ctr+f

#Het kan gebruikt worden met 
import re
#Er zijn verschillende functies:
"match, search, findall, sub, fullmatch"
#het gebruik is volgens de synatx hieronder
"""
[]	A set of characters	"[a-m]"	
\	Signals a special sequence (can also be used to escape special characters)	"\d"	
.	Any character (except newline character)	"he..o"	
^	Starts with	"^hello"	
$	Ends with	"planet$"	
*	Zero or more occurrences	"he.*o"	
+	One or more occurrences	"he.+o"	
?	Zero or one occurrences	"he.?o"	
{}	Exactly the specified number of occurrences	"he.{2}o"	
|	Either or	"falls|stays"	
()	Capture and group	 
"""

#in funcites kan dit gebruikt worden met een if FUNCTIE: ; print(FUNCTIE.group())
#zo wordt de gevonden woord terug gegeven

#als je in de functie de synatx in twee of meer groepen verdeeld met () moet je bij .group(nummmer van groep)

#SUB is anders, het vervangt de gevonden woord met de volgende word die na komt (met comma)

#algemeen gebruik; object= re.search("SYNTAX", WAAR ZOEKEN)