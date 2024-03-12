courses = {
    'python':{'name':'python','fee':2000,'duration':'2 month'},
    'c++':{'name':'c++','fee':3000,'duration':'3 month'},
    'javascript':{'name':'javascript','fee':4000,'duration':'5 month'},
    'java':{'name':'java','fee':4000,'duration':'5 month'},
    'kottlin':{'name':'kottlin','fee':4000,'duration':'5 month'},
    'php':{'name':'php','fee':4000,'duration':'5 month'},
    'html':{'name':'html','fee':4000,'duration':'5 month'}
}

print("courses\n")
for key in courses:
    print(courses[key]['name'],"\n")

courses['java']['fee'] = 9000

print("\nafter changing java fee to $9000:\n")
print(courses['java'])

