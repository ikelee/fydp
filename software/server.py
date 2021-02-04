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
    cur.execute('''SELECT * FROM sensor_raw_one''')
    rv = cur.fetchall()
    return str(list(map(lambda x: float(x[12]), list(rv))))

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
    cur.execute('''SELECT * FROM sensor_raw_one''')
    rv = cur.fetchall()
    x_accel_one=list(map(lambda x: float(x[1]), list(rv)))
    y_accel_one=list(map(lambda x: float(x[2]), list(rv)))
    z_accel_one=list(map(lambda x: float(x[3]), list(rv)))
    x_gyro=list(map(lambda x: float(x[4]), list(rv)))
    y_gyro=list(map(lambda x: float(x[5]), list(rv)))
    z_gyro=list(map(lambda x: float(x[6]), list(rv)))
    x_accel_two=list(map(lambda x: float(x[8]), list(rv)))
    y_accel_two=list(map(lambda x: float(x[9]), list(rv)))
    z_accel_two=list(map(lambda x: float(x[10]), list(rv)))
    timestamp=list(map(lambda x: float(x[11]), list(rv)))
    x_angular_accel=list(map(lambda x: float(x[12]), list(rv)))
    y_angular_accel=list(map(lambda x: float(x[13]), list(rv)))
    z_angular_accel=list(map(lambda x: float(x[14]), list(rv)))
    return render_template('line_chart.html', title='Current Head Data', labels=timestamp, values=[x_accel_one, y_accel_one, z_accel_one, x_gyro, y_gyro, z_gyro, x_accel_two, y_accel_two, z_accel_two, x_angular_accel, y_angular_accel, z_angular_accel])

if __name__ == '__main__':
    app.run(debug=True)