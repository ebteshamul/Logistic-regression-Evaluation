from flask import Flask, render_template, request
import pickle

app = Flask(__name__, template_folder="template")
model1 = pickle.load(open("gender_classi.pkl",  "rb"))
@app.route("/home")
def home():
	return render_template("index.html")

@app.route("/predict",  methods=['POST', 'GET'])
def prewd():
	forhead_cm = float(request.form.get("width"))
	pred = model1.predict([[forhead_cm]])

	return render_template("index.html", result= pred)



if __name__ =="__main__":
	app.run(debug=True)