from tkinter import *




# difinições
from tkinter import Label

programa = Tk()
programa.title('nome da aplicação')
programa.geometry("500x500")




#criando função:
def coletar_dados():
    #coletando informações
    nome = entrada_nome.get()
    idade = entrada_idade.get()
    residencia = entrada_residencia.get()

    #transformando texto em dado:
    nome_saida['text']= nome
    idade_saida['text'] = idade
    residencia_saida['text'] = residencia






#campo texto nome:
label_nome = Label(programa, width=10, height=2, text='Nome')
label_nome.grid(row=1, column=2)

#campo texto idade:
label_idade = Label(programa, width=10,height=2, text='Idade')
label_idade.grid(row=2, column=2)

#campo localização:
label_localiza = Label(programa, width=10, height=2, text='Residência')
label_localiza.grid(row=3,column=2)






#campos de entrada

#entrada nome:
entrada_nome = Entry(programa, width=30, font=('Arial 10'))
entrada_nome.grid(row=1, column=3)

#entrada Idade:
entrada_idade = Entry(programa, width=30, font=('Arial 10'))
entrada_idade.grid(row=2, column=3)

#Entrada Residência:
entrada_residencia = Entry(programa, width=30, font="Arial 10")
entrada_residencia.grid(row=3, column=3)





#campos de saida:

#saida nome
nome_saida = Label(programa, width=10, font="Arial 10", text="saida_nome")
nome_saida.grid(row=1, column=4)

#saida idade
idade_saida = Label(programa, width=10, font='Arial 10', text='saida_idade')
idade_saida.grid(row=2, column=4)

#saida residencia
residencia_saida = Label(programa, width=10, font='Arial 10', text='saida_resid')
residencia_saida.grid(row=3, column=4)







#criando botão para executar função
botao_dado = Button(programa, command=coletar_dados, text="Confirmar", width=25, height=3, relief='raised', fg='#000')
botao_dado.grid(row=6, column=3)


#criando botão apagar
botao_apagar = Button(programa, command=programa.quit, text='Fechar Programa', width=25, height=3, relief='raised', fg='#000')
botao_apagar.grid(row=8, column=3)


#lop que executa a aplicação
programa.mainloop()