from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def loadmain():
	return render_template("index.html")
	
@app.route("/",methods = ['POST'])
def respond():
	num1 = request.form['num1']
	num2 = request.form['num2']
	return "Thank u" + num1 + num2
	
if __name__=='__main__':
	app.run()
