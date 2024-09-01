from flask import Flask, render_template,request,flash,redirect,url_for

from datetime import datetime

import mysql.connector


# Inicializa o aplicativo do Flask
app = Flask(__name__)
app.secret_key = '123'


# Faz a Conexão com o banco de dados
comanda_bd = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='',
    database='comanda_bar'
)

@app.route('/')
def login():
    return render_template('login.html')



# Define a rota para capturar os dados do formulário e inseri-los no banco de dados.
@app.route("/login_cliente", methods=['POST'])
def login_cliente():
        
    if request.method == 'POST':
        # Coletar os dados do formulário
        nome = request.form.get('nome')
        cpf = request.form.get('cpf')
        data_aniversario = request.form.get('data_aniversario')
        endereco = request.form.get('endereco')
        bairro = request.form.get('bairro')
        cidade = request.form.get('cidade')
        estado = request.form.get('estado')
        cep = request.form.get('cep')

        print(f"Nome: {nome}, CPF: {cpf}, Data de Aniversário: {data_aniversario}, Endereço: {endereco}, Bairro: {bairro}, Cidade: {cidade}, Estado: {estado}, CEP: {cep}")
    

        # Insere os dados no banco de dados
        cursor = comanda_bd.cursor()
        try:
            # Prepara a consulta no SQL para inserir os dados
            query = """
            INSERT INTO cliente (nome, cpf, data_aniversario, endereco, bairro, cidade, estado, cep) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            values = (nome, cpf, data_aniversario, endereco, bairro, cidade, estado, cep)
            
            # Executa a inserção
            cursor.execute(query, values)
            
            # Confirma a transação no banco de dados
            comanda_bd.commit()
            
            flash("Dados inseridos com sucesso!", "success")
        except mysql.connector.Error as err:
            flash(f"Ocorreu um erro: {err}", "danger")
        finally:
            cursor.close()

        # Redirecionar ou recarregar o formulário
        return render_template('pedido.html') # direcionar para o novo formulario quando você clicar no botão, ou alguma pagina. 
        #return redirect(url_for('pedido.html')) # proxima pagina


        # Roda o aplicativo Flask
if __name__ == '__main__':
    app.run(debug=True)
