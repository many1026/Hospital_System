#%%
import pickle
import random
from datetime import datetime
import pandas as pd


lista_pacientes = []
lista_medicamentos = []
lista_padecimientos = []
lista_doctores = []
lista_historiales = []


class Persona:
    def __init__(self, nombre, fecha_nacimiento, rfc, telefono, email):
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.rfc = rfc
        self.telefono = telefono
        self.email = email

class Doctor(Persona):
    def __init__(self, nombre, fecha_nacimiento, rfc, telefono, email, especialidad, cedula):
        super().__init__(nombre, fecha_nacimiento, rfc, telefono, email)
        self.especialidad = especialidad
        self.cedula = cedula

    def atender_paciente(self, paciente):
        # Lógica para atender al paciente
        pass

class Paciente(Persona):
    def __init__(self, nombre, fecha_nacimiento, rfc, telefono, email, genero, edad, peso, grupo_sanguineo):
        super().__init__(nombre, fecha_nacimiento, rfc, telefono, email)
        self.genero = genero
        self.edad = edad
        self.peso = peso
        self.grupo_sanguineo = grupo_sanguineo

    def ser_atendido_por(self, doctor):
        # Lógica para ser atendido por un doctor
        pass

class Medicamento:
    def __init__(self, nombre, laboratorio, composicion, via_administracion, dosis, lote, fecha_caducidad):
        self.nombre = nombre
        self.laboratorio = laboratorio
        self.composicion = composicion
        self.via_administracion = via_administracion
        self.dosis = dosis
        self.lote = lote
        self.fecha_caducidad = fecha_caducidad

class Padecimiento:
    def __init__(self, nombre, descripcion, causas, tratamiento):
        self.nombre = nombre
        self.descripcion = descripcion
        self.causas = causas
        self.tratamiento = tratamiento
##PARA LOS PADECIMIENTOS
class HistorialMedico:
    def __init__(self, paciente, padecimiento):
        self.folio = str(random.randint(10000, 99999))  # Genera un folio aleatorio de 5 dígitos
        self.paciente = paciente
        self.padecimiento = padecimiento
        self.signos_vitales = {}  # Inicialmente vacío

    def agregar_signo_vital(self, clave, valor):
        self.signos_vitales[clave] = valor


def guardar_datos_historial(historiales, archivo):
    with open(archivo, 'wb') as archivo_guardar:
        pickle.dump(historiales, archivo_guardar)

def cargar_datos_historial(archivo):
    try:
        with open(archivo, 'rb') as archivo_cargar:
            return pickle.load(archivo_cargar)
    except FileNotFoundError:
        return []



# Función para dar de baja un padecimiento por nombre
def baja_padecimiento(lista_padecimientos, nombre_padecimiento):
    lista_padecimientos = [pad for pad in lista_padecimientos if pad.nombre != nombre_padecimiento]

# Función para modificar un padecimiento existente por nombre
def cambio_padecimiento(lista_padecimientos, nombre_padecimiento, nuevos_datos):
    for pad in lista_padecimientos:
        if pad.nombre == nombre_padecimiento:
            # Aquí puedes actualizar los atributos del padecimiento según los nuevos datos
            pad.nombre = nuevos_datos['nombre']
            pad.descripcion = nuevos_datos['descripcion']
            pad.causas = nuevos_datos['causas']
            pad.tratamiento = nuevos_datos['tratamiento']

# Función para guardar datos de padecimientos en un archivo
def guardar_datos_padecimientos(lista_padecimientos, archivo):
    with open(archivo, 'w') as file:
        for padecimiento in lista_padecimientos:
            # Aquí debes escribir cada atributo del padecimiento en una línea del archivo
            linea = f"{padecimiento.nombre},{padecimiento.descripcion},{padecimiento.causas},{padecimiento.tratamiento}\n"
            file.write(linea)

# Función para cargar datos de padecimientos desde un archivo
def cargar_datos_padecimientos(archivo):
    lista_padecimientos = []
    with open(archivo, 'r') as file:
        for linea in file:
            # Aquí debes leer cada línea del archivo y crear instancias de Padecimiento
            datos = linea.strip().split(',')
            nuevo_padecimiento = Padecimiento(datos[0], datos[1], datos[2], datos[3])
            lista_padecimientos.append(nuevo_padecimiento)
    return lista_padecimientos
# Crear una nueva instancia de Medicamento y agregarla a la lista
#PARA LAS MEDICINAS
# Eliminar un medicamento de la lista por nombre
def baja_medicamento(lista_medicamentos, nombre_medicamento):
    lista_medicamentos = [med for med in lista_medicamentos if med.nombre != nombre_medicamento]

# Modificar un medicamento existente por nombre
def cambio_medicamento(lista_medicamentos, nombre_medicamento, nuevos_datos):
    for med in lista_medicamentos:
        if med.nombre == nombre_medicamento:
            # Aquí puedes actualizar los atributos del medicamento según los nuevos datos
            med.nombre = nuevos_datos['nombre']
            med.laboratorio = nuevos_datos['laboratorio']
            # Actualiza los demás atributos de manera similar
def guardar_datos(lista_medicamentos, archivo):
    with open(archivo, 'w') as file:
        for medicamento in lista_medicamentos:
            # Aquí debes escribir cada atributo del medicamento en una línea del archivo
            linea = f"{medicamento.nombre},{medicamento.laboratorio},{medicamento.composicion},{medicamento.via_administracion},{medicamento.dosis},{medicamento.lote},{medicamento.fecha_caducidad}\n"
            file.write(linea)
def cargar_datos(archivo):
    lista_medicamentos = []
    with open(archivo, 'r') as file:
        for linea in file:
            # Aquí debes leer cada línea del archivo y crear instancias de Medicamento
            datos = linea.strip().split(',')
            nuevo_medicamento = Medicamento(datos[0], datos[1], datos[2], datos[3], datos[4], datos[5], datos[6])
            lista_medicamentos.append(nuevo_medicamento)
    return lista_medicamentos
def guardar_datos_doctores(lista_doctores, archivo):
    with open(archivo, 'w') as file:
        for doctor in lista_doctores:
            # Aquí debes escribir cada atributo del doctor en una línea del archivo
            linea = f"{doctor.nombre},{doctor.fecha_nacimiento},{doctor.rfc},{doctor.telefono},{doctor.email},{doctor.especialidad},{doctor.cedula}\n"
            file.write(linea)

def cambio_doctor(lista_doctores, archivo, cedula, nuevos_datos):
    # Abre el archivo en modo lectura y escritura
    with open(archivo, 'r+') as file:
        for i, linea in enumerate(file):
            # Divide la línea en campos
            datos = linea.strip().split(',')
            
            # Comprueba si la cédula coincide con la que estás buscando
            if datos[6] == cedula:
                # Mueve el puntero a la posición correcta para realizar la modificación
                file.seek(i * len(linea))
                
                # Actualiza los datos en la lista de doctores
                for doctor in lista_doctores:
                    if doctor.cedula == cedula:
                        doctor.nombre = nuevos_datos['nombre']
                        doctor.fecha_nacimiento = nuevos_datos['fecha_nacimiento']
                        doctor.rfc = nuevos_datos['rfc']
                        doctor.telefono = nuevos_datos['telefono']
                        doctor.email = nuevos_datos['email']
                        doctor.especialidad = nuevos_datos['especialidad']
                        doctor.cedula = nuevos_datos['cedula']
                
                # Escribe la línea actualizada en el archivo
                file.write(f"{datos[0]},{datos[1]},{datos[2]},{datos[3]},{datos[4]},{datos[5]},{datos[6]}\n")
                break
def cargar_datos_doctores(archivo):
    with open(archivo, 'r') as file:
        for linea in file:
            datos = linea.strip().split(',')
            nuevo_doctor = Doctor(datos[0], datos[1], datos[2], datos[3], datos[4], datos[5], datos[6])
            lista_doctores.append(nuevo_doctor)
    return lista_doctores
def baja_doctor(lista_doctores, archivo, cedula):
    # Eliminar al doctor de la lista
    lista_doctores = [doctor for doctor in lista_doctores if doctor.cedula != cedula]

    # Reescribir todos los doctores restantes en el archivo
    with open(archivo, 'w') as file:
        for doctor in lista_doctores:
            file.write(f"{doctor.nombre},{doctor.fecha_nacimiento},{doctor.rfc},{doctor.telefono},{doctor.email},{doctor.especialidad},{doctor.cedula}\n")

def baja_paciente(lista_pacientes, rfc_paciente):
    lista_pacientes = [paciente for paciente in lista_pacientes if paciente.rfc != rfc_paciente]

def cambio_paciente(lista_pacientes, rfc_paciente, nuevos_datos):
    for paciente in lista_pacientes:
        if paciente.rfc == rfc_paciente:
            paciente.nombre = nuevos_datos['nombre']
            paciente.fecha_nacimiento = nuevos_datos['fecha_nacimiento']
            paciente.rfc = nuevos_datos['rfc']
            paciente.telefono = nuevos_datos['telefono']
            paciente.email = nuevos_datos['email']
            paciente.genero = nuevos_datos['genero']
            paciente.edad = nuevos_datos['edad']
            paciente.peso = nuevos_datos['peso']
            paciente.grupo_sanguineo = nuevos_datos['grupo_sanguineo']
def guardar_pacientes(lista_pacientes, archivo):
    with open(archivo, 'wb') as file:
        pickle.dump(lista_pacientes, file)

def cargar_pacientes(archivo):
    try:
        with open(archivo, 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return []

# Al inicio del programa, cargar la lista de pacientes si existe un archivo previo
lista_pacientes = cargar_pacientes('pacientes.pkl')



#%%
while True:
        archivo_doctores = "doctores"
        print('Opciones: ')
        print("1. Medicamento")
        print("2. Padecimiento")
        print("3. Doctor")
        print("4. Paciente")
        print("5. Historial Medico")
        print("6. Salir")

        opcion_1 = input('Selecciona una opcion: ')
        if opcion_1 == '1':

            print("Opciones:")
            print("1. Alta de Medicamento")
            print("2. Baja de Medicamento")
            print("3. Cambio de Medicamento")
            print("4. Lectura de medicamentos")
            print("5. Salir")

            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                nombre = input("Nombre del medicamento: ")
                laboratorio = input("Laboratorio: ")
                composicion = input("Composición: ")
                via_administracion = input("Vía de Administración: ")
                dosis = input("Dosis: ")
                lote = input("Lote: ")
                fecha_caducidad = input("Fecha de Caducidad (YYYY-MM-DD): ")
                nuevo_medicamento = Medicamento(nombre, laboratorio, composicion, via_administracion, dosis, lote, fecha_caducidad)
                lista_medicamentos.append(nuevo_medicamento)
                archivo_guardar = input("Nombre del archivo para guardar los datos: ")
                guardar_datos(lista_medicamentos, archivo_guardar)
                print("Medicamento agregado exitosamente.\n")

            elif opcion == "2":
                nombre_med = input("Ingresa el nombre del medicamento a dar de baja: ")
                baja_medicamento(lista_medicamentos, nombre_med)
                print("Medicamento eliminado exitosamente.\n")

            elif opcion == "3":
                nombre_med = input("Ingresa el nombre del medicamento a modificar: ")
                # Aquí puedes solicitar al usuario los nuevos datos
                nuevos_datos = {
                    'nombre': input("Nuevo nombre: "),
                    'laboratorio': input("Nuevo laboratorio: "),
                    # Completa con los demás atributos
                }
                print("Medicamento modificado exitosamente.\n")

                cambio_medicamento(lista_medicamentos, nombre_med, nuevos_datos)
            elif opcion == "4":
                archivo_cargar = input("Nombre del archivo para cargar los datos: ")
                lista_medicamentos = cargar_datos(archivo_cargar)
                print("Lista de Medicamentos:")
                for medicamento in lista_medicamentos:
                    print(f"Nombre: {medicamento.nombre}")
                    print(f"Laboratorio: {medicamento.laboratorio}")
                    print(f"Composición: {medicamento.composicion}")
                    print(f"Vía de Administración: {medicamento.via_administracion}")
                    print(f"Dosis: {medicamento.dosis}")
                    print(f"Lote: {medicamento.lote}")
                    print(f"Fecha de Caducidad: {medicamento.fecha_caducidad}")
                    print("\n")  # Agregar una línea en blanco entre medicamentos

            elif opcion == "5":
                break
        elif opcion_1 == '2':
            print("Opciones:")
            print("1. Alta de Padecimiento")
            print("2. Baja de Padecimiento")
            print("3. Cambio de Padecimiento")
            print("4. Lectura de Datos de padecimiento")
            print("5. Salir")

            opcion = input("Selecciona una opción: ")


            if opcion == "1":
                nombre = input("Nombre del Padecimiento: ")
                descripcion = input("Descripción: ")
                causas = input("Causas: ")
                tratamiento = input("Tratamiento: ")
                nuevo_padecimiento = Padecimiento(nombre, descripcion, causas, tratamiento)
                lista_padecimientos.append(nuevo_padecimiento)
                archivo_guardar = input("Nombre del archivo para guardar los datos de padecimientos: ")
                guardar_datos_padecimientos(lista_padecimientos, archivo_guardar)
                print("Padecimiento agregado exitosamente.\n")

            elif opcion == "2":
                nombre_pad = input("Ingresa el nombre del padecimiento a dar de baja: ")
                baja_padecimiento(lista_padecimientos, nombre_pad)
                print("Padecimiento eliminado exitosamente.\n")

            elif opcion == "3":
                nombre_pad = input("Ingresa el nombre del padecimiento a modificar: ")
                # Aquí puedes solicitar al usuario los nuevos datos
                nuevos_datos = {
                    'nombre': input("Nuevo nombre: "),
                    'descripcion': input("Nueva descripción: "),
                    'causas': input("Nuevas causas: "),
                    'tratamiento': input("Nuevo tratamiento: "),
                }
                cambio_padecimiento(lista_padecimientos, nombre_pad, nuevos_datos)
                print("Padecimiento modificado exitosamente.\n")

            elif opcion == "4":
                archivo_cargar = input("Nombre del archivo para cargar los datos de padecimientos: ")
                lista_padecimientos = cargar_datos_padecimientos(archivo_cargar)
                print("Lista de Padecimientos:")
                for padecimiento in lista_padecimientos:
                    print(f"Nombre: {padecimiento.nombre}")
                    print(f"Descripción: {padecimiento.descripcion}")
                    print(f"Causas: {padecimiento.causas}")
                    print(f"Tratamiento: {padecimiento.tratamiento}")
                    print("\n")  # Agregar una línea en blanco entre padecimientos
            elif opcion == "5":
                break
        elif opcion_1 == '3':
            print("Opciones:")
            print("1. Alta de Doctor")
            print("2. Baja de Doctor")
            print("3. Modificar Doctor")
            print("4. Lectura Datos")
            print("5. Salir")
            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                nombre = input("Nombre del Doctor: ")
                fecha_nacimiento = input("Fecha de Nacimiento (YYYY-MM-DD): ")
                rfc = input("RFC: ")
                telefono = input("Teléfono: ")
                email = input("Email: ")
                especialidad = input("Especialidad: ")
                cedula = input("Cédula Profesional: ")
                nuevo_doctor = Doctor(nombre, fecha_nacimiento, rfc, telefono, email, especialidad, cedula)
                lista_doctores.append(nuevo_doctor)
                for doctor in lista_doctores:
                    print(f"Nombre: {doctor.nombre}")
                    print(f"Fecha de Nacimiento: {doctor.fecha_nacimiento}")
                    print(f"RFC: {doctor.rfc}")
                    print(f"Teléfono: {doctor.telefono}")
                    print(f"Email: {doctor.email}")
                    print(f"Especialidad: {doctor.especialidad}")
                    print(f"Cédula: {doctor.cedula}")
                    print("\n")  # Agregar una línea en blanco entre doctores
                    archivo_guardar = 'doctores'
                    guardar_datos_doctores(lista_doctores, archivo_guardar)
                    print("Doctor agregado exitosamente.\n")


            elif opcion == "2":
                cedula_doc = input("Ingresa la cédula del doctor a dar de baja: ")
                baja_doctor(lista_doctores, archivo_doctores, cedula_doc)
                print("Doctor eliminado exitosamente.\n")

            elif opcion == "3":
                cedula_doc = input("Ingresa la cédula del doctor a modificar: ")
                nuevos_datos = {
                    'nombre': input("Nuevo nombre: "),
                    'fecha_nacimiento': input("Nueva fecha de nacimiento (YYYY-MM-DD): "),
                    'rfc': input("Nuevo RFC: "),
                    'telefono': input("Nuevo teléfono: "),
                    'email': input("Nuevo email: "),
                    'especialidad': input("Nueva especialidad: "),
                    'cedula': input("Nueva cédula: "),
                }
                cambio_doctor(lista_doctores, archivo_doctores, cedula_doc, nuevos_datos)
                print("Doctor modificado exitosamente.\n")

            elif opcion == "4":
                archivo_cargar = 'doctores'
                lista_doctores = cargar_datos_doctores(archivo_cargar)
                print("Lista de Doctores:")
                for doctor in lista_doctores:
                    print(f"Nombre: {doctor.nombre}")
                    print(f"Fecha de Nacimiento: {doctor.fecha_nacimiento}")
                    print(f"RFC: {doctor.rfc}")
                    print(f"Teléfono: {doctor.telefono}")
                    print(f"Email: {doctor.email}")
                    print(f"Especialidad: {doctor.especialidad}")
                    print(f"Cédula: {doctor.cedula}")
                    print("\n")  # Agregar una línea en blanco entre doctores
            elif opcion == "5":
                break
        elif opcion_1 == '4':
            print("Opciones:")
            print("1. Alta de Paciente")
            print("2. Baja de Paciente")
            print("3. Modificar Paciente")
            print("4. Cargar Datos")
            print("5. Salir")
            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                nombre = input("Nombre del Paciente: ")
                fecha_nacimiento = input("Fecha de Nacimiento (YYYY-MM-DD): ")
                rfc = input("RFC: ")
                telefono = input("Teléfono: ")
                email = input("Email: ")
                genero = input("Género: ")
                edad = input("Edad: ")
                peso = input("Peso: ")
                grupo_sanguineo = input("Grupo Sanguíneo: ")
                nuevo_paciente = Paciente(nombre, fecha_nacimiento, rfc, telefono, email, genero, edad, peso, grupo_sanguineo)
                lista_pacientes.append(nuevo_paciente)
                for paciente in lista_pacientes:
                    print(f"Nombre: {paciente.nombre}")
                    print(f"Fecha de Nacimiento: {paciente.fecha_nacimiento}")
                    print(f"RFC: {paciente.rfc}")
                    print(f"Teléfono: {paciente.telefono}")
                    print(f"Email: {paciente.email}")
                    print(f"Género: {paciente.genero}")
                    print(f"Edad: {paciente.edad}")
                    print(f"Peso: {paciente.peso}")
                    print(f"Grupo Sanguíneo: {paciente.grupo_sanguineo}")
                    print("\n")  # Agregar una línea en blanco entre pacientes
                    archivo_guardar = 'pacientes.pkl'
                    guardar_pacientes(lista_pacientes, archivo_guardar)
                print("Paciente agregado exitosamente.\n")


            elif opcion == "2":
                rfc_paciente = input("RFC del paciente a dar de baja: ")
                lista_pacientes = baja_paciente(lista_pacientes, rfc_paciente)
                print("Paciente eliminado exitosamente.\n")
                print("Paciente elimnado exitosamente.\n")
                
            elif opcion == "3":
                rfc_paciente = input("RFC del paciente a modificar: ")
                nuevos_datos = {
                    'nombre': input("Nuevo nombre: "),
                    'fecha_nacimiento': input("Nueva fecha de nacimiento: "),
                    'rfc': input("Nuevo RFC: "),
                    'telefono': input("Nuevo teléfono: "),
                    'email': input("Nuevo email: "),
                    'genero': input("Nuevo género: "),
                    'edad': input("Nueva edad: "),
                    'peso': input("Nuevo peso: "),
                    'grupo_sanguineo': input("Nuevo grupo sanguíneo: ")
                }
                lista_pacientes = cambio_paciente(lista_pacientes, rfc_paciente, nuevos_datos)
                print("Paciente modificado exitosamente.\n")
                

            elif opcion == "4":
                archivo_cargar = 'pacientes.pkl'
                lista_pacientes = cargar_pacientes(archivo_cargar)
                print("Lista de Pacientes:")
                for paciente in lista_pacientes:
                    print(f"Nombre: {paciente.nombre}")
                    print(f"Fecha de Nacimiento: {paciente.fecha_nacimiento}")
                    print(f"RFC: {paciente.rfc}")
                    print(f"Teléfono: {paciente.telefono}")
                    print(f"Email: {paciente.email}")
                    print(f"Género: {paciente.genero}")
                    print(f"Edad: {paciente.edad}")
                    print(f"Peso: {paciente.peso}")
                    print(f"Grupo Sanguíneo: {paciente.grupo_sanguineo}")
                    print("\n")  # Agregar una línea en blanco entre pacientes
            elif opcion == "5":
                break

        elif opcion_1 == '5':
                        print('Opciones: ')
                        print("1. Agregar Historial Médico")
                        print("2. Cargar Datos")
                        print("3. Salir")

                        opcion_1 = input('Selecciona una opcion: ')

                        if opcion_1 == '1':
                            paciente = input("Paciente: ")
                            padecimiento = input("Padecimiento: ")

                            historial = HistorialMedico(paciente, padecimiento)

                            # Generar signos vitales aleatorios
                            signos_vitales_aleatorios = {
                                "Pulso": random.randint(60, 100),
                                "Frecuencia Cardiaca": random.randint(60, 100),
                                "Frecuencia Respiratoria": random.randint(12, 20),
                                "Temperatura": round(random.uniform(36.0, 37.5), 1),
                                "Presión Arterial": f"{random.randint(90, 140)}/{random.randint(60, 90)}"
                            }

                            for clave, valor in signos_vitales_aleatorios.items():
                                historial.agregar_signo_vital(clave, valor)

                            lista_historiales.append(historial)
                            print("Historial Médico Agregado.\n")
                            archivo_guardar = 'historial.txt'
                            guardar_datos_historial(lista_historiales, archivo_guardar)
                            print("Datos guardados.\n")
                            
                        elif opcion_1 == '2':
                            archivo_cargar = 'historial.txt'
                            historiales = cargar_datos_historial(archivo_cargar)

                            for historial in historiales:
                                print(f"Folio: {historial.folio}")
                                print(f"Paciente: {historial.paciente}")
                                print(f"Padecimiento: {historial.padecimiento}")
                                print("Signos Vitales:")
                                for clave, valor in historial.signos_vitales.items():
                                    print(f"{clave}: {valor}")
                                print()

                        elif opcion_1 == '3':
                            break
        elif opcion_1 == "6":
            break

#%%

# Solicitar al usuario el nombre del doctor y la especialidad
doctor = input("Nombre del Doctor: ")
especialidad = input("Especialidad: ")
medicina = input("Medicina: ")
# Leer los datos del archivo "historial.pkl" y crear un DataFrame
with open('historial.pkl', 'rb') as file:
    lista_historiales = pickle.load(file)

data = []
for historial in lista_historiales:
    data.append([
        doctor,  # Nombre del Doctor proporcionado por el usuario
        especialidad,  # Especialidad proporcionada por el usuario
        medicina,
        historial.paciente,
        historial.folio,
        historial.padecimiento,
        historial.signos_vitales
    ])

column_names = ['Doctor', 'Especialidad', 'Paciente', 'Folio historial médico', 'Padecimiento', 'Medicamento', 'Signos vitales']

df = pd.DataFrame(data, columns=column_names)

# Ahora puedes continuar con la generación del informe en Excel como se mencionó anteriormente
archivo_excel = "reporte_excel.xlsx"
df.to_excel(archivo_excel, index=False)

print(f"Reporte generado y guardado en {archivo_excel}")
# %%
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import pickle

#%%
# Solicitar al usuario el nombre del doctor, especialidad, medicina, email, tratamiento, laboratorio y composición
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

# Obtener datos del usuario
doctor = input("Nombre del Doctor: ")
especialidad = input("Especialidad: ")
medicina = input("Medicina: ")
email = input("Email del Doctor: ")
tratamiento = input("Tratamiento: ")
laboratorio = input("Laboratorio: ")
composicion = input("Composición: ")

# Leer los datos del archivo "historial.pkl" y crear un DataFrame
with open('historial.pkl', 'rb') as file:
    lista_historiales = pickle.load(file)

data = []
for historial in lista_historiales:
    data.append([
        f" {doctor}",  # Nombre del Doctor proporcionado por el usuario
        f"  {especialidad}",  # Especialidad proporcionada por el usuario
        f"  {medicina}",
        f" {email}",
        f" {tratamiento}",
        f"  {laboratorio}",
        f"  {composicion}",
        f" {historial.paciente}",
        f"   {historial.folio}",
        f"  {historial.padecimiento}",
    ])

# Crear un archivo PDF
archivo_pdf = "reporte_pdf.pdf"
doc = SimpleDocTemplate(archivo_pdf, pagesize=landscape(letter))

# Crear una tabla con los datos
ancho_pagina, alto_pagina = landscape(letter)
ancho_columnas = [1 * ancho_pagina / len(data[0])] * len(data[0])  # Distribuir el ancho de manera uniforme

# Estilo para los títulos
styles = getSampleStyleSheet()
style_title = styles["Normal"]
style_title.alignment = 1  # Alineación al centro
style_title.fontName = 'Helvetica-Bold'

# Agregar una fila con los títulos
titulos = [
    Paragraph(" Doctor: ", style_title),
    Paragraph(" Especialidad: ", style_title),
    Paragraph(" Medicina: ", style_title),
    Paragraph(" Email del Doctor: ", style_title),
    Paragraph(" Tratamiento: ", style_title),
    Paragraph(" Laboratorio: ", style_title),
    Paragraph(" Composición: ", style_title),
    Paragraph(" Paciente: ", style_title),
    Paragraph(" Folio historial médico: ", style_title),
    Paragraph("Padecimiento: ", style_title),
]

tabla_data = [titulos] + data

tabla = Table(tabla_data, colWidths=ancho_columnas)
tabla.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ('GRID', (0, 0), (-1, -1), 1, colors.black)
]))

# Construir el PDF
elems = []
elems.append(tabla)
doc.build(elems)

# Mostrar un mensaje de confirmación
print(f"Informe PDF generado y guardado en {archivo_pdf}")




# %%
import random
import matplotlib.pyplot as plt

# Generar un conjunto de signos vitales para cada día de la semana
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

signos_vitales_por_dia = {}
for dia in dias_semana:
    signos_vitales_por_dia[dia] = {
        'Pulso': random.randint(60, 100),
        'Frecuencia Cardiaca': random.randint(60, 100),
        'Frecuencia Respiratoria': random.randint(12, 20),
        'Temperatura': round(random.uniform(36.0, 37.5), 1),
        'Presión Arterial': f"{random.randint(90, 140)}/{random.randint(60, 90)}"
    }

# Extraer los datos de presión arterial y temperatura por día
presion_arterial_por_dia = []
temperatura_por_dia = []
for dia in dias_semana:
    presion_arterial_por_dia.append(int(signos_vitales_por_dia[dia]['Presión Arterial'].split('/')[0]))
    temperatura_por_dia.append(signos_vitales_por_dia[dia]['Temperatura'])

# Crear gráfico de presión arterial por días
plt.figure(figsize=(10, 5))
plt.plot(dias_semana, presion_arterial_por_dia, marker='o', linestyle='-')
plt.title('Presión Arterial por Días')
plt.xlabel('Día de la Semana')
plt.ylabel('Presión Arterial (mmHg)')
plt.grid(True)

# Mostrar el gráfico de presión arterial
plt.show()

# Crear gráfico de temperatura por días
plt.figure(figsize=(10, 5))
plt.plot(dias_semana, temperatura_por_dia, marker='o', linestyle='-')
plt.title('Temperatura por Días')
plt.xlabel('Día de la Semana')
plt.ylabel('Temperatura (°C)')
plt.grid(True)

# Mostrar el gráfico de temperatura
plt.show()


# %%
