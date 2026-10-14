from flask import Flask, render_template, jsonify, send_file
from pathlib import Path
import json, csv, io, os

BASE_DIR = Path(__file__).resolve().parent
app = Flask(__name__)
with (BASE_DIR / "data" / "data.json").open(encoding="utf-8") as f:
    DATA = json.load(f)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/data")
def api_data():
    return jsonify(DATA)

@app.route("/download/csv")
def download_csv():
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(DATA["columns"])
    writer.writerows(DATA["data"])
    mem = io.BytesIO(output.getvalue().encode("utf-8-sig"))
    mem.seek(0)
    return send_file(mem, mimetype="text/csv", as_attachment=True,
                     download_name="data_deskriptif.csv")

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "5000")), debug=False)
