import firebase_admin
from firebase_admin import credentials
from firebase_admin import db 

firebase_sdk = credentials.Certificate('C:/Users/Acer/Downloads/prueba-bf21e-firebase-adminsdk-mwdhi-1514b5a5cd.json')

firebase_admin.initialize_app(firebase_sdk,{'databaseURL':'https://prueba-bf21e-default-rtdb.firebaseio.com/'})
'''
# Crear una Coleccion con el Nombre de alguien
ref =db.reference('/Nombres')
ref.push({'Nombre':'Sergio','Apellido':'Espinosa','Edad':'21'})'''
'''
#Modificar un dato
ref = db.reference('/Nombres')
producto_ref = ref.child('-NFv_pnAXORpDzuJCAx6')
producto_ref.update({'Edad':'22'})'''
'''
#Agregar un producto mas
ref = db.reference('Nombres')
nombre = {'Nombre':'A','Apellido':'B','Edad':'20'}
nombre_ref= ref.push(nombre)'''