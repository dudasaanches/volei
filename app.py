from flask import Flask, render_template, request, redirect

app = Flask(__name__)

class cadvolei:
    def __init__(self,nome,idade,posicao,nivel,cidade,dia,horario):
        self.nome = nome
        self.idade = idade
        self.posicao = posicao
        self.nivel = nivel
        self.cidade = cidade
        self.dia = dia
        self.horario = horario

volleyball_players = []


@app.route('/')

def volei():  # put application's code here
    return render_template("volei.html", Titulo = "Jogadores de volêi", ListaJogadores = volleyball_players)

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html', Titulo = "Cadastro dos jogadores")

@app.route("/criar", methods=['POST'])
def criar():
    nome = request.form['nome']
    idade = request.form['idade']
    posicao = request.form['posicao']
    nivel = request.form['nivel']
    cidade = request.form['cidade']
    dia = request.form['dia']
    horario = request.form['horario']
    obj = cadvolei(nome,idade,posicao,nivel,cidade,dia,horario)
    volleyball_players.append(obj)
    return redirect('/')

if __name__ == '__main__':
    app.run()
