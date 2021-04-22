import cgitb
import cgi
cgitb.enable()
#!/usr/bin/env python3

form = cgi.FieldStorage()
print("Content-type: text/html")
print()
print("<h1>Hello world!</h1>")
print("Починяю примус")