# import keyword
# print(keyword.kwlist,end="\n")
import keyword

print("Python Keywords:")
for kw in keyword.kwlist:
    print("-", kw)
# Print total number of keywords
print("\nTotal number of keywords:", len(keyword.kwlist))