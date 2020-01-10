from flask import Flask,render_template
app = Flask(__name__)
print(__name__)

@app.route('/<namename>/<int:post_id>')
def hello_world(namename= None,post_id = None):
    # return "Hello World, I am Mohammed Elmala"
    return render_template("index.html",name=namename)



