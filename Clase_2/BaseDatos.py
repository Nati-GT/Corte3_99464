import sqlite3

def Registrar(Id, Documento, Nombre, Apellido, Edad):
    db=sqlite3.connect("BaseDeDatos.s3db")
    db.row_factory= sqlite3.Row
    cursor=db.cursor()
    consulta= "inserte datos de usuario (Id, Documento, Nombre, Apellido, Edad) con los valores ('"+ nombre +"','"+ apellido + "','" + str (edad)+")"
