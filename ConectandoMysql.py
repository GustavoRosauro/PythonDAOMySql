import mysql.connector
from Pessoa import Pessoa

db = mysql.connector.connect(host="localhost", database="empresa", user="root", password="")


def mostraDados():
    try:
        cursor = db.cursor()
        listaPessoas = list()
        sql = "select * from pessoa"
        cursor.execute(sql)
        resultado = cursor.fetchall()
        for row in resultado:
            p = Pessoa(row[1], row[2], row[3])
            listaPessoas.append(p)
        for pessoa in listaPessoas:
            print('seu nome é ' + pessoa.getNome() + ' Sua idade é ' + str(
                pessoa.getIdade()) + ' seu cpf é ' + pessoa.getCPF())
    except print(str(Exception)):
        pass


def inserirDados():
    try:
        cursor = db.cursor()
        p = Pessoa(input('Informe o nome que deseja inserir'), input('informe a idade'), input('informe o cpf'))
        sql = "insert into pessoa (nome,idade,cpf) values (%s,%s,%s)"
        records = (p.getNome(), p.getIdade(), p.getCPF())
        cursor.execute(sql, records)
        db.commit()
        print('nova linha inserida')
    except print(Exception):
        pass

def removeItem(id):
    try:
        cursor = db.cursor()
        sqlDelete = "delete from pessoa where id = " + str(id)
        cursor.execute(sqlDelete)
        db.commit()
        print('foi removido com sucesso')
    except print(Exception):
        pass
def editarItem(id):
    try:
        cursor = db.cursor()
        p = Pessoa(input('informe o novo nome'), input('informa nova idade'), input('informe novo cpf'))
        sqlUpdate = " update pessoa " \
                    " set nome =%s," \
                    " idade =%s," \
                    " cpf =%s" \
                    " where id = " + str(id)
        dados = (p.getNome(), int(p.getIdade()), p.getCPF())
        cursor.execute(sqlUpdate, dados)
        db.commit()
    except print(Exception):
        pass
continua = True
while continua:
    resposta = str(input('informe 1 para inserir e 2 para visualizar 3 para remover e 4 para editar'))
    if resposta.strip() == '1':
        inserirDados()
    elif resposta.strip() == '2':
        mostraDados()
    elif resposta.strip() == '3':
        removeItem(int(input('informe o código que deseja remover')))
    elif resposta.strip() == '4':
        editarItem(input('informe o código do usuário que deseja editar'))
    else:
        print('Valor informado não foi encontrado')
    continua = True if input('deseja continuar? caso sim digite sim').strip() == 'sim' else False
