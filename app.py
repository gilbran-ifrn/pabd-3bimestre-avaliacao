from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

from flask_login import LoginManager
from flask_login import login_required
from flask_login import login_user
from flask_login import logout_user
from flask_login import current_user
from flask_login import UserMixin

from crud import createUpdateDelete
from crud import read



'''
####################################################################
# Dicionário apenas utilizado para as telas de feedback
# com o usuário.
####################################################################
'''
feedback = {
    'url' : '',
    'msg' : ''
}



'''
####################################################################
# Instanciação do objeto APP
####################################################################
'''
app = Flask(__name__)
app.secret_key = 'string super secreta'



'''
####################################################################
# Instanciação e definiçoes necessária
# para o gerenciamento da sessao
####################################################################
'''
# Objeto gerenciador de sessão
loggin_manager = LoginManager()
loggin_manager.init_app(app)

# Classe necessária para poder gerenciar a sessão na função LOAD_USER
class Usuario(UserMixin):
    nome = ''
    def __init__(self):
        super().__init__()

# Desc: Verifica se o usuário está com a sessão ativa
# Entrada: id do usuário
# Saída: objeto Usuario se ativo | None, caso inativo
@loggin_manager.user_loader
def load_user(id):
    mens = read(
        "SELECT id, nome FROM paciente WHERE id = %s",
        (id,),
        'fetchone'
    )

    if (mens):
        u = Usuario()
        u.id = id
        u.nome = mens['nome']

        return u
    return None

# Desc: Gerencia o que fazer quando um acesso não autorizado 
#       tenta acessar partes privadas (@login_required)
# Entrada: None
# Saída: rota /
@loggin_manager.unauthorized_handler
def naoAutorizado():
    print('ACESSO NÃO AUTORIZADO')
    return redirect('/')

# Desc: Logout do usuário logado
# Entrada: None (necessário estar logado)
# Saída: Página de login
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')



'''
####################################################################
# Rota index -> /
####################################################################
'''
# Desc: Rota padrão da aplicação
# Entrada: None
# Saída: Página de login | Página de painel
@app.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(f"/painel")
    else:
        return render_template('login.html')
    
# Desc: Página inicial do usuário que está logado
# Entrada: id do usuário
# Saída: Página de painel
@app.route('/painel')
@login_required
def painel():
    return render_template('painel.html')
    


'''
####################################################################
# Login do usuário
####################################################################
'''
# Desc: Rota chamada pelo form de login
# Entrada: None
# Saída: Página do painel | Função naoAutorizado()
@app.route('/login', methods=['POST'])
def autenticacao():
        emaillogin = request.form['email']

        mens = read(
            "SELECT id, nome, senha FROM paciente WHERE email = %s",
            (emaillogin,),
            'fetchone'
        )

        if mens != None:
            # 1o parametro=senha do banco em hash
            # 2o parametro=senha do forms sem hash
            if check_password_hash(mens['senha'], request.form['senha']):
                usuario = Usuario()
                usuario.id = mens['id']
                usuario.nome = mens['nome']
                
                login_user(usuario) # comando que efetiva o inicio da sessão

                return redirect(f"/painel")
            
        return loggin_manager.unauthorized()



'''
####################################################################
# Tudo relativo ao usuário
####################################################################
'''
# Desc: Rota para adição de um novo usuário
# Entrada: 
# Saída: (GET) Form de cadastro | (POST) Feedback
@app.route('/addUsuario', methods=['GET','POST'])
def addUsuario():
    if request.method == 'GET':
        return render_template('userAdd.html')
    
    else: # request.method == 'POST':
        n = request.form['nome']
        e = request.form['email']
        s = generate_password_hash(request.form['senha'])

        status = createUpdateDelete(
            "INSERT INTO paciente (nome, email, senha) VALUES (%s, %s, %s)",
            (n, e, s),
            'INSERT'
        )

        if status:
            feedback["url"] = "/"
            feedback["msg"] = "Usuário cadastrado com sucesso!"

            return render_template('respSucesso.html', fb=feedback)
        
        else:
            feedback["url"] = "/addUsuario"
            feedback["msg"] = "Falha ao cadastrar usuário"
            
            return render_template('respFalha.html', fb=feedback)
    
# Desc: Rota para alteração de dados de um usuário
# Entrada: 
# Saída: (GET) Form de alteração | (POST) Feedback
@app.route('/updateUsuario', methods=['GET','POST'])
@login_required
def updateUsuario():
    id = current_user.get_id()

    if request.method == 'GET':
        dados = read(
            "SELECT nome, email FROM paciente WHERE id = %s",
            (id,),
            'fetchone'
        )
        
        return render_template('userUpdate.html', dadosBD=dados)
        
    else: # request.method == 'POST'
        n = request.form['nome']
        e = request.form['email']
        s = generate_password_hash(request.form['senha'])

        status = createUpdateDelete(
            "UPDATE paciente \
                SET nome = %s, email = %s, senha = %s \
                WHERE id = %s",
            (n, e, s, id),
            'UPDATE'
        )

        if status:
            feedback["url"] = f"/painel"
            feedback["msg"] = "Dados atualizados com sucesso!"
            return render_template('respSucesso.html', fb=feedback)
        
        else:
            feedback["url"] = f"/updateUsuario"
            feedback["msg"] = "Falha ao atualizar os dados!"
            return render_template('respFalha.html', fb=feedback)



'''
####################################################################
# Tudo relativo as consultas
####################################################################
'''
# Desc: Lista todos os agendamentos de consulta do paciente
# Entrada: 
# Saída: Página com a listagem das consultas
@app.route('/consultas')
@login_required
def consultas():
    id = current_user.get_id()

    dados = read(
        ##################################
        ###    SEU CÓDIGO AQUI - 6     ###
        ##################################
    )

    return render_template('consultas.html', dadosBD=dados)
    
# Desc: Adiciona um novo agendamento de consulta
# Entrada: 
# Saída: Página de erro ou página de painel
@app.route('/addConsulta', methods=['GET','POST'])
@login_required
def addConsulta():
    id = current_user.get_id()

    if request.method == 'GET':
        dadosMedicos = read(
            "SELECT id, especialidade, nome, descricao \
                FROM profissional \
                ORDER BY especialidade",
            None,
            'fetchall'
        )

        return render_template('consultaAdd.html', dadosBD=dadosMedicos)
    
    else: # request.method == 'POST':
        medicoID = request.form['medico']
        data = request.form['data']
        hora = request.form['horario']

        datahora = f"{data} {hora}:00"

        status = createUpdateDelete(
            ##################################
            ###    SEU CÓDIGO AQUI - 5     ###
            ##################################
        )

        if status:
            feedback["url"] = f"/consultas"
            feedback["msg"] = "Consulta agendada com sucesso!"
            return render_template('respSucesso.html', fb=feedback)
        
        else:
            feedback["url"] = f"/addConsulta"
            feedback["msg"] = "Falha ao agendar a consulta!"
            return render_template('respFalha.html', fb=feedback)


# Desc: Atualiza o agendamento de uma consulta do paciente
# Entrada: id da consulta
# Saída: (GET) Form de alteração | (POST) Feedback
@app.route('/updateConsulta/<idConsulta>', methods=['GET','POST'])
@login_required
def updateConsulta(idConsulta):
    idUsuario = current_user.get_id()

    verifica = read(
        "SELECT id FROM consulta WHERE id=%s AND idPaciente=%s",
        (idConsulta, idUsuario),
        'fetchone'
    )

    if verifica: # a consulta pertence ao usuário logado
        if request.method == 'GET':
            dadosMedicos = read(
                "SELECT id, especialidade, nome, descricao \
                    FROM profissional \
                    ORDER BY especialidade",
                None,
                'fetchall'
            )

            dadosConsulta = read(
                "SELECT \
                    con.id AS consultaID, \
                    pro.id AS medicoID, \
                    DATE_FORMAT(con.datahora, '%Y-%m-%d') AS data, \
                    DATE_FORMAT(con.datahora, '%H:%i') AS hora \
                FROM \
                    consulta AS con, \
                    paciente AS pac, \
                    profissional AS pro \
                WHERE \
                    pac.id=con.idPaciente AND \
                    pro.id=con.idProfissional AND \
                    con.id=%s AND pac.id=%s;",
                (idConsulta, idUsuario),
                'fetchone'
            )
            return render_template("consultaUpdate.html", dadosBDConsulta=dadosConsulta, dadosBDMedicos=dadosMedicos)
        else: # request.method == 'POST'
            medicoID = request.form['medico']
            data = request.form['data']
            hora = request.form['horario']

            datahora = f"{data} {hora}:00"

            status = createUpdateDelete(
                ##################################
                ###    SEU CÓDIGO AQUI - 4     ###
                ##################################
            )

            if status:
                feedback["url"] = f"/consultas"
                feedback["msg"] = "Dados da consulta atualizados com sucesso!"
                return render_template('respSucesso.html', fb=feedback)
            
            else:
                feedback["url"] = f"/updateConsulta/{idConsulta}"
                feedback["msg"] = "Falha ao atualizar os dados da consulta!"
                return render_template('respFalha.html', fb=feedback)


    else: # a consulta não pertence ao usuário logado
        redirect("/")

    
        

# Desc: Exclui o agendamento de consulta do paciente
# Entrada: id da consulta
# Saída: Feedback
@app.route('/deleteConsulta/<idConsulta>')
@login_required
def deleteConsulta(idConsulta):
    # VERIFICAR SE A CONSULTA EH MINHA MESMO

    status = createUpdateDelete(
        ##################################
        ###    SEU CÓDIGO AQUI - 3     ###
        ##################################
    )

    if status:
        feedback["url"] = f"/consultas"
        feedback["msg"] = "Agendamento excluído com sucesso!"

        return render_template('respSucesso.html', fb=feedback)
    
    else:
        feedback["url"] = f"/consultas"
        feedback["msg"] = "Falha na exclusão do agendamento!"

        return render_template('respFalha.html', fb=feedback)



'''
####################################################################
# Exibe a listagem de médicos
####################################################################
'''
# Desc: Lista todos os médicos cadastrados
# Entrada: 
# Saída: Página com os médicos cadastrados
@app.route('/medicos')
@login_required
def medicos():
    dados = read(
        ##################################
        ###    SEU CÓDIGO AQUI - 2     ###
        ##################################
    )

    return render_template('medicos.html', dadosBD=dados)