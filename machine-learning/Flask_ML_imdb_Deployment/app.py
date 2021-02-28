from flask import Flask, render_template, request

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

import pickle as pkl

clf = pkl.load(open('./model.pkl', 'rb'))


@app.route('/', methods=['POST', 'GET'])
def hello_world():
    if request.method == 'POST':
        print("POST")
        text = str(request.form.get('message'))
        result = clf.predict([text])
        print("result ",result)
        return render_template("main.html", result=result[0])

    return render_template("main.html")


if __name__ == '__main__':
    app.run()
