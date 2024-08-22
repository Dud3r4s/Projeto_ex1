from flask import Flask, render_template, request, redirect, flash
import mysql.connector

# Inicialize o aplicativo Flask
app = Flask(__name__)
app.secret_key = ''  # Necessário para flash

# Conexão com o banco de dados
comanda_bd = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='',
    database='comanda_bar'
)

# Defina a rota para capturar os dados do formulário e inseri-los no banco de dados
@app.route("/cliente", methods=['POST'])
def cliente():
    print(request.method)
    if request.method == 'POST':
        # Coletar os dados do formulário
        nome = request.form.get('nome')
        cpf = request.form.get('cpf')
        data_aniversario = request.form.get('data_aniversario')
        endereco = request.form.get('endereco')  # Sem acento
        bairro = request.form.get('bairro')
        cidade = request.form.get('cidade')
        estado = request.form.get('estado')
        cep = request.form.get('cep')

        print(f"Nome: {nome}, CPF: {cpf}, Data de Aniversário: {data_aniversario}, Endereço: {endereco}, Bairro: {bairro}, Cidade: {cidade}, Estado: {estado}, CEP: {cep}")


        # Insira os dados no banco de dados
        cursor = comanda_bd.cursor()
        try:
            # Prepare a consulta SQL para inserir os dados
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
        return render_template('')
    else:
        # Se for uma requisição GET, exibe o formulário
        return render_template('prim_Funcao.html')

# Rodar o aplicativo Flask
if __name__ == '__main__':
    app.run(debug=True)
