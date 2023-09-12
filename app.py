from flask import Flask
from flask import render_template, request, redirect, session
from flaskext.mysql import MySQL
from claseAulas import Aulas

app = Flask(__name__)

app.secret_key = "digitalforge"

# AGREGAR UN CONTROL DE TIEMPO DE LA SESION, (SOLO SI ES REQUERIDO)

mysql = MySQL()

app.config['MYSQL_DATABASE_HOST'] = 'db4free.net'
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_USER'] = 'usuario_adso02'
app.config['MYSQL_DATABASE_PASSWORD'] = 'S3n4+2023'
app.config['MYSQL_DATABASE_DB'] = 'instituto_03'

mysql.init_app(app)

conexion = mysql.connect()
cursor = conexion.cursor()

lasAulas = Aulas(mysql)

@app.route('/')
def index():
    resultado = lasAulas.consultaAulas()
    return render_template('index.html', resultados = resultado)


@app.route('/crearAula', methods = ['POST'])
def crearAula():
    _id = request.form['id']
    descripcion = request.form['descripcion']
    capacidad = request.form['capacidad']
    idEdificio = request.form ['idedificio']
    equipoAudioV = request.form['equipoAV']
    usuario = request.form['usuario']
    #borrado = request.form['password']

    lasAulas.agregarAula([_id, descripcion, capacidad, idEdificio, equipoAudioV, usuario])
    return redirect('/')

@app.route('/desactivarAula/<_id>')
def desactivarAula(_id):
        lasAulas.desactivarAula(_id)
        return redirect('/')

@app.route('/updateAula/<_id>', methods=['GET'])
def updateMedico(_id):
        resultado = lasAulas.actualizaAula(_id)
        return render_template('actualizaAula.html', resultados = resultado[0])

@app.route('/actualizarDatosAula', methods = ['POST'])
def updateDatos():
    id = request.form['id']
    descripcion = request.form['descripcion']
    capacidad = request.form['capacidad']
    idEdificio = request.form ['idedificio']
    equipoAudioV = request.form['equipoAV']
    usuario = request.form['usuario']

    lasAulas.actualizaDatosA([id, descripcion, capacidad, idEdificio, equipoAudioV, usuario])

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)


# TABLA aulas
#(('idAula', 'varchar(10)', 'NO', 'PRI', None, ''), ('descripcion', 'varchar(50)', 'NO', '', None, ''), ('capacidad', 'int', 'NO', '', None, ''), ('idEdificio', 'varchar(3)', 'NO', '', None, ''), ('equipoAudiovisual', 'tinyint(1)', 'NO', '', None, ''), ('usuario', 'varchar(12)', 'NO', '', None, ''), ('borrado', 'tinyint(1)', 'NO', '', None, ''))