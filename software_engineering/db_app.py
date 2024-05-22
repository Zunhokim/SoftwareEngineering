from flask import Flask, render_template, request, make_response
import sqlite3 as sql

app = Flask(__name__)

@app.route('/')
def homepage():
  return render_template('index.html')

@app.route('/new')
def new_student():
  return render_template('new.html')

@app.route('/addrec', methods=['POST', 'GET'])
def addnew():
  if request.method == 'POST':
    try:
      nm = request.form['name']
      addr = request.form['addr']
      phone = request.form['phone']
      id = request.form['id']

      with sql.connect("student.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO students(name, addr, phone, id) VALUES(?, ?, ?, ?)", (nm, addr, phone, id))
        con.commit()
        msg = "Record successfully added"
    except:
      con.rollback()
      msg = "error in insert operation"
    finally:
      return render_template("result.html", msg = msg)
      con.close()

@app.route('/list')
def list():
  con = sql.connect("student.db")
  con.row_factory = sql.Row
  cur = con.cursor()
  cur.execute("SELECT * FROM students")
  rows = cur.fetchall();
  return render_template("list.html", rows = rows)

if __name__ == '__main__':
  app.run(debug=True)