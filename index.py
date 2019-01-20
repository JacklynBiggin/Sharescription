#!C:\Users\Jerry\AppData\Local\Programs\Python\Python37-32\python.exe
print("Content-Type: text/html")
print()
print ("""
<TITLE>CGI script ! Python</TITLE>
<H1>This is my first CGI script</H1>
""")
print("WHYYYYY")

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def main():
	# Put Facebook login here
    print ("""Hello""")
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug = True)
 
