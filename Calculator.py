from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def fun():
    return render_template('Cal.html')

app.run(debug=True,port=4893)
