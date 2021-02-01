from flask import Flask, Markup, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'IMPACT'

mysql = MySQL(app)

labels = [
    'JAN', 'FEB', 'MAR', 'APR',
    'MAY', 'JUN', 'JUL', 'AUG',
    'SEP', 'OCT', 'NOV', 'DEC'
]

values = [
    967.67, 1190.89, 1079.75, 1349.19,
    2328.91, 2504.28, 2873.83, 4764.87,
    4349.29, 6458.30, 9907, 16297
]

colors = [
    "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
    "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
    "#C71585", "#FF4500", "#FEDCBA", "#46BFBD"]

@app.route('/')
def main():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT round(x_accel_one, 5) FROM sensor_raw''')
    rv = cur.fetchall()
    return str(rv)

@app.route('/bar')
def bar():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT round(x_accel_one, 5) FROM sensor_raw''')
    rv = cur.fetchall()
    bar_values=list(map(lambda x: float(x[0]), list(rv)))
    bar_labels=["" for _ in range(len(bar_values))]
    return render_template('bar_chart.html', title='Bitcoin Monthly Price in USD', max=max(bar_values), min=min(bar_values), labels=bar_labels, values=bar_values)

@app.route('/line')
def line():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT round(x_accel_one, 3) FROM sensor_raw''')
    rv = cur.fetchall()
    line_values=list(map(lambda x: float(x[0]), list(rv)))
    line_labels=["" for _ in range(len(line_values))]
    return render_template('line_chart.html', title='Current Head Data', max=max(line_values), min=min(line_values), labels=line_labels, values=line_values)

if __name__ == '__main__':
    app.run(debug=True)