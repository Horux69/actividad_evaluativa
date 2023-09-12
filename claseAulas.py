class Aulas:
    def __init__(self, miBD):
        self.mysql = miBD
        self.conexion = self.mysql.connect()
        self.cursor = self.conexion.cursor()


    def consultaAulas(self):
        sql = "SELECT * FROM aulas WHERE borrado = 1"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        self.conexion.commit()
        return resultado
    
    def agregarAula(self, aula):

        borrado = 1

        sql = f"INSERT INTO aulas (idAula, descripcion, capacidad, idEdificio, equipoAudiovisual, usuario, borrado) VALUES ('{aula[0]}', '{aula[1]}', '{aula[2]}', '{aula[3]}', '{aula[4]}', '{aula[5]}', '{borrado}')"
        self.cursor.execute(sql)
        self.conexion.commit()

    def desactivarAula(self, _id):
        sql = f"UPDATE `aulas` SET `borrado`= 0 WHERE `idAula` = '{_id}'"
        self.cursor.execute(sql)
        self.conexion.commit()

    def actualizaAula(self, _id):
        consulta = f"SELECT * FROM aulas WHERE idAula = '{_id}'"
        self.cursor.execute(consulta)
        resultado = self.cursor.fetchall()
        self.conexion.commit()
        return resultado
    
    def actualizaDatosA(self, aula):
        consulta = f"UPDATE aulas SET descripcion = '{aula[1]}', capacidad = '{aula[2]}', idEdificio = '{aula[3]}', equipoAudiovisual = '{aula[4]}', usuario = '{aula[5]}' WHERE idAula = '{aula[0]}'"
        self.cursor.execute(consulta)
        self.conexion.commit()