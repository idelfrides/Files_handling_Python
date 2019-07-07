
import BlocoDeNotas as Bn
import time as t

def bloco_notas():
    bnobj = Bn.BlocoDeNotas()
    bnobj.app_info()
    bnobj.prepare2list()

    if bnobj.lista_notas.__len__() is 0:
        print('\n ************************************'
              '\n\t WARNING: NOTAS NAO REGISTRADA.'
              '\n ************************************')
        t.sleep(3)
        print('\n\t Nenhuma nota foi encontrada.'
              '\n\t Crie um nova pra operar. '
              '\n\t No menu a seguir escolhe opcao CREATE \n')
        t.sleep(5)
        opcao = bnobj.menu_create()
        if opcao is 1:  # 1 -> create a note
            bnobj.oper_info(1, 'obama')
            bnobj.create()  # 1 -> create
            bnobj.prepare2list()
        elif opcao is 0:  # 2 -> read a note
            print('\n\t  O SR(A) escolheu SAIR. \n\t Aplicao sera encerrada.\n\n')
            t.sleep(3)
            exit(0)
        else:
            pass
    else:
        pass

    run = True
    while run is True:
        code_note = bnobj.list_note()
        if code_note >= 1 and code_note <= bnobj.tam:  # one note chosed
            name_note = bnobj.lista_notas[code_note-1]
            bnobj.show_choice(name_note)
            bnobj.making_operations(code_note, name_note)
            return bloco_notas()
        elif code_note is bnobj.tam + 1:  # go to create a new note
            bnobj.oper_info(1, 'Obama')
            bnobj.create()
            t.sleep(2)
            bnobj.reset_all()
            bnobj.prepare2list()
        elif code_note is 0 :   # 0 -> quit the app
            print('\n  O SR(A) escolheu SAIR. \n Aplicao sera encerrada.\n\n')
            t.sleep(4)
            exit(0)
        else:
            run = False



bloco_notas()