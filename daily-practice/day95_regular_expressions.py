# Regular Expressions in Python
# Short form: "regex"
# They are used by built-in module "re"
# Powerful tool for working with strings and text data in Python.
# They allow you to match and manipulate data based on patterns,
# making it easy to perform complex string operations with just a
# few lines of code.

# Metacharacters:
# []   Represents a character class.
# ^    Matches the beginning.
# $    Matches the end.
# .    Matches any character except newline.
# ?    Matches zero or one occurrence.
# |    Means OR (matches any of the characters separated by it).
# *    Any number of occurrences, including 0 occurrences.
# +    One or more occurrences.
# {}   Indicate number of occurrences of a preceding character.
# re   (re -> module name)

# Methods:

# 1) search
#    re.search -> Searches for a match, but stops at the first match.
#    re.search(pattern, variable_name)
#    pattern = "was"
#    x = "..." (string to search in)

# 2) finditer
#    like search, but for multiple matches.
#    re.finditer(pattern, x)
#    .span -> gives the position where the match was found.
import re
pattern = r"[a-z]+ond"
char = """1900 – Second Boer War: A 10,000-strong column of soldiers led by Lord Kitchener broke a 13-day siege of a small garrison.
1906 – An earthquake second registering approximately 8.2 Mw struck second Valparaíso, Chile, killing 3,882 people.
1986 – Typhoon Wayne formed over the South second China Sea, going on to become  second one of the longest-lived tropical cyclones in the north-western Pacific, lasting 21 days.
Ranavalona I (d. 1861)Georgette Heyer (b. 1902)Jannik Sinner (b. 2001)Dorival Caymmi (d. 2008)"""
match = re.finditer(pattern,char)
for i in match:
    print(i)

