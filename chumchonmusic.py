from flask import Flask, render_template, request, redirect, url_for
import pymysql

app = Flask(__name__)
conn = pymysql.connect('localhost', 'root', '','musicschool')

@app.route("/")
def showData():
        return render_template('index.html')

@app.route("/teacher")
def showteacher():
    with conn:
        cur = conn.cursor()
        cur.execute("select * from teacher")
        rows = cur.fetchall()
        return render_template('teacher.html', datas = rows)

@app.route("/student")
def showstudent():
    with conn:
        cur = conn.cursor()
        cur.execute("select * from student")
        rows = cur.fetchall()
        return render_template('student.html', datas = rows)

@app.route("/addteacher")
def showFromteacher():
        return render_template('addteacher.html')

@app.route("/addstudent")
def showFromstudent():
        return render_template('addstudent.html')

@app.route("/insert", methods=['POST'])
def insert():
    if request.method == "POST":
        Firstname = request.form['Firstname']
        Lastname = request.form['Lastname']
        Nickname = request.form['Nickname']
        Birthday = request.form['Birthday']
        Email = request.form['Email']
        TelNum = request.form['TelNum']
        LineId = request.form['LineId']
        Image = request.form['Image']
        with conn.cursor() as cursor:
            sql = "Insert into 'teacher' ('Firstname', 'Lastname', 'Nickname', 'Birthday', 'Email', 'TelNum', 'LineId', 'Image') values(%s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (Firstname, Lastname, Nickname, Birthday, Email, TelNum, LineId, Image))
            conn.commit()
        return redirect(url_for('showData'))

if __name__ == "__main__":
    app.run(debug=True)