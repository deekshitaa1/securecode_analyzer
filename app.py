
from flask import Flask, request, render_template_string
from scanner import run_scan

app = Flask(__name__)

UPLOAD_FORM = '''
<h2>SecureCode Analyzer</h2>
<form method="POST" enctype="multipart/form-data">
  <input type="file" name="codefile" />
  <button type="submit">Scan</button>
</form>
'''

@app.route("/", methods=["GET","POST"])
def home():
    if request.method == "POST":
        f = request.files["codefile"]
        code = f.read().decode("utf-8")
        results = run_scan(code)
        return {"results": results}
    return render_template_string(UPLOAD_FORM)

if __name__ == "__main__":
    app.run(debug=True)
