
import glob, os
import time as t
# from datetime import date

class BlocoDeNotas(object):
    zero = 0
    one = 1
    two = 2
    tree = 3
    four = 4
    five = 5
    lista_notas = []
    tam = -1

    def __init__(self):
        self.reset_all()

    def app_info(self):
        print('\n\n  ==========================================='
              '\n\t This app work with files \n'
              '\t It´s make a CRUD operations on files.'
              '\n  ===========================================')

    def prepare2list(self):
        self.change_dir(2)  # to folder notes
        for arquivo in glob.glob('*.txt'):
            self.lista_notas.append(arquivo)

        self.change_dir(1)  # to root project


    def list_note(self):
        print('\n\n MENU DAS NOTAS EXISTENTES \n')
        index = 1
        opcao = -1
        self.tam = self.lista_notas.__len__()
        n = self.tam
        for nota in range(n):  # 0 ate tam-1
            print('\n [{}] {} '.format(index, self.lista_notas[nota]))
            index = index + 1
        print('\n [{}] CREATE'.format(n + 1))
        print('\n [0] SAIR')

        help_me = True
        while help_me is True:
            try:
                opcao = int(input('\n\n Escolha uma nota pra operar: '))
                if opcao >= 0 and opcao <= n + 1:
                    print('\n OPCAO VALIDA \n')
                    help_me = False
                else:
                    print('\n\n ******************************************'
                          '\n WARNING:'
                          '\n Tipo de opracao invalido!! '
                          '\n Escolhe um tipo listado a seguir ')
                    print('\n OPCAO ERRADA:  {}'.format(opcao))
                    print('*******************************************')
                    help_me = True
            except Exception as error_type:
                if opcao < 0 or type(opcao) is str:
                    print('\n\n ******************************************'
                          '\n WARNING:'
                          '\n Tipo de opracao invalido!! '
                          '\n Escolhe um tipo listado a seguir ')
                    print('\n TIPO DE ERRO: \n  {}'.format(error_type))
                    print('*******************************************')
                else:

                    help_me = False
        return opcao

    def menu_operations(self):
        op_oper = -1
        print('\n\n MENU DE OPERACOES CRUD\n\n '
              '1 -> READ \n '
              '2 -> UPDATE | REPLACE \n '
              '3 -> UPDATE | ADD \n '
              '4 -> DELETE \n '
              '5 -> VOLTAR')

        help_me = True
        while help_me is True:
            try:
                op_oper = int(input('\n Escolha uma operacao:  '))
                if op_oper >= 1 and op_oper <= 5:
                    print('\n OPCAO VALIDA \n')
                    help_me = False
                else:
                    print('\n\n ******************************************'
                          '\n WARNING:'
                          '\n Tipo de opracao invalido!! '
                          '\n Escolhe um tipo listado a seguir ')
                    print('\n OPCAO ERRADA:  {}'.format(op_oper))
                    print('*******************************************')
                    help_me = True
            except Exception as erro_tipo:
                if op_oper < 0 or op_oper > 5:
                    print('\n\n ******************************************'
                          '\n WARNING:'
                          '\n Tipo de opracao invalido!! '
                          '\n Escolhe um tipo listado a seguir ')
                    print('\n TIPO DE ERRO: \n  {}'.format(erro_tipo))
                    print('*******************************************')
                else:
                    help_me = False
            help_me = False  # get out from the while loop
        return op_oper

    def menu_create(self):
        op_oper = -1
        print('\n\n MENU DE OPERACAO CREATE \n\n ')
        print('{} -> CREATE '.format(self.one))
        print('{} -> SAIR '.format(self.zero))

        help_me = True
        while help_me is True:
            try:
                op_oper = int(input('\n Escolha uma opcao:  '))
                if op_oper is self.zero or op_oper is self.one:
                    print('\n OPCAO VALIDA \n')
                    help_me = False
                else:
                    print('\n\n ******************************************'
                          '\n WARNING:'
                          '\n Tipo de opracao invalido!! '
                          '\n Escolhe um tipo listado a seguir ')
                    print('\n OPCAO ERRADA:  {}'.format(op_oper))
                    print('*******************************************')
                    help_me = True
            except Exception as erro_tipo:
               # print('valor de entrada {}'.format(op_oper))
                if type(op_oper) is str or op_oper < self.zero:
                    print('\n\n ******************************************'
                          '\n WARNING:'
                          '\n Tipo de opracao invalido!! '
                          '\n Escolhe um tipo listado a seguir ')
                    print('\n TIPO DE ERRO: \n  {}'.format(erro_tipo))
                    print('*******************************************')
                    help_me = True
                else:
                    pass
            #help_me = False  # get out from the while loop
        return op_oper

    def create(self):
        # data_hoje = date.today()
        hour = t.asctime()
        name = input('\n Note name: ')
        name_note = name + '.txt'
        self.change_dir(2)
        try:
            arq = open(name_note, 'w', encoding="utf-8")
            text = input('\n Entry your note(Text): ')
            text = text + '\n'
            tags = input('\n Your tags:  ')
            tags = tags + '\n'
            arq.writelines(text)
            arq.writelines(tags)
            arq.write(hour)
            arq.close()
            self.feedback()
            self.change_dir(1)
            return
        except Exception as erro:
            print('\n A error ocorred when loadoing the file --> {}.'.format(name_note))
            print('\n This is the error: {}'.format(erro))

    def read(self, ind_nota):
        nome_nota = self.lista_notas[ind_nota]
        self.change_dir(2)
        try:
            arq = open(nome_nota, 'r', encoding="utf-8")
            for linha in arq:
                print(linha)
            # arq.readline()
            # arq.writelines(tags)
            # arq.write(hora)
            arq.close()
            self.change_dir(1)
        except Exception as erro:
            print('\n Ocorreu um erro ao abrir o arquivo de notas.')
            print('\n O erro é: {}'.format(erro))

    def update_replace(self,ind_nota):
        hora = t.asctime()
        nome_nota = self.lista_notas[ind_nota]
        self.change_dir(2)
        try:
            # delete the content inside the file
            arq = open(nome_nota, 'w', encoding="utf-8")
            arq.close()

            arq = open(nome_nota, 'w', encoding="utf-8")
            texto = input('\n Sua nova nota: ')
            texto = texto + '\n'
            tags = input('\n As tags da nova nota:  ')
            tags = tags + '\n'

            arq.writelines(texto)
            arq.writelines(tags)
            arq.write(hora)
            arq.close()
            self.feedback()
            self.change_dir(1)
            return
        except Exception as erro:
            print('\n Ocorreu um erro ao carregar o arquivo.')
            print('\n O erro é: {}'.format(erro))

    def update_add(self, ind_nota):
        hora = t.asctime()
        nome_nota = self.lista_notas[ind_nota]
        self.change_dir(2)
        try:
            arq = open(nome_nota, 'w', encoding="utf-8")
            arq.close()

            arq = open(nome_nota, 'w', encoding="utf-8")
            texto = input('\n Sua nova nota: ')
            texto = texto + '\n'
            tags = input('\n As tags da nova nota:  ')
            tags = tags + '\n'

            arq.writelines(texto)
            arq.writelines(tags)
            arq.write(hora)
            arq.close()
            self.change_dir(1)
            return
        except Exception as erro:
            print('\n Ocorreu um erro ao carregar o arquivo.')
            print('\n O erro é: {}'.format(erro))

    def delete(self, ind_nota):
        note = self.lista_notas[ind_nota]
        self.change_dir(2)
        this_project = glob.glob('*.txt')
        # print(this_project)
        try:
            if note in this_project:
                os.unlink(note)
                # os.remove('{}/{}'.format(mypath, note))
                print('\n A nota {} foi deletada com Sucesso'.format(note))
                print('\n Escolha a opcao CREATE para cirar uma nova nota ou '
                      '\n opcao VOLTAR para escolher outra nota e trabalhar ')
                self.change_dir(1)
            else:
                self.change_dir(1)
        except Exception as erro:
            print('\n Ocorreu um erro ao remover a nota {}'.format(note))
            print('\n O erro é: {}'.format(erro))

    def show_choice(self, note_name):
        print('\n\n ===========================================')
        print('\n\t\t    CHOSEN NOTE \n\n\t\t\t {}'.format(note_name))
        print('\n ===========================================')

    def feedback(self):
        print('\n\n -------------------------------------------')
        print('\n\t    OPERATION DONE SUCCESSFULLY')
        print('\n -------------------------------------------')

    def oper_info(self, code_op, note_name):
        if code_op is 1:
            print('\n ===========================================')
            print('\t    CREATING A NEW NOTE  ')
            print(' =========================================== \n')
        elif code_op is 2:
            print('\n ===========================================')
            print('\t    READING THE NOTE {}'.format(note_name))
            print(' ===========================================\n')
        elif code_op is 3:
            print('\n ===========================================')
            print('\t    UPDATEING NOTE  {}'.format(note_name))
            print(' ===========================================\n')
        elif code_op is 4:
            print('\n ===========================================')
            print('\t    REMOVING NOTE:  {}'.format(note_name))
            print(' ===========================================\n')

    def reset_all(self):
        # print('\n I AM RESET ALL METHOD \n')
        self.lista_notas.clear()

    def making_operations(self, code_note, name_note):
        # choice one operation mode
        real_oper = True
        while real_oper is True:
            opcao = self.menu_operations()
            if opcao is 1:  # 2 -> read a note
                self.oper_info(2, name_note)
                self.read(code_note - 1)
                self.make_line()
            elif opcao is 2:  # 3 -> update - replace
                self.oper_info(3, name_note)
                self.update_replace(code_note - 1)  # 3 -> replace the old content
            elif opcao is 3:  # 4 -> update - add
                self.oper_info(3, name_note)
                self.update_add(code_note - 1)  # 2 -> alterar p/ adicionar
            elif opcao is 4:  # 5 -> delete
                self.oper_info(4, name_note)
                self.delete(code_note - 1)  # 2 -> delete the note
            elif opcao is 5:  # 6 -> VOLTAR
                print('\n  O SR(A) escolheu VOLTAR. \n\n')
                t.sleep(3)
                real_oper = False
            else:
                pass
        return

    def change_dir(self, code):
        if code is 1: # root dir
            current_dir = os.path.dirname(os.path.abspath(__file__))
            os.chdir(current_dir)
        elif code is 2: # folder notes
            os.chdir('notes')
        else:
            pass

    def get_cwd(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        # current_dir = os.getcwd()
        return current_dir