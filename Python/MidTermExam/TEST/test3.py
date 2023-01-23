course = [ "Python", "Javascript", "C++", "__reserved__" ]
print(course)

course[3] = "Go"
print(course)

print(course[1].upper())

newStr = course[1] + " language"
print(newStr)

print(len(course))
print(max(course))
print(min(course))
print(sorted(course))
print(sorted(course, reverse=True))

requestedCourse = [ "HTML5", "CSS3" ]
newCourse = course + requestedCourse
print(newCourse)