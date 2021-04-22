#!/usr/bin/python

import cgitb, cgi
cgitb.enable()
#!/usr/bin/env python3

data = cgi.FieldStorage()

print("Content-Type: text/html")
print(data)