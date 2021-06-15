from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
from openpyxl import load_workbook
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'bd_cargadatos'
Bootstrap(app)
mysql = MySQL(app)

@app.route('/')
def Index():    
    return render_template('index.html', listado = obtenerDatos())

@app.route('/cargar', methods=['POST'])
def Cargar():
    if request.method == 'POST':   
        # cursor =  mysql.connection.cursor()
        # cursor.execute("select * from datos")
        # datos = cursor.fetchall()

        # datos = obtenerDatos()
        #carga de archivo
        nombre_archivo = request.form['archivo']
        wb = load_workbook(nombre_archivo)

        #Hojas del libro
        sheets = wb.sheetnames
        for sheet in sheets:
            #Hoja activa
            sheetActive = wb[sheet]
            if sheet in wb.sheetnames and wb[sheet].max_column > 0 and wb[sheet].max_row > 0:                
                #Obtener la cantidad de Columnas
                cols = wb[sheet].max_column
                #Obtener la cantidad de Filas
                rows = wb[sheet].max_row
                # rows = 10
                print('La hoja tiene columnas',cols)
                print('La hoja tiene filas',rows)

                #Recorrer cada fila y obtener los datos de cada column
                for row in range(2, rows+1):
                    nombre= sheetActive.cell(row,1).value
                    apellido= sheetActive.cell(row,2).value
                    nacionalidad= sheetActive.cell(row,3).value
                    fechaContrato = sheetActive.cell(row,4).value
                    sexo = sheetActive.cell(row,5).value

                    cursor = mysql.connection.cursor()
                    cursor.execute('INSERT INTO datos(nombre, apellido, nacionalidad, fechaContrato, sexo) values(%s,%s,%s,%s,%s)', (nombre, apellido, nacionalidad, fechaContrato, sexo))
                    mysql.connection.commit()
                print('Carga Exitosa')
            else:
                print('No existen datos para cargar')
    return redirect(url_for('Index'))

def obtenerDatos():
    cursor =  mysql.connection.cursor()
    cursor.execute("SELECT * FROM datos")
    data = cursor.fetchall()
    return data

if __name__ == '__main__':
    app.run(port=3000, debug=True)