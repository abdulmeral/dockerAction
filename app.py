from flask import Flask, render_template
app = Flask(__name__, template_folder='./template',static_folder='./template/screenshots')

@app.route("/")
def hello():
  return render_template("index.html")

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)