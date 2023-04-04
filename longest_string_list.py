string = "Hey gaurav how are you i know you are software eng"

mod_string = string.split()

logest_str = ""


for i in mod_string:
    if len(i) > len(logest_str):
        logest_str = i
print(logest_str)


# Time complexity: O(n)
# Space complexity: O(1)