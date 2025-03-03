import re

string = "123b456abcg1234ababcccvfg35hu45hudbfgh23789"
pattern_obj = re.compile(r"abc")
# pattern_obj = re.compile(r"[a-d]")

# match_finder = pattern_obj.finditer(string)
# match_finder = pattern_obj.search(string)
# match_finder = pattern_obj.split(string)
match_finder = pattern_obj.sub(' hi ',string)

# for matching in match_finder:
#     print(matching)
print(match_finder)

print("git started")