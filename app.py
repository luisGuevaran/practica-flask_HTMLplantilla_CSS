from flask import Flask,render_template,request
import math

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():
    tt =0
    pc=3000
    pt=4500
    respuesta=None
    if request.method == 'POST':
        c= int(request.form['cafe'])
        p= int(request.form['pastel'])

        tt= (c*pc)+(p*pt)
        respuesta = f"El total a pagar es: ${tt}"
    return render_template('luisG1.html', mensaje=respuesta)




@app.route("/ejercicio2",methods=["GET", "POST"])
def ejercicio2():
    mensaje=None
    paqtA=2
    paqtB=5
    if request.method == 'POST':
        pa= int(request.form['pA']) 
        pb= int(request.form['pB'])
        pt= (pa*paqtA)+(pb*paqtB)
        mensaje = f"El peso total es: {pt} kg"
    return render_template("luisG2.html", mensaje=mensaje)

@app.route("/ejercicio3",methods=["GET", "POST"])
def ejercicio3():
    
    mensaje=None
    if request.method == 'POST':
        dispCaja= int(request.form['cr'])
        botellVacia= int(request.form['cv'])
        botellaDisp=(dispCaja*12)-botellVacia
        mensaje = f"Las botellas disponibles son: {botellaDisp}"

    return render_template("luisG3.html", mensaje=mensaje)

@app.route("/ejercicio4",methods=["GET", "POST"])
def ejercicio4():
    mensaje=None
    if request.method == 'POST':
        personasDelant=int(request.form['pf'])
        tiemProm=4
        tiempoTotal=personasDelant*tiemProm
        mensaje = f"El tiempo estimado de espera es: {tiempoTotal} minutos"
    return render_template("luisG4.html", mensaje=mensaje)

@app.route("/ejercicio5",methods=["GET", "POST"])   
def ejercicio5():
    mensaje=None
    if request.method== 'POST':
        km=float(request.form['ck'])
        kmGas=12
        gasTotal=math.ceil(km/kmGas)
        mensaje = f"Los litros de gasolina necesarios son: {gasTotal} litros"
    return render_template("luisG5.html", mensaje=mensaje)

if __name__ == "__main__":
    app.run(debug=True)