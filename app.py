from flask import Flask, render_template, request

import similarity

app = Flask(__name__)

@app.route("/" ,methods =['POST'])
def hello(): 
    if request.method == "POST":
        text1 = request.form.get("text1")
        text2 = request.form.get("text2")
        sim = similarity.similarity(text1,text2)
        
    return render_template("index.html",prediction=sim)


if __name__ == "__main__":
    app.run(debug=True)


