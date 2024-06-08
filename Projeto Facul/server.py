from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('reserva.html')

@app.route('/enviar_dados', methods=['POST'])
def dados_reserva():
    if request.method == 'POST':
        nome = request.form['nome']
        quantidade = request.form['quantidade']
        try:
            conexao = mysql.connector.connect(
                host='localhost',
                database='reservas',
                user='root',
                password='admin04'
                )
            
            cursor = conexao.cursor()
            cursor.execute("INSERT INTO dados (NOME, QUANTIDADE) VALUES (%s, %s)", (nome, quantidade))
            conexao.commit()
            
            cursor.close()
            conexao.close()
            return redirect('/')
        except Exception as e:
            return str(e)

if __name__ == '__main__':
    app.run(debug=True)
