from flask import Flask, render_template, jsonify

app = Flask(__name__)

DEPTS = [
  {
    'id' : 'ushering',
    'salary':'#10,000',
    'work_type':'physical',
    'branch':'umuariaga',
  },

  {
    'id' : 'sanitation',
    'salary':'#10,000',
    'work_type':'physical',
    'branch':'bende_road',
  },
  {
    'id' : 'music',
    'work_type':'remote',
    'branch':'umuariaga',
  },
  {
    'id' : 'transport',
    'salary':'#10,000',
    'work_type':'physical',
    'branch':'umuariaga',
  },
  {
    'id' : 'finance',
    'work_type':'remote',
    'branch':'bende_road',
  },
]

@app.route("/")
def hello_world():
  return render_template("home.html",
                        church_name="HOSA INT'L SUNDAY SCH", depts=DEPTS)
@app.route("/api/depts")
def dept_list():
    return jsonify(DEPTS)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)