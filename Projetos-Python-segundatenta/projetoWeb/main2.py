from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nome = request.form['nome']
        senha = request.form['senha']
        cpf = request.form['cpf']

        print(f"Nome: {nome}")
        print(f"Senha: {senha}")
        print(f"CPF: {cpf}")

        return "Dados recebidos! Verifique o terminal para ver as informações."

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


#Cria um template html, backend python,