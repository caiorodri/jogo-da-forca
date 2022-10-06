import sqlite3
import re


class Sistema_Users:

    def __init__(self, nickname, senha, email='', repeticao_senha=None):

        self.nickname = nickname
        self.email = email
        self.senha = senha
        self.repeticao_senha = repeticao_senha

    def check_email(self):

        regex = r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'

        if(re.search(regex, self.email)):

            return True

        else:

            return False

    def ranking(self):

        conexao = sqlite3.connect('sist_login.db')
        cursor = conexao.cursor()

        cursor.execute('SELECT * FROM usuarios ORDER BY vitorias DESC')

        contador = 0

        print('\n--- RANKING ---')

        print('\nP - NICK - W - L\n')

        for linha in cursor.fetchall():

            contador += 1

            if contador <= 10:

                print(
                    f'{contador} - {linha[1]} - {linha[4]} - {linha[5]} ')

        cursor.close()
        conexao.close()

        _ = input('\nPressione enter para continuar...')

    def cadastro(self):

        conexao = sqlite3.connect('sist_login.db')
        cursor = conexao.cursor()

        cursor.execute('SELECT * FROM usuarios')

        for linha in cursor.fetchall():

            if self.nickname in linha[1]:

                cursor.close()
                conexao.close()

                return '\nNickname já está sendo usado\n'

            if self.email in linha[2]:

                cursor.close()
                conexao.close()
                return '\nEmail existente\n'

            if self.check_email() == False:

                cursor.close()
                conexao.close()
                return '\nEmail invalido\n'

            if self.senha != self.repeticao_senha:

                cursor.close()
                conexao.close()
                return '\nSenhas diferentes\n'

            if len(self.senha) < 8:

                cursor.close()
                conexao.close()
                return '\nA senha precisa ter pelo menos 8 caractéres \n'

            if len(self.nickname) > 8 or len(self.nickname) < 4:

                cursor.close()
                conexao.close()
                return '\nSeu nickname deve ter entre 4 e 8 caractéres \n'

        cursor.execute('INSERT INTO usuarios (nickname, email, senha, vitorias, derrotas) VALUES (:nickname, :email, :senha, :vitorias, :derrotas)',
                       {'nickname': self.nickname, 'email': self.email, 'senha': self.senha, 'vitorias': 0, 'derrotas': 0})

        conexao.commit()

        cursor.close()
        conexao.close()

        return True

    def login(self):

        conexao = sqlite3.connect('sist_login.db')

        cursor = conexao.cursor()

        consulta = 'SELECT * FROM usuarios WHERE nickname LIKE ?'

        cursor.execute(consulta, (self.nickname,))

        dados = cursor.fetchall()

        try:

            if self.senha != dados[0][3]:

                cursor.close()
                conexao.close()
                return '\nSenha invalida.\n'

        except IndexError:

            return '\nUsuario invalido.\n'

        conexao.commit()

        cursor.close()
        conexao.close()

        return True

    def vitoria(self):

        conexao = sqlite3.connect('sist_login.db')

        cursor = conexao.cursor()

        consulta = 'UPDATE usuarios SET vitorias=vitorias+1 WHERE nickname=?'

        cursor.execute(consulta, (self.nickname,))

        conexao.commit()

        cursor.close()
        conexao.close()

    def derrota(self):

        conexao = sqlite3.connect('sist_login.db')

        cursor = conexao.cursor()

        consulta = 'UPDATE usuarios SET derrotas=derrotas+1 WHERE nickname=?'

        cursor.execute(consulta, (self.nickname,))

        conexao.commit()

        cursor.close()
        conexao.close()

    def status(self):

        conexao = sqlite3.connect('sist_login.db')

        cursor = conexao.cursor()

        consulta = 'SELECT * FROM usuarios WHERE nickname=?'

        cursor.execute(consulta, (self.nickname,))

        dados = cursor.fetchall()

        print(f"""Perfil do {self.nickname}

Partidas: {dados[0][-1] + dados[0][-2]}
Vitórias: {dados[0][-2]}
Derrotas: {dados[0][-1]}
""")

        conexao.commit()

        cursor.close()
        conexao.close()
