from flask import Flask, render_template, request, g, redirect, url_for, jsonify
from db import coll
app = Flask(__name__)
@app.route('/')
def addInfo():
    return render_template('main.html')

@app.route('/seeInfo', methods=['GET'])
def seeInfo():
    coll = cluster.find({})
    print(info)
    return render_template("info.html",info=info)
@app.route('/postInfo', methods=['POST'])
def newInfo():
    name = request.form.get("name", "unnamed")
    email = request.form.get("email", "none")
    coll.insert_one({"name": name, "email": email})
    
    return redirect(url_for('seeInfo'))

@app.route('/deleteBob')
def deleteBob():
    coll.delete_many({"name": "Bob Saget"})

    return redirect(url_for('seeInfo'))


@app.route("/test")
def test():
    coll.insert_one({"name": "HANNJNNNK"})
    return "Connected to the data base!"
if __name__ == '__main__':
    app.run(port=8000)
