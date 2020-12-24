from main import *


################# tkcalendar ###############
from tkcalendar import Calendar, DateEntry
from datetime import date


def sales():

	######################### Tab master ################################

	tab_control = ttk.Notebook(frame_main,width=1245, height=6805)

	tab1 = ttk.Frame(tab_control)
	tab2 = ttk.Frame(tab_control)
	tab3 = ttk.Frame(tab_control)
	tab4 = ttk.Frame(tab_control)
	tab5 = ttk.Frame(tab_control)
	tab6 = ttk.Frame(tab_control)

	
	tab_control.add(tab1, text='Quotation')
	tab_control.add(tab2, text='Order Confirmation')
	tab_control.add(tab3, text='Proforma Invoice ')
	tab_control.add(tab4, text='Invoice')
	tab_control.add(tab5, text='Credit Note')
	tab_control.add(tab6, text='Debit Note')

	tab_control.place(x=2, y=0)

	
	def app_quatation_frame():

	    app_name = Label(tab1, text="Quatation Details", width=150,height=1,pady=7, padx=5, relief="flat", anchor=NW, font=('Helvetica 10 '), bg=co9, fg=co1)
	    app_name.grid(row=0, column=0, sticky=NSEW, padx=0, columnspan=2)

	    frame_top = Frame(tab1, width=1245,height=545, relief="flat",)
	    frame_top.grid(row=1, column=0, sticky=NSEW, padx=300, pady=15)
	    
	    frame_direita = Frame(tab1, width=545, height=500,  relief="flat",)
	    frame_direita.grid(row=2, column=0, sticky=NSEW, padx=90, pady=22)

	    ##### dividindo o frame esquerdo em duas partes,cima e baixo ######
	    frame_e_cima = Frame(frame_top, width=1245,height=40,  relief="flat",)
	    frame_e_cima.grid(row=0, column=0, sticky=NSEW, padx=5)
	    
	    frame_e_baixo = Frame(frame_top, width=1245,height=150,  relief="flat",)
	    frame_e_baixo.grid(row=1, column=0, sticky=NSEW, padx=5, pady=15)

	    ### função main #####

	    def main(a):

	        ############## New #############
	        if a == 'new':
	            
	            for widget in frame_e_baixo.winfo_children():
	                widget.destroy()
	            
	            def novo_categoria():
	            
	                valores = [e_nome.get()]
	                
	                if e_nome.get()=='':
	                    messagebox.showerror('Erro', 'Preencha todos os campos')
	                else:
	                    inserir_categoria(valores)

	                    messagebox.showinfo(
	                        'Sucesso', 'Os dados foram inseridos com sucesso')

	                    for widget in frame_e_baixo.winfo_children():
	                        widget.destroy()

	                    mostrar()

	            app_nome = Label(frame_e_baixo, text="+ Adicionar categoria", height=1,
	                     pady=15, padx=5, relief="flat", anchor=NW, font=('Helvetica 13 bold'),  fg=co4)
	            app_nome.grid(row=0, column=0, sticky=NSEW, padx=0, columnspan=2)
	            
	            l_nome = Label(frame_e_baixo, text="Nome", height=1,
	                            pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), fg=co4)
	            l_nome.grid(row=1, column=0, sticky=NSEW, padx=5, pady=5)
	            e_nome = Entry(frame_e_baixo, width=30, justify='center')
	            e_nome.grid(row=1, column=1, sticky=NSEW,
	                         padx=5, pady=5, ipady=0)

	            l_nome = Label(frame_e_baixo, text="", height=1,
	                            pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'),  fg=co4)
	            l_nome.grid(row=2, column=0, sticky=NSEW, padx=5, pady=7)

	            botao_confirmar = Button(frame_e_baixo, text="Confirmar", width=10, height=1, bg=co2, fg=co1,
	                                     font=('Ivy 7 bold'), relief=RAISED, overrelief=RIDGE)
	            botao_confirmar.grid(row=1, column=2, sticky=E, padx=5, pady=5)
	            
	            
	        ############## list #############
	        if a == 'list':
	            
	            for widget in frame_e_baixo.winfo_children():
	                widget.destroy()
	            
	            def actualizar_cat():
	            
	                valores = [e_titlo.get(), e_autor.get(), e_editora.get(),e_categoria.get(),e_copias.get()]
	                
	                if e_titlo.get()=='' or e_autor.get()=='' or e_editora.get()=='' or e_categoria.get()=='' or e_copias.get()=='':
	                    messagebox.showerror('Erro', 'Preencha todos os campos')
	                else:
	                    inserir_livro(valores)

	                    messagebox.showinfo(
	                        'Sucesso', 'Os dados foram inseridos com sucesso')

	                    for widget in frame_e_baixo.winfo_children():
	                        widget.destroy()

	                    mostrar()

	            app_nome = Label(frame_e_baixo, text="+ Actualizar categoria", height=1,
	                     pady=15, padx=5, relief="flat", anchor=NW, font=('Helvetica 13 bold'),  fg=co4)
	            app_nome.grid(row=0, column=0, sticky=NSEW, padx=0, columnspan=2)
	            
	            l_selecione = Label(frame_e_baixo, text="Selecionar categoria", height=1,
	                            pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'),  fg=co4)
	            l_selecione.grid(row=1, column=0, sticky=NSEW, padx=5, pady=5)
	           
	            b_escolher = ttk.Combobox(frame_e_baixo, width=15, font=('Ivy 10 bold'))
	            b_escolher['values'] = ['Romance','Desenho','Historia']
	            b_escolher.grid(row=1, column=1, sticky=NSEW, padx=5, pady=5, ipady=0)

	            l_nome = Label(frame_e_baixo, text="Novo nome", height=1,
	                                pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'),  fg=co4)
	            l_nome.grid(row=1, column=2, sticky=E, padx=20, pady=5)
	            e_nome = Entry(frame_e_baixo, width=20, justify='center')
	            e_nome.grid(row=1, column=3, sticky=E,
	                             padx=5, pady=5, ipady=0)

	            botao_confirmar = Button(frame_e_baixo, text="Confirmar", width=10, height=1, bg=co2, fg=co1,
	                                     font=('Ivy 7 bold'), relief=RAISED, overrelief=RIDGE)
	            botao_confirmar.grid(row=3, column=3, sticky=E, padx=5, pady=5)

	        ############## Deletar categoria #############
	        if a == 'clear':
	            
	            for widget in frame_e_baixo.winfo_children():
	                widget.destroy()
	            
	            def deletar_cat():
	            
	                valores = [e_titlo.get(), e_autor.get(), e_editora.get(),e_categoria.get(),e_copias.get()]
	                
	                if e_titlo.get()=='' or e_autor.get()=='' or e_editora.get()=='' or e_categoria.get()=='' or e_copias.get()=='':
	                    messagebox.showerror('Erro', 'Preencha todos os campos')
	                else:
	                    inserir_livro(valores)

	                    messagebox.showinfo(
	                        'Sucesso', 'Os dados foram inseridos com sucesso')

	                    for widget in frame_e_baixo.winfo_children():
	                        widget.destroy()

	                    mostrar()

	            app_nome = Label(frame_e_baixo, text="- Deletar categoria", height=1,
	                     pady=15, padx=5, relief="flat", anchor=NW, font=('Helvetica 13 bold'),  fg=co4)
	            app_nome.grid(row=0, column=0, sticky=NSEW, padx=0, columnspan=2)
	            
	            l_selecione = Label(frame_e_baixo, text="Selecionar categoria", height=1,
	                            pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), fg=co4)
	            l_selecione.grid(row=1, column=0, sticky=NSEW, padx=5, pady=5)
	           
	            b_escolher = ttk.Combobox(frame_e_baixo, width=15, font=('Ivy 10 bold'))
	            b_escolher['values'] = ['Romance','Desenho','Historia']
	            b_escolher.grid(row=1, column=1, sticky=NSEW, padx=5, pady=5, ipady=0)

	            l_nome = Label(frame_e_baixo, text="Ao deletar uma categoria, todos os livros associados a ela tambem serao deletadas", height=1,
	                                pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'),  fg=co4)
	            l_nome.grid(row=2, column=0, sticky=E, padx=20, pady=5)
	            

	            botao_confirmar = Button(frame_e_baixo, text="Confirmar", width=10, height=1, bg=co2, fg=co1,
	                                     font=('Ivy 7 bold'), relief=RAISED, overrelief=RIDGE)
	            botao_confirmar.grid(row=3, column=1, sticky=E, padx=5, pady=5)


	        ############## export ########

	        if a == 'exportr':
	            for widget in frame_e_baixo.winfo_children():
	                widget.destroy()
	            try:
	                treev_itens = tree.focus()
	                treev_dicionario = tree.item(treev_itens)
	                treev_lista = treev_dicionario['values']
	                valor = treev_lista[0]
	                
	                
	                app_nome = Label(frame_e_baixo, text="Atualizar livros", height=1,
	                     pady=15, padx=5, relief="flat", anchor=NW, font=('Helvetica 13 bold'),  fg=co4)
	                app_nome.grid(row=0, column=0, sticky=NSEW, padx=0, columnspan=2)
	                
	                l_titlo = Label(frame_e_baixo, text="Titlo", height=1,
	                                pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'),  fg=co4)
	                l_titlo.grid(row=1, column=0, sticky=NSEW, padx=5, pady=5)
	                e_titlo = Entry(frame_e_baixo, width=30, justify='center')
	                e_titlo.grid(row=1, column=1, sticky=NSEW,
	                            padx=5, pady=5, ipady=0)

	                l_autor = Label(frame_e_baixo, text="Autor", height=1,
	                                pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'),  fg=co4)
	                l_autor.grid(row=2, column=0, sticky=NSEW, padx=5, pady=5)
	                e_autor = Entry(frame_e_baixo, width=20, justify='center')
	                e_autor.grid(row=2, column=1, sticky=NSEW,
	                            padx=5, pady=5, ipady=0)

	                l_editora = Label(frame_e_baixo, text="Editora", height=1,
	                                pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'),  fg=co4)
	                l_editora.grid(row=3, column=0, sticky=NSEW, padx=5, pady=5)
	                e_editora = Entry(frame_e_baixo, width=20, justify='center')
	                e_editora.grid(row=3, column=1, sticky=NSEW,
	                            padx=5, pady=5, ipady=0)

	                l_categoria = Label(frame_e_baixo, text="Categoria", height=1,
	                                    pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'),  fg=co4)
	                l_categoria.grid(row=1, column=2, sticky=E, padx=20, pady=5)
	                e_categoria = Entry(frame_e_baixo, width=20, justify='center')
	                e_categoria.grid(row=1, column=3, sticky=E,
	                                padx=5, pady=5, ipady=0)

	                l_copias = Label(frame_e_baixo, text="No. copias", height=1,
	                                pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'),  fg=co4)
	                l_copias.grid(row=2, column=2, sticky=E, padx=20, pady=5)
	                e_copias = Entry(frame_e_baixo, width=20, justify='center')
	                e_copias.grid(row=2, column=3, sticky=E,
	                            padx=5, pady=5, ipady=0)

	                botao_confirmar = Button(frame_e_baixo, text="Confirmar", width=10, height=1, bg=co2, fg=co1,
	                                        font=('Ivy 7 bold'), relief=RAISED, overrelief=RIDGE)
	                botao_confirmar.grid(row=3, column=3, sticky=E, padx=5, pady=5)

	            except IndexError:
	                messagebox.showerror(
	                    'Erro', 'Seleciona um dos dados na tabela')

	   

	    ##### Top buttons  ########
	   
	    b_novo_cat = Button(frame_e_cima, text="New", width=15, height=1, bg=co3, fg="white",
	                        font=('Ivy 8 bold'), anchor="center", relief=RAISED, command=lambda: main('new'))
	    b_novo_cat.grid(row=0, column=0,  sticky=NSEW, pady=1, padx=3)
	    
	    
	    b_remover_cat = Button(frame_e_cima, text="List", width=15, height=1, bg=co3, fg="white",
	                           font=('Ivy 8 bold'), anchor="center", relief=RAISED, command=lambda: main('list'))
	    b_remover_cat.grid(row=0, column=1,  sticky=NSEW, pady=1, padx=3)


	    b_novo = Button(frame_e_cima, text="Clear", width=15, height=1, bg=co3, fg="white",
	                    font=('Ivy 8 bold'), anchor="center", relief=RAISED, command=lambda: main('clear'))
	    b_novo.grid(row=0, column=2,  sticky=NSEW, pady=1, padx=3)

	    b_remover = Button(frame_e_cima, text="Export", width=15, height=1, bg=co3,
	                       fg="white", font=('Ivy 8 bold'), anchor="center", relief=RAISED, command=lambda: main('export'))
	    b_remover.grid(row=0, column=3,  sticky=NSEW, pady=1, padx=3)

	    

	    ################# frame tree ####################

	    # creating a treeview with dual scrollbars
	    list_header = ['Action','Serial No.',  'QTN Type',
	                   'QTN No.', 'QTN Date', 'Custumer Name','QTN Amount','Cancelled?','Cancelled Date']

	    df_list = [
	    		   ['test data',12347, 'type data', 343, '12/19/2010', 'custumer data name',"500010",'NO','12/19/2010'], 
	               ['test data',12347, 'type data', 343, '12/19/2010', 'custumer data name',"500010",'NO','12/19/2010'],
	               ['test data',12347, 'type data', 343, '12/19/2010', 'custumer data name',"500010",'NO','12/19/2010'],
	               ['test data',12347, 'type data', 343, '12/19/2010', 'custumer data name',"500010",'NO','12/19/2010'],
	               ['test data',12347, 'type data', 343, '12/19/2010', 'custumer data name',"500010",'NO','12/19/2010'],
	               ]

	    tree = ttk.Treeview(frame_direita, selectmode="extended",
	                        columns=list_header, show="headings")
	    # vertical scrollbar
	    vsb = ttk.Scrollbar(
	        frame_direita, orient="vertical", command=tree.yview)
	    # horizontal scrollbar
	    hsb = ttk.Scrollbar(
	        frame_direita, orient="horizontal", command=tree.xview)

	    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

	    tree.grid(column=0, row=0, sticky='nsew')
	    vsb.grid(column=1, row=0, sticky='ns')
	    hsb.grid(column=0, row=1, sticky='ew')
	    frame_direita.grid_rowconfigure(0, weight=2)
	    
	    hd=["center","center","center","center","center","center","center","center",'center']
	    h=[90,70,140,90,140,140,100,100,100]
	    n=0
	    
	    for col in list_header:
	        tree.heading(col, text=col.title(), anchor=CENTER)
	        # adjust the column's width to the header string
	        tree.column(col, width=h[n],anchor=hd[n])
	        
	        n+=1

	    for item in df_list:
	        tree.insert('', 'end', values=item)

	app_quatation_frame()

		
