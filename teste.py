
import tkinter as tk

import random


bandeiras = [
    ("Andorra", "ad.png"),
    ("EAU", "ae.png"),
    ("Afeganistão", "af.png"),
    ("Antígua Barbuda", "ag.png"),
    ("Anguila", "ai.png"),
    ("Albânia", "al.png"),
    ("Armênia", "am.png"),
    ("Angola", "ao.png"),
    ("Argentina", "ar.png"),
    ("Samoa Americana", "as.png"),
    ("Áustria", "at.png"),
    ("Austrália", "au.png"),
    ("Aruba", "aw.png"),
    ("Azerbaijão", "az.png"),
    ("Bósnia e Herzegovina", "ba.png"),
    ("Barbados", "bb.png"),
    ("Bangladesh", "bd.png"),
    ("Bélgica", "be.png"),
    ("Burkina Faso", "bf.png"),
    ("Bulgária", "bg.png"),
    ("Bahrein", "bh.png"),
    ("Burundi", "bi.png"),
    ("Benin", "bj.png"),
    ("Bermudas", "bm.png"),
    ("Brunei", "bn.png"),
    ("Bolívia", "bo.png"),
    ("Brasil", "br.png"),
    ("Bahamas", "bs.png"),
    ("Butão", "bt.png"),
    ("Botsuana", "bw.png"),
    ("Bielorrússia", "by.png"),
    ("Belize", "bz.png"),
    ("Canadá", "ca.png"),
    ("RD Congo", "cd.png"),
    ("Centro-Africana", "cf.png"),
    ("República do Congo", "cg.png"),
    ("Suíça", "ch.png"),
    ("Costa do Marfim", "ci.png"),
    ("Ilhas Cook", "ck.png"),
    ("Chile", "cl.png"),
    ("Camarões", "cm.png"),
    ("China", "cn.png"),
    ("Colômbia", "co.png"),
    ("Costa Rica", "cr.png"),
    ("Cuba", "cu.png"),
    ("Cabo Verde", "cv.png"),
    ("Curaçao", "cw.png"),
    ("Chipre", "cy.png"),
    ("Tchéquia", "cz.png"),
    ("Alemanha", "de.png"),
    ("Djibuti", "dj.png"),
    ("Dinamarca", "dk.png"),
    ("Dominica", "dm.png"),
    ("República Dominicana", "do.png"),
    ("Argélia", "dz.png"),
    ("Equador", "ec.png"),
    ("Estônia", "ee.png"),
    ("Egito", "eg.png"),
    ("Saara Ocidental", "eh.png"),
    ("Eritreia", "er.png"),
    ("Espanha", "es.png"),
    ("Etiópia", "et.png"),
    ("Finlândia", "fi.png"),
    ("Fiji", "fj.png"),
    ("Micronésia", "fm.png"),
    ("Ilhas Faroe", "fo.png"),
    ("França", "fr.png"),
    ("Gabão", "ga.png"),
    ("Inglaterra", "gb-eng.png"),
    ("Irlanda do Norte", "gb-nir.png"),
    ("Escócia", "gb-sct.png"),
    ("País de Gales", "gb-wls.png"),
    ("Reino Unido", "gb.png"),
    ("Granada", "gd.png"),
    ("Geórgia", "ge.png"),
    ("Guiana Francesa", "gf.png"),
    ("Gana", "gh.png"),
    ("Gibraltar", "gi.png"),
    ("Gâmbia", "gm.png"),
    ("Guiné", "gn.png"),
    ("Guadalupe", "gp.png"),
    ("Guiné Equatorial", "gq.png"),
    ("Grécia", "gr.png"),
    ("Guatemala", "gt.png"),
    ("Guam", "gu.png"),
    ("Guiné-Bissau", "gw.png"),
    ("Guiana", "gy.png"),
    ("Hong Kong", "hk.png"),
    ("Honduras", "hn.png"),
    ("Croácia", "hr.png"),
    ("Haiti", "ht.png"),
    ("Hungria", "hu.png"),
    ("Indonésia", "id.png"),
    ("Irlanda", "ie.png"),
    ("Israel", "il.png"),
    ("Índia", "in.png"),
    ("Iraque", "iq.png"),
    ("Irã", "ir.png"),
    ("Islândia", "is.png"),
    ("Itália", "it.png"),
    ("Jamaica", "jm.png"),
    ("Jordânia", "jo.png"),
    ("Japão", "jp.png"),
    ("Quênia", "ke.png"),
    ("Quirguistão", "kg.png"),
    ("Camboja", "kh.png"),
    ("Kiribati", "ki.png"),
    ("Comoros", "km.png"),
    ("Cristóvão e Névis", "kn.png"),
    ("Coreia do Norte", "kp.png"),
    ("Coreia do Sul", "kr.png"),
    ("Kuwait", "kw.png"),
    ("Ilhas Cayman", "ky.png"),
    ("Laos", "la.png"),
    ("Líbano", "lb.png"),
    ("Santa Lúcia", "lc.png"),
    ("Liechtenstein", "li.png"),
    ("Sri Lanka", "lk.png"),
    ("Libéria", "lr.png"),
    ("Lesoto", "ls.png"),
    ("Lituânia", "lt.png"),
    ("Luxemburgo", "lu.png"),
    ("Letônia", "lv.png"),
    ("Líbia", "ly.png"),
    ("Marrocos", "ma.png"),
    ("Mônaco", "mc.png"),
    ("Moldávia", "md.png"),
    ("Montenegro", "me.png"),
    ("São Martinho (França)", "mf.png"),
    ("Madagascar", "mg.png"),
    ("Ilhas Marshall", "mh.png"),
    ("Macedônia do Norte", "mk.png"),
    ("Mali", "ml.png"),
    ("Mianmar", "mm.png"),
    ("Mongólia", "mn.png"),
    ("Macau", "mo.png"),
    ("Mauritânia", "mr.png"),
    ("Montserrat", "ms.png"),
    ("Malta", "mt.png"),
    ("Maurício", "mu.png"),
    ("Maldivas", "mv.png"),
    ("Maláui", "mw.png"),
    ("México", "mx.png"),
    ("Malásia", "my.png"),
    ("Moçambique", "mz.png"),
    ("Namíbia", "na.png"),
    ("Nova Caledônia", "nc.png"),
    ("Níger", "ne.png"),
    ("Nigéria", "ng.png"),
    ("Nicarágua", "ni.png"),
    ("Países Baixos", "nl.png"),
    ("Noruega", "no.png"),
    ("Nepal", "np.png"),
    ("Nauru", "nr.png"),
    ("Niue", "nu.png"),
    ("Nova Zelândia", "nz.png"),
    ("Omã", "om.png"),
    ("Panamá", "pa.png"),
    ("Peru", "pe.png"),
    ("Polinésia Francesa", "pf.png"),
    ("Papua-Nova Guiné", "pg.png"),
    ("Filipinas", "ph.png"),
    ("Paquistão", "pk.png"),
    ("Polônia", "pl.png"),
    ("Porto Rico", "pr.png"),
    ("Palestina", "ps.png"),
    ("Portugal", "pt.png"),
    ("Palau", "pw.png"),
    ("Paraguai", "py.png"),
    ("Catar", "qa.png"),
    ("Romênia", "ro.png"),
    ("Sérvia", "rs.png"),
    ("Rússia", "ru.png"),
    ("Ruanda", "rw.png"),
    ("Arábia Saudita", "sa.png"),
    ("Ilhas Salomão", "sb.png"),
    ("Seicheles", "sc.png"),
    ("Sudão", "sd.png"),
    ("Suécia", "se.png"),
    ("Singapura", "sg.png"),
    ("Santa Helena", "sh.png"),
    ("Eslovênia", "si.png"),
    ("Eslováquia", "sk.png"),
    ("Serra Leoa", "sl.png"),
    ("San Marino", "sm.png"),
    ("Senegal", "sn.png"),
    ("Somália", "so.png"),
    ("Suriname", "sr.png"),
    ("Sudão do Sul", "ss.png"),
    ("Tomé e Príncipe", "st.png"),
    ("El Salvador", "sv.png"),
    ("Síria", "sy.png"),
    ("Turcas e Caicos", "tc.png"),
    ("Chade", "td.png"),
    ("Togo", "tg.png"),
    ("Tailândia", "th.png"),
    ("Tadjiquistão", "tj.png"),
    ("Tokelau", "tk.png"),
    ("Timor-Leste", "tl.png"),
    ("Tunísia", "tn.png"),
    ("Tonga", "to.png"),
    ("Turquia", "tr.png"),
    ("Trinidad Tobago", "tt.png"),
    ("Tuvalu", "tv.png"),
    ("Taiwan", "tw.png"),
    ("Tanzânia", "tz.png"),
    ("Ucrânia", "ua.png"),
    ("Uganda", "ug.png"),
    ("Estados Unidos", "us.png"),
    ("Uruguai", "uy.png"),
    ("Uzbequistão", "uz.png"),
    ("Vaticano", "va.png"),
    ("Vicente e Granadinas", "vc.png"),
    ("Venezuela", "ve.png"),
    ("IV Britânicas", "vg.png"),
    ("IV Americanas", "vi.png"),
    ("Vietnã", "vn.png"),
    ("Vanuatu", "vu.png"),
    ("Samoa", "ws.png"),
    ("Kosovo", "xk.png"),
    ("Iêmen", "ye.png"),
    ("África do Sul", "za.png"),
    ("Zâmbia", "zm.png"),
    ("Zimbábue", "zw.png")
]


bandeiras_faceis = [
    ("Brasil", "br.png"),
    ("Estados Unidos", "us.png"),
    ("Canadá", "ca.png"),
    ("Japão", "jp.png"),
    ("França", "fr.png"),
    ("Itália", "it.png"),
    ("Alemanha", "de.png"),
    ("Espanha", "es.png"),
    ("Reino Unido", "gb.png"),
    ("Argentina", "ar.png"),
    ("México", "mx.png"),
    ("China", "cn.png"),
    ("Rússia", "ru.png"),
    ("Índia", "in.png"),
    ("Austrália", "au.png"),
    ("Suíça", "ch.png"),
    ("Suécia", "se.png"),
    ("Noruega", "no.png"),
    ("Dinamarca", "dk.png"),
    ("Portugal", "pt.png"),
    ("Bélgica", "be.png"),
    ("Países Baixos", "nl.png"),
    ("Coreia do Sul", "kr.png"),
    ("Coreia do Norte", "kp.png"),
    ("Israel", "il.png"),
    ("Arábia Saudita", "sa.png"),
    ("Turquia", "tr.png"),
    ("Egito", "eg.png"),
    ("Grécia", "gr.png"),
    ("Irlanda", "ie.png"),
    ("Chile", "cl.png"),
    ("Colômbia", "co.png"),
    ("Peru", "pe.png"),
    ("Venezuela", "ve.png"),
    ("Ucrânia", "ua.png"),
    ("Polônia", "pl.png"),
    ("Catar", "qa.png"),
    ("Vietnã", "vn.png"),
    ("Jamaica", "jm.png"),
    ("África do Sul", "za.png")
]


bandeiras_medias = [
    ("Albânia", "al.png"),
    ("Angola", "ao.png"),
    ("Armênia", "am.png"),
    ("Azerbaijão", "az.png"),
    ("Bangladesh", "bd.png"),
    ("Bolívia", "bo.png"),
    ("Bahamas", "bs.png"),
    ("Butão", "bt.png"),
    ("Botsuana", "bw.png"),
    ("Bielorrússia", "by.png"),
    ("Bulgária", "bg.png"),
    ("Barbados", "bb.png"),
    ("Camarões", "cm.png"),
    ("Camboja", "kh.png"),
    ("Cabo Verde", "cv.png"),
    ("Chipre", "cy.png"),
    ("Croácia", "hr.png"),
    ("Estônia", "ee.png"),
    ("Finlândia", "fi.png"),
    ("Fiji", "fj.png"),
    ("Geórgia", "ge.png"),
    ("Gana", "gh.png"),
    ("Grécia", "gr.png"),
    ("Guatemala", "gt.png"),
    ("Haiti", "ht.png"),
    ("Hungria", "hu.png"),
    ("Indonésia", "id.png"),
    ("Irlanda do Norte", "gb-nir.png"),
    ("Escócia", "gb-sct.png"),
    ("País de Gales", "gb-wls.png"),
    ("Jordânia", "jo.png"),
    ("Quênia", "ke.png"),
    ("Quirguistão", "kg.png"),
    ("Laos", "la.png"),
    ("Líbano", "lb.png"),
    ("Lituânia", "lt.png"),
    ("Letônia", "lv.png"),
    ("Madagascar", "mg.png"),
    ("Malásia", "my.png"),
    ("Mongólia", "mn.png"),
    ("Moçambique", "mz.png"),
    ("Nepal", "np.png"),
    ("Nigéria", "ng.png"),
    ("Nova Zelândia", "nz.png"),
    ("Omã", "om.png"),
    ("Panamá", "pa.png"),
    ("Papua-Nova Guiné", "pg.png"),
    ("Filipinas", "ph.png"),
    ("Paquistão", "pk.png"),
    ("Paraguai", "py.png"),
    ("Romênia", "ro.png"),
    ("Sérvia", "rs.png"),
    ("Síria", "sy.png"),
    ("Tailândia", "th.png"),
    ("Trinidad Tobago", "tt.png"),
    ("Tunísia", "tn.png"),
    ("Tanzânia", "tz.png"),
    ("Uruguai", "uy.png"),
    ("Uzbequistão", "uz.png"),
    ("Vaticano", "va.png"),
    ("Vanuatu", "vu.png"),
    ("Zâmbia", "zm.png")
]

bandeiras_dificeis = [
    ("Andorra", "ad.png"),
    ("EAU", "ae.png"),
    ("Afeganistão", "af.png"),
    ("Antígua Barbuda", "ag.png"),
    ("Anguila", "ai.png"),
    ("Samoa Americana", "as.png"),
    ("Aruba", "aw.png"),
    ("Bósnia e Herzegovina", "ba.png"),
    ("Burkina Faso", "bf.png"),
    ("Bahrein", "bh.png"),
    ("Burundi", "bi.png"),
    ("Benin", "bj.png"),
    ("Bermudas", "bm.png"),
    ("Brunei", "bn.png"),
    ("Belize", "bz.png"),
    ("RD Congo", "cd.png"),
    ("Centro-Africana", "cf.png"),
    ("República do Congo", "cg.png"),
    ("Costa do Marfim", "ci.png"),
    ("Ilhas Cook", "ck.png"),
    ("Costa Rica", "cr.png"),
    ("Cuba", "cu.png"),
    ("Curaçao", "cw.png"),
    ("Djibuti", "dj.png"),
    ("Dominica", "dm.png"),
    ("República Dominicana", "do.png"),
    ("Saara Ocidental", "eh.png"),
    ("Eritreia", "er.png"),
    ("Etiópia", "et.png"),
    ("Micronésia", "fm.png"),
    ("Ilhas Faroe", "fo.png"),
    ("Gabão", "ga.png"),
    ("Granada", "gd.png"),
    ("Guiana Francesa", "gf.png"),
    ("Gibraltar", "gi.png"),
    ("Gâmbia", "gm.png"),
    ("Guiné", "gn.png"),
    ("Guadalupe", "gp.png"),
    ("Guiné Equatorial", "gq.png"),
    ("Guam", "gu.png"),
    ("Guiné-Bissau", "gw.png"),
    ("Guiana", "gy.png"),
    ("Hong Kong", "hk.png"),
    ("Honduras", "hn.png"),
    ("Comoros", "km.png"),
    ("Cristóvão e Névis", "kn.png"),
    ("Kuwait", "kw.png"),
    ("Ilhas Cayman", "ky.png"),
    ("Líbia", "ly.png"),
    ("Mônaco", "mc.png"),
    ("Moldávia", "md.png"),
    ("Montenegro", "me.png"),
    ("São Martinho (França)", "mf.png"),
    ("Ilhas Marshall", "mh.png"),
    ("Macedônia do Norte", "mk.png"),
    ("Mali", "ml.png"),
    ("Mianmar", "mm.png"),
    ("Macau", "mo.png"),
    ("Mauritânia", "mr.png"),
    ("Montserrat", "ms.png"),
    ("Malta", "mt.png"),
    ("Maurício", "mu.png"),
    ("Maldivas", "mv.png"),
    ("Maláui", "mw.png"),
    ("Namíbia", "na.png"),
    ("Nova Caledônia", "nc.png"),
    ("Níger", "ne.png"),
    ("Nicarágua", "ni.png"),
    ("Nauru", "nr.png"),
    ("Niue", "nu.png"),
    ("Omã", "om.png"),  # já nas médias — retirar se quiser
    ("Polinésia Francesa", "pf.png"),
    ("Palestina", "ps.png"),
    ("Palau", "pw.png"),
    ("Catar", "qa.png"),  # já nas fáceis
    ("Tomé e Príncipe", "st.png"),
    ("El Salvador", "sv.png"),
    ("Turcas e Caicos", "tc.png"),
    ("Chade", "td.png"),
    ("Togo", "tg.png"),
    ("Tadjiquistão", "tj.png"),
    ("Tokelau", "tk.png"),
    ("Timor-Leste", "tl.png"),
    ("Tonga", "to.png"),
    ("Tuvalu", "tv.png"),
    ("Taiwan", "tw.png"),
    ("Ilhas Salomão", "sb.png"),
    ("Seicheles", "sc.png"),
    ("San Marino", "sm.png"),
    ("Somália", "so.png"),
    ("Sudão", "sd.png"),
    ("Sudão do Sul", "ss.png"),
    ("Suriname", "sr.png"),
    ("Vicente e Granadinas", "vc.png"),
    ("IV Britânicas", "vg.png"),
    ("IV Americanas", "vi.png"),
    ("Vanuatu", "vu.png"),  # já nas médias
    ("Kosovo", "xk.png"),
    ("Iêmen", "ye.png"),
    ("Zimbábue", "zw.png")
]


#CLASSES

class Interface:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tela Inicial")

        # Tela cheia automática
        self.root.attributes('-fullscreen', True)
        
        #Foto do fundo
        self.imagem_mapa = tk.PhotoImage(file="fundo_oficial.png")
        
        self.label_mapa = tk.Label(self.root, image=self.imagem_mapa)
        self.canva_imagem_mapa_mundi = tk.Canvas(self.root, width=1440, height=900, highlightthickness=0, bd=0)
        self.canva_imagem_mapa_mundi.pack(fill="both")
        self.canva_imagem_mapa_mundi.create_image(720,450, image=self.imagem_mapa, anchor="center")
        
        #POSICIONAR AS BANDEIRAS COM O TITULO SENDO LABEL SERIA COMPLICADO, POR CONTA DO GLOBO E AS BANDEIRINHAS
        
        # Botão "Jogar" centralizado
        botao_jogar = tk.Button(self.root, text="QUIZ BANDEIRAS", font=("Luckiest Guy", 24),
                                fg="black", bg="white",width=15, height=1, command=self.Quiz)
        botao_jogar.place(relx=0.38, rely=0.76, anchor="center")
        
        # Botão "Sair" logo abaixo, com pequeno espaço
        botao_sair = tk.Button(self.root, text="SAIR", font=("Luckiest Guy", 24),
                               fg="black", bg="white", width=15, height=1, command=self.sair)
        botao_sair.place(relx=0.48, rely=0.83, anchor="center")
        
        # Botão "Flage" centralizado
        botao_Flagle = tk.Button(self.root, text="FLAGLE", font=("Luckiest Guy", 24),
                                fg="black", bg="white",width=15, height=1, command=self.Flagle)
        botao_Flagle.place(relx=0.59, rely=0.76, anchor="center")
    
        # mainloop deve vir no final
        self.root.mainloop()
        
        
    def Quiz(self):
        self.root.destroy()
        nova_janela = tk.Tk()
        self.app = Quiz(nova_janela)
        nova_janela.mainloop()
        
    def sair(self):
        self.root.destroy()
        
    def Flagle(self):
        self.root.destroy()
        self.nova_janela2 = tk.Tk()
        self.app2 = Flagle(self.nova_janela2)
        self.nova_janela2.mainloop()
    


class Quiz:
    def __init__(self, master):
        self.master = master
        self.master.title("Jogo das Bandeiras")
        
        # Tela cheia automática
        self.master.attributes('-fullscreen', True)
        
        #Foto do fundo
        self.imagem_fundo_2 = tk.PhotoImage(file="Fundo_quiz_flagle.png")
        self.label_mapa = tk.Label(self.master, image=self.imagem_fundo_2)
        self.label_mapa.place(relx=0.5, rely=0.5, anchor='center')


        #ESCOLHAS DIFICULDADES QUIZ
        self.botao_escolha_geral = tk.Button(self.master, text="GERAL", font=("Luckiest Guy", 24),
                                fg="black", bg="white",width=15, height=1, command=self.Quiz_geral)
        self.botao_escolha_geral.place(relx=0.5, rely=0.38, anchor="center")
        
        self.botao_dificuldade_facil = tk.Button(self.master, text="FÁCIL", font=("Luckiest Guy", 24),
                                fg="black", bg="white",width=15, height=1, command=self.Quiz_Facil)
        self.botao_dificuldade_facil.place(relx=0.5, rely=0.45, anchor="center")
        
        self.botao_dificuldade_medio = tk.Button(self.master, text="MÉDIO", font=("Luckiest Guy", 24),
                                fg="black", bg="white",width=15, height=1, command=self.Quiz_Medio)
        self.botao_dificuldade_medio.place(relx=0.5, rely=0.52, anchor="center")
        
        self.botao_dificuldade_dificil = tk.Button(self.master, text="DIFÍCIL", font=("Luckiest Guy", 24),
                                fg="black", bg="white",width=15, height=1, command=self.Quiz_Dificil)
        self.botao_dificuldade_dificil.place(relx=0.5, rely=0.59, anchor="center")
        
        # Botão para voltar à tela inicial
        self.botao_Sair = tk.Button(self.master, text="Sair" ,font=("Luckiest Guy", 24),
                          fg="black", bg="white", width=9, height=1, command=self.sair)
        self.botao_Sair.place(relx= 0.50, rely=0.8, anchor="center")
        
    def sair(self):
        root10 = self.master
        root10.destroy()
        Interface()  # Retorna à tela inicial

    def Quiz_geral(self):
        
        #DESTROIR BOTAO DE ESCOLHA DIFICULDADE
        self.botao_escolha_geral.destroy()
        self.botao_dificuldade_facil.destroy()
        self.botao_dificuldade_medio.destroy()
        self.botao_dificuldade_dificil.destroy()
        
        
        # ESCOLHENDO A BANDEIRA E OPCOES CERTAS E ERRADAS
        self.alternativa_certa, self.arquivo_certo = random.choice(bandeiras)
        erradas = [item for item in bandeiras if item[0] != self.alternativa_certa]
        self.opcoes_erradas = random.sample(erradas, 3)
    
        # JUNTA TODAS AS OPCOES E EMBARALHA
        opcoes = [self.alternativa_certa] + [e[0] for e in self.opcoes_erradas]
        random.shuffle(opcoes)
    
        # COLOCANDO A BANDEIRA NA TELA
        self.bandeira_tela = tk.PhotoImage(file=self.arquivo_certo)
    
        if "np" in self.arquivo_certo:
            self.bandeira_tela = self.bandeira_tela.subsample(1,1)
        else:
            self.bandeira_tela = self.bandeira_tela.subsample(2, 2)
    
        self.label_bandeira_tela = tk.Label(self.master, image=self.bandeira_tela, bd=0)
        self.label_bandeira_tela.place(relx=0.5, rely=0.33, anchor="center")
    
        # COLOCANDO OS 4 BOTÕES COM AS OPÇÕES
        self.botao_1 = tk.Button(self.master, text=opcoes[0], font=("Luckiest Guy", 20),
                          fg="black", bg="white", width=16, height=1,
                          command=lambda: self.ClickPais_GERAL(opcoes[0]))
        self.botao_2 = tk.Button(self.master, text=opcoes[1], font=("Luckiest Guy", 20),
                                  fg="black", bg="white", width=16, height=1,
                                  command=lambda: self.ClickPais_GERAL(opcoes[1]))
        self.botao_3 = tk.Button(self.master, text=opcoes[2], font=("Luckiest Guy", 20),
                                  fg="black", bg="white", width=16, height=1,
                                  command=lambda: self.ClickPais_GERAL(opcoes[2]))
        self.botao_4 = tk.Button(self.master, text=opcoes[3], font=("Luckiest Guy", 20),
                                  fg="black", bg="white", width=16, height=1,
                                  command=lambda: self.ClickPais_GERAL(opcoes[3]))
        
        # POSICIONANDO
        self.botao_1.place(relx=0.41, rely=0.60, anchor="center")
        self.botao_2.place(relx=0.59, rely=0.60, anchor="center")
        self.botao_3.place(relx=0.41, rely=0.68, anchor="center")
        self.botao_4.place(relx=0.59, rely=0.68, anchor="center")
    
        
    def Quiz_Facil(self):
        
        #DESTROIR BOTAO DE ESCOLHA DIFICULDADE
        self.botao_escolha_geral.destroy()
        self.botao_dificuldade_facil.destroy()
        self.botao_dificuldade_medio.destroy()
        self.botao_dificuldade_dificil.destroy()
        
        # ESCOLHENDO A BANDEIRA E OPCOES CERTAS E ERRADAS
        self.alternativa_certa, self.arquivo_certo = random.choice(bandeiras_faceis)
        erradas = [item for item in bandeiras_faceis if item[0] != self.alternativa_certa]
        self.opcoes_erradas = random.sample(erradas, 3)
    
        # JUNTA TODAS AS OPCOES E EMBARALHA
        opcoes = [self.alternativa_certa] + [e[0] for e in self.opcoes_erradas]
        random.shuffle(opcoes)
    
        # COLOCANDO A BANDEIRA NA TELA
        self.bandeira_tela = tk.PhotoImage(file=self.arquivo_certo)
    
        if "np" in self.arquivo_certo:
            self.bandeira_tela = self.bandeira_tela.subsample(1,1)
        else:
            self.bandeira_tela = self.bandeira_tela.subsample(2, 2)
    
        self.label_bandeira_tela = tk.Label(self.master, image=self.bandeira_tela, bd=0)
        self.label_bandeira_tela.place(relx=0.5, rely=0.33, anchor="center")
    
        # COLOCANDO OS 4 BOTÕES COM AS OPÇÕES
        self.botao_1 = tk.Button(self.master, text=opcoes[0], font=("Luckiest Guy", 20),
                          fg="black", bg="white", width=16, height=1,
                          command=lambda: self.ClickPais_FACIL(opcoes[0]))
        self.botao_2 = tk.Button(self.master, text=opcoes[1], font=("Luckiest Guy", 20),
                                  fg="black", bg="white", width=16, height=1,
                                  command=lambda: self.ClickPais_FACIL(opcoes[1]))
        self.botao_3 = tk.Button(self.master, text=opcoes[2], font=("Luckiest Guy", 20),
                                  fg="black", bg="white", width=16, height=1,
                                  command=lambda: self.ClickPais_FACIL(opcoes[2]))
        self.botao_4 = tk.Button(self.master, text=opcoes[3], font=("Luckiest Guy", 20),
                                  fg="black", bg="white", width=16, height=1,
                                  command=lambda: self.ClickPais_FACIL(opcoes[3]))
      
        # POSICIONANDO
        self.botao_1.place(relx=0.41, rely=0.60, anchor="center")
        self.botao_2.place(relx=0.59, rely=0.60, anchor="center")
        self.botao_3.place(relx=0.41, rely=0.68, anchor="center")
        self.botao_4.place(relx=0.59, rely=0.68, anchor="center")
    
    
    def Quiz_Medio(self):
        
        #DESTROIR BOTAO DE ESCOLHA DIFICULDADE
        self.botao_escolha_geral.destroy()
        self.botao_dificuldade_facil.destroy()
        self.botao_dificuldade_medio.destroy()
        self.botao_dificuldade_dificil.destroy()
        
        # ESCOLHENDO A BANDEIRA E OPCOES CERTAS E ERRADAS
        self.alternativa_certa, self.arquivo_certo = random.choice(bandeiras_medias)
        erradas = [item for item in bandeiras_medias if item[0] != self.alternativa_certa]
        self.opcoes_erradas = random.sample(erradas, 3)
    
        # JUNTA TODAS AS OPCOES E EMBARALHA
        opcoes = [self.alternativa_certa] + [e[0] for e in self.opcoes_erradas]
        random.shuffle(opcoes)
    
        # COLOCANDO A BANDEIRA NA TELA
        self.bandeira_tela = tk.PhotoImage(file=self.arquivo_certo)
    
        if "np" in self.arquivo_certo:
            self.bandeira_tela = self.bandeira_tela.subsample(1,1)
        else:
            self.bandeira_tela = self.bandeira_tela.subsample(2, 2)
    
        self.label_bandeira_tela = tk.Label(self.master, image=self.bandeira_tela, bd=0)
        self.label_bandeira_tela.place(relx=0.5, rely=0.33, anchor="center")
    
        # COLOCANDO OS 4 BOTÕES COM AS OPÇÕES
        self.botao_1 = tk.Button(self.master, text=opcoes[0], font=("Luckiest Guy", 20),
                          fg="black", bg="white", width=16, height=1,
                          command=lambda: self.ClickPais_MEDIO(opcoes[0]))
        self.botao_2 = tk.Button(self.master, text=opcoes[1], font=("Luckiest Guy", 20),
                                  fg="black", bg="white", width=16, height=1,
                                  command=lambda: self.ClickPais_MEDIO(opcoes[1]))
        self.botao_3 = tk.Button(self.master, text=opcoes[2], font=("Luckiest Guy", 20),
                                  fg="black", bg="white", width=16, height=1,
                                  command=lambda: self.ClickPais_MEDIO(opcoes[2]))
        self.botao_4 = tk.Button(self.master, text=opcoes[3], font=("Luckiest Guy", 20),
                                  fg="black", bg="white", width=16, height=1,
                                  command=lambda: self.ClickPais_MEDIO(opcoes[3]))
        
       
        # POSICIONANDO
        self.botao_1.place(relx=0.41, rely=0.60, anchor="center")
        self.botao_2.place(relx=0.59, rely=0.60, anchor="center")
        self.botao_3.place(relx=0.41, rely=0.68, anchor="center")
        self.botao_4.place(relx=0.59, rely=0.68, anchor="center")
        
  
    def Quiz_Dificil(self):
            
            #DESTROIR BOTAO DE ESCOLHA DIFICULDADE
            self.botao_escolha_geral.destroy()
            self.botao_dificuldade_facil.destroy()
            self.botao_dificuldade_medio.destroy()
            self.botao_dificuldade_dificil.destroy()
            
            # ESCOLHENDO A BANDEIRA E OPCOES CERTAS E ERRADAS
            self.alternativa_certa, self.arquivo_certo = random.choice(bandeiras_dificeis)
            erradas = [item for item in bandeiras_dificeis if item[0] != self.alternativa_certa]
            self.opcoes_erradas = random.sample(erradas, 3)
        
            # JUNTA TODAS AS OPCOES E EMBARALHA
            opcoes = [self.alternativa_certa] + [e[0] for e in self.opcoes_erradas]
            random.shuffle(opcoes)
        
            # COLOCANDO A BANDEIRA NA TELA
            self.bandeira_tela = tk.PhotoImage(file=self.arquivo_certo)
        
            if "np" in self.arquivo_certo:
                self.bandeira_tela = self.bandeira_tela.subsample(1,1)
            else:
                self.bandeira_tela = self.bandeira_tela.subsample(2, 2)
        
            self.label_bandeira_tela = tk.Label(self.master, image=self.bandeira_tela, bd=0)
            self.label_bandeira_tela.place(relx=0.5, rely=0.33, anchor="center")
        
            # COLOCANDO OS 4 BOTÕES COM AS OPÇÕES
            self.botao_1 = tk.Button(self.master, text=opcoes[0], font=("Luckiest Guy", 20),
                              fg="black", bg="white", width=16, height=1,
                              command=lambda: self.ClickPais_DIFICIL(opcoes[0]))
            self.botao_2 = tk.Button(self.master, text=opcoes[1], font=("Luckiest Guy", 20),
                                      fg="black", bg="white", width=16, height=1,
                                      command=lambda: self.ClickPais_DIFICIL(opcoes[1]))
            self.botao_3 = tk.Button(self.master, text=opcoes[2], font=("Luckiest Guy", 20),
                                      fg="black", bg="white", width=16, height=1,
                                      command=lambda: self.ClickPais_DIFICIL(opcoes[2]))
            self.botao_4 = tk.Button(self.master, text=opcoes[3], font=("Luckiest Guy", 20),
                                      fg="black", bg="white", width=16, height=1,
                                      command=lambda: self.ClickPais_DIFICIL(opcoes[3]))
          
            # POSICIONANDO
            self.botao_1.place(relx=0.41, rely=0.60, anchor="center")
            self.botao_2.place(relx=0.59, rely=0.60, anchor="center")
            self.botao_3.place(relx=0.41, rely=0.68, anchor="center")
            self.botao_4.place(relx=0.59, rely=0.68, anchor="center")
        
    
    #CLICANDO NAS ALTERNATIVAS E MUDANDO A BANDEIRA
    def ClickPais_GERAL(self, pais_escolhido):
        if pais_escolhido == self.alternativa_certa:
            # ESCOLHENDO A BANDEIRA E OPCOES CERTAS E ERRADAS
            self.alternativa_certa, self.arquivo_certo = random.choice(bandeiras)
            erradas = [item for item in bandeiras if item[0] != self.alternativa_certa]
            self.opcoes_erradas = random.sample(erradas, 3)
            
            # JUNTA TODAS AS OPCOES E EMBARALHA
            opcoes = [self.alternativa_certa] + [e[0] for e in self.opcoes_erradas]
            random.shuffle(opcoes)
        
            # COLOCANDO A BANDEIRA NA TELA
            self.bandeira_tela = tk.PhotoImage(file=self.arquivo_certo)
            
        
            if "np" in self.arquivo_certo:
                self.bandeira_tela = self.bandeira_tela.subsample(1, 1)
            else:
                self.bandeira_tela = self.bandeira_tela.subsample(2, 2)
                
            self.label_bandeira_tela = tk.Label(self.master, image=self.bandeira_tela, bd=0)
            self.label_bandeira_tela.place(relx=0.5, rely=0.33, anchor="center")
        
            #DESTRUIR BOTÃO
            
            self.botao_1.destroy()
            self.botao_2.destroy()
            self.botao_3.destroy()
            self.botao_4.destroy()
            
            #COLOCANDO NOVAS OPÇÕES NOS BOTOES
            #COLOCANDO OS 4 BOTÕES COM AS OPÇÕES
            self.botao_1 = tk.Button(self.master, text=opcoes[0], font=("Luckiest Guy", 20),
                              fg="black", bg="white", width=16, height=1,
                              command=lambda: self.ClickPais_GERAL(opcoes[0]))
            self.botao_2 = tk.Button(self.master, text=opcoes[1], font=("Luckiest Guy", 20),
                                      fg="black", bg="white", width=16, height=1,
                                      command=lambda: self.ClickPais_GERAL(opcoes[1]))
            self.botao_3 = tk.Button(self.master, text=opcoes[2], font=("Luckiest Guy", 20),
                                      fg="black", bg="white", width=16, height=1,
                                      command=lambda: self.ClickPais_GERAL(opcoes[2]))
            self.botao_4 = tk.Button(self.master, text=opcoes[3], font=("Luckiest Guy", 20),
                                      fg="black", bg="white", width=16, height=1,
                                      command=lambda: self.ClickPais_GERAL(opcoes[3]))
            
            # POSICIONANDO
            self.botao_1.place(relx=0.41, rely=0.60, anchor="center")
            self.botao_2.place(relx=0.59, rely=0.60, anchor="center")
            self.botao_3.place(relx=0.41, rely=0.68, anchor="center")
            self.botao_4.place(relx=0.59, rely=0.68, anchor="center")

    
        else:
            
            #DESTRUIR BOTOES
            self.botao_1.destroy()
            self.botao_2.destroy()
            self.botao_3.destroy()
            self.botao_4.destroy()
            
            self.botao_jogar_novamente = tk.Button(self.master, text="Jogar Novamente!",font=("Luckiest Guy", 30), fg="black", bg="white", command=self.JogarDeNovo_GERAL)
            self.botao_jogar_novamente.place(relx=0.50, rely=0.62, anchor="center")
            
    
    #CLICANDO NAS ALTERNATIVAS E MUDANDO A BANDEIRA
    def ClickPais_FACIL(self, pais_escolhido):
        if pais_escolhido == self.alternativa_certa:
            # ESCOLHENDO A BANDEIRA E OPCOES CERTAS E ERRADAS
            self.alternativa_certa, self.arquivo_certo = random.choice(bandeiras_faceis)
            erradas = [item for item in bandeiras_faceis if item[0] != self.alternativa_certa]
            self.opcoes_erradas = random.sample(erradas, 3)
            
            # JUNTA TODAS AS OPCOES E EMBARALHA
            opcoes = [self.alternativa_certa] + [e[0] for e in self.opcoes_erradas]
            random.shuffle(opcoes)
        
            # COLOCANDO A BANDEIRA NA TELA
            self.bandeira_tela = tk.PhotoImage(file=self.arquivo_certo)
            
        
            if "np" in self.arquivo_certo:
                self.bandeira_tela = self.bandeira_tela.subsample(1, 1)
            else:
                self.bandeira_tela = self.bandeira_tela.subsample(2, 2)
                
            self.label_bandeira_tela = tk.Label(self.master, image=self.bandeira_tela, bd=0)
            self.label_bandeira_tela.place(relx=0.5, rely=0.33, anchor="center")
        
            #DESTRUIR BOTÃO
            
            self.botao_1.destroy()
            self.botao_2.destroy()
            self.botao_3.destroy()
            self.botao_4.destroy()
            
            #COLOCANDO NOVAS OPÇÕES NOS BOTOES
            #COLOCANDO OS 4 BOTÕES COM AS OPÇÕES
            self.botao_1 = tk.Button(self.master, text=opcoes[0], font=("Luckiest Guy", 20),
                              fg="black", bg="white", width=16, height=1,
                              command=lambda: self.ClickPais_FACIL(opcoes[0]))
            self.botao_2 = tk.Button(self.master, text=opcoes[1], font=("Luckiest Guy", 20),
                                      fg="black", bg="white", width=16, height=1,
                                      command=lambda: self.ClickPais_FACIL(opcoes[1]))
            self.botao_3 = tk.Button(self.master, text=opcoes[2], font=("Luckiest Guy", 20),
                                      fg="black", bg="white", width=16, height=1,
                                      command=lambda: self.ClickPais_FACIL(opcoes[2]))
            self.botao_4 = tk.Button(self.master, text=opcoes[3], font=("Luckiest Guy", 20),
                                      fg="black", bg="white", width=16, height=1,
                                      command=lambda: self.ClickPais_FACIL(opcoes[3]))
        
            # POSICIONANDO
            self.botao_1.place(relx=0.41, rely=0.60, anchor="center")
            self.botao_2.place(relx=0.59, rely=0.60, anchor="center")
            self.botao_3.place(relx=0.41, rely=0.68, anchor="center")
            self.botao_4.place(relx=0.59, rely=0.68, anchor="center")
        
        else:
         
            #DESTRUIR BOTOES
            self.botao_1.destroy()
            self.botao_2.destroy()
            self.botao_3.destroy()
            self.botao_4.destroy()
        
            self.botao_jogar_novamente = tk.Button(self.master, text="Jogar Novamente!",font=("Luckiest Guy", 30), fg="black", bg="white", command=self.JogarDeNovo_FACIL)
            self.botao_jogar_novamente.place(relx=0.50, rely=0.62, anchor="center")
            
    
    #CLICANDO NAS ALTERNATIVAS E MUDANDO A BANDEIRA
    def ClickPais_MEDIO(self, pais_escolhido):
        if pais_escolhido == self.alternativa_certa:
            # ESCOLHENDO A BANDEIRA E OPCOES CERTAS E ERRADAS
            self.alternativa_certa, self.arquivo_certo = random.choice(bandeiras_medias)
            erradas = [item for item in bandeiras_medias if item[0] != self.alternativa_certa]
            self.opcoes_erradas = random.sample(erradas, 3)
            
            # JUNTA TODAS AS OPCOES E EMBARALHA
            opcoes = [self.alternativa_certa] + [e[0] for e in self.opcoes_erradas]
            random.shuffle(opcoes)
        
            # COLOCANDO A BANDEIRA NA TELA
            self.bandeira_tela = tk.PhotoImage(file=self.arquivo_certo)
            
        
            if "np" in self.arquivo_certo:
                self.bandeira_tela = self.bandeira_tela.subsample(1, 1)
            else:
                self.bandeira_tela = self.bandeira_tela.subsample(2, 2)
                
            self.label_bandeira_tela = tk.Label(self.master, image=self.bandeira_tela, bd=0)
            self.label_bandeira_tela.place(relx=0.5, rely=0.33, anchor="center")
        
            #DESTRUIR BOTÃO
            
            self.botao_1.destroy()
            self.botao_2.destroy()
            self.botao_3.destroy()
            self.botao_4.destroy()
            
            #COLOCANDO NOVAS OPÇÕES NOS BOTOES
            #COLOCANDO OS 4 BOTÕES COM AS OPÇÕES
            self.botao_1 = tk.Button(self.master, text=opcoes[0], font=("Luckiest Guy", 20),
                              fg="black", bg="white", width=16, height=1,
                              command=lambda: self.ClickPais_MEDIO(opcoes[0]))
            self.botao_2 = tk.Button(self.master, text=opcoes[1], font=("Luckiest Guy", 20),
                                      fg="black", bg="white", width=16, height=1,
                                      command=lambda: self.ClickPais_MEDIO(opcoes[1]))
            self.botao_3 = tk.Button(self.master, text=opcoes[2], font=("Luckiest Guy", 20),
                                      fg="black", bg="white", width=16, height=1,
                                      command=lambda: self.ClickPais_MEDIO(opcoes[2]))
            self.botao_4 = tk.Button(self.master, text=opcoes[3], font=("Luckiest Guy", 20),
                                      fg="black", bg="white", width=16, height=1,
                                      command=lambda: self.ClickPais_MEDIO(opcoes[3]))
        
            # POSICIONANDO
            self.botao_1.place(relx=0.41, rely=0.60, anchor="center")
            self.botao_2.place(relx=0.59, rely=0.60, anchor="center")
            self.botao_3.place(relx=0.41, rely=0.68, anchor="center")
            self.botao_4.place(relx=0.59, rely=0.68, anchor="center")
        else:
            #
            #DESTRUIR BOTOES
            self.botao_1.destroy()
            self.botao_2.destroy()
            self.botao_3.destroy()
            self.botao_4.destroy()
            
            self.botao_jogar_novamente = tk.Button(self.master, text="Jogar Novamente!",font=("Luckiest Guy", 30), fg="black", bg="white", command=self.JogarDeNovo_MEDIO)
            self.botao_jogar_novamente.place(relx=0.50, rely=0.62, anchor="center")
            
    
    #CLICANDO NAS ALTERNATIVAS E MUDANDO A BANDEIRA
    def ClickPais_DIFICIL(self, pais_escolhido):
        if pais_escolhido == self.alternativa_certa:
            # ESCOLHENDO A BANDEIRA E OPCOES CERTAS E ERRADAS
            self.alternativa_certa, self.arquivo_certo = random.choice(bandeiras_dificeis)
            erradas = [item for item in bandeiras_dificeis if item[0] != self.alternativa_certa]
            self.opcoes_erradas = random.sample(erradas, 3)
            
            # JUNTA TODAS AS OPCOES E EMBARALHA
            opcoes = [self.alternativa_certa] + [e[0] for e in self.opcoes_erradas]
            random.shuffle(opcoes)
        
            # COLOCANDO A BANDEIRA NA TELA
            self.bandeira_tela = tk.PhotoImage(file=self.arquivo_certo)
            
        
            if "np" in self.arquivo_certo:
                self.bandeira_tela = self.bandeira_tela.subsample(1, 1)
            else:
                self.bandeira_tela = self.bandeira_tela.subsample(2, 2)
                
            self.label_bandeira_tela = tk.Label(self.master, image=self.bandeira_tela, bd=0)
            self.label_bandeira_tela.place(relx=0.5, rely=0.33, anchor="center")
        
            #DESTRUIR BOTÃO
            
            self.botao_1.destroy()
            self.botao_2.destroy()
            self.botao_3.destroy()
            self.botao_4.destroy()
            
            #COLOCANDO NOVAS OPÇÕES NOS BOTOES
            #COLOCANDO OS 4 BOTÕES COM AS OPÇÕES
            self.botao_1 = tk.Button(self.master, text=opcoes[0], font=("Luckiest Guy", 20),
                              fg="black", bg="white", width=16, height=1,
                              command=lambda: self.ClickPais_DIFICIL(opcoes[0]))
            self.botao_2 = tk.Button(self.master, text=opcoes[1], font=("Luckiest Guy", 20),
                                      fg="black", bg="white", width=16, height=1,
                                      command=lambda: self.ClickPais_DIFICIL(opcoes[1]))
            self.botao_3 = tk.Button(self.master, text=opcoes[2], font=("Luckiest Guy", 20),
                                      fg="black", bg="white", width=16, height=1,
                                      command=lambda: self.ClickPais_DIFICIL(opcoes[2]))
            self.botao_4 = tk.Button(self.master, text=opcoes[3], font=("Luckiest Guy", 20),
                                      fg="black", bg="white", width=16, height=1,
                                      command=lambda: self.ClickPais_DIFICIL(opcoes[3]))
        
            # POSICIONANDO
            self.botao_1.place(relx=0.41, rely=0.60, anchor="center")
            self.botao_2.place(relx=0.59, rely=0.60, anchor="center")
            self.botao_3.place(relx=0.41, rely=0.68, anchor="center")
            self.botao_4.place(relx=0.59, rely=0.68, anchor="center")
        else:

            #DESTRUIR BOTOES
            self.botao_1.destroy()
            self.botao_2.destroy()
            self.botao_3.destroy()
            self.botao_4.destroy()
            
            self.botao_jogar_novamente = tk.Button(self.master, text="Jogar Novamente!",font=("Luckiest Guy", 30), fg="black", bg="white", command=self.JogarDeNovo_DIFICIL)
            self.botao_jogar_novamente.place(relx=0.50, rely=0.62, anchor="center")
            
    def JogarDeNovo_GERAL(self):
        
        #DESTRUIR TEXTO
        

        # ESCOLHENDO A BANDEIRA E OPCOES CERTAS E ERRADAS
        self.alternativa_certa, self.arquivo_certo = random.choice(bandeiras)
        erradas = [item for item in bandeiras if item[0] != self.alternativa_certa]
        self.opcoes_erradas = random.sample(erradas, 3)
    
        # JUNTA TODAS AS OPCOES E EMBARALHA
        opcoes = [self.alternativa_certa] + [e[0] for e in self.opcoes_erradas]
        random.shuffle(opcoes)
        
        self.botao_jogar_novamente.destroy()
        
        # COLOCANDO A BANDEIRA NA TELA
        self.bandeira_tela = tk.PhotoImage(file=self.arquivo_certo)
    
        if "np" in self.arquivo_certo:
            self.bandeira_tela = self.bandeira_tela.subsample(1, 1)
        else:
            self.bandeira_tela = self.bandeira_tela.subsample(2, 2)
    
        self.label_bandeira_tela = tk.Label(self.master, image=self.bandeira_tela, bd=0)
        self.label_bandeira_tela.place(relx=0.5, rely=0.33, anchor="center")
    
        # COLOCANDO OS 4 BOTÕES COM AS OPÇÕES
        self.botao_1 = tk.Button(self.master, text=opcoes[0], font=("Luckiest Guy", 20),
                          fg="black", bg="white", width=16, height=1,
                          command=lambda: self.ClickPais_GERAL(opcoes[0]))
        self.botao_2 = tk.Button(self.master, text=opcoes[1], font=("Luckiest Guy", 20),
                                  fg="black", bg="white", width=16, height=1,
                                  command=lambda: self.ClickPais_GERAL(opcoes[1]))
        self.botao_3 = tk.Button(self.master, text=opcoes[2], font=("Luckiest Guy", 20),
                                  fg="black", bg="white", width=16, height=1,
                                  command=lambda: self.ClickPais_GERAL(opcoes[2]))
        self.botao_4 = tk.Button(self.master, text=opcoes[3], font=("Luckiest Guy", 20),
                                  fg="black", bg="white", width=16, height=1,
                                  command=lambda: self.ClickPais_GERAL(opcoes[3]))

    
        # POSICIONANDO
        self.botao_1.place(relx=0.41, rely=0.60, anchor="center")
        self.botao_2.place(relx=0.59, rely=0.60, anchor="center")
        self.botao_3.place(relx=0.41, rely=0.68, anchor="center")
        self.botao_4.place(relx=0.59, rely=0.68, anchor="center")
        
    def JogarDeNovo_FACIL(self):
        
        #DESTRUIR TEXTO
        

        # ESCOLHENDO A BANDEIRA E OPCOES CERTAS E ERRADAS
        self.alternativa_certa, self.arquivo_certo = random.choice(bandeiras_faceis)
        erradas = [item for item in bandeiras_faceis if item[0] != self.alternativa_certa]
        self.opcoes_erradas = random.sample(erradas, 3)
    
        # JUNTA TODAS AS OPCOES E EMBARALHA
        opcoes = [self.alternativa_certa] + [e[0] for e in self.opcoes_erradas]
        random.shuffle(opcoes)
        
        self.botao_jogar_novamente.destroy()
        
        # COLOCANDO A BANDEIRA NA TELA
        self.bandeira_tela = tk.PhotoImage(file=self.arquivo_certo)
    
        if "np" in self.arquivo_certo:
            self.bandeira_tela = self.bandeira_tela.subsample(1, 1)
        else:
            self.bandeira_tela = self.bandeira_tela.subsample(2, 2)
    
        self.label_bandeira_tela = tk.Label(self.master, image=self.bandeira_tela, bd=0)
        self.label_bandeira_tela.place(relx=0.5, rely=0.33, anchor="center")
    
        # COLOCANDO OS 4 BOTÕES COM AS OPÇÕES
        self.botao_1 = tk.Button(self.master, text=opcoes[0], font=("Luckiest Guy", 20),
                          fg="black", bg="white", width=16, height=1,
                          command=lambda: self.ClickPais_FACIL(opcoes[0]))
        self.botao_2 = tk.Button(self.master, text=opcoes[1], font=("Luckiest Guy", 20),
                                  fg="black", bg="white", width=16, height=1,
                                  command=lambda: self.ClickPais_FACIL(opcoes[1]))
        self.botao_3 = tk.Button(self.master, text=opcoes[2], font=("Luckiest Guy", 20),
                                  fg="black", bg="white", width=16, height=1,
                                  command=lambda: self.ClickPais_FACIL(opcoes[2]))
        self.botao_4 = tk.Button(self.master, text=opcoes[3], font=("Luckiest Guy", 20),
                                  fg="black", bg="white", width=16, height=1,
                                  command=lambda: self.ClickPais_FACIL(opcoes[3]))

    
        # POSICIONANDO
        self.botao_1.place(relx=0.41, rely=0.60, anchor="center")
        self.botao_2.place(relx=0.59, rely=0.60, anchor="center")
        self.botao_3.place(relx=0.41, rely=0.68, anchor="center")
        self.botao_4.place(relx=0.59, rely=0.68, anchor="center")
        

    def JogarDeNovo_MEDIO(self):
        
        #DESTRUIR TEXTO
        

        # ESCOLHENDO A BANDEIRA E OPCOES CERTAS E ERRADAS
        self.alternativa_certa, self.arquivo_certo = random.choice(bandeiras_medias)
        erradas = [item for item in bandeiras_medias if item[0] != self.alternativa_certa]
        self.opcoes_erradas = random.sample(erradas, 3)
    
        # JUNTA TODAS AS OPCOES E EMBARALHA
        opcoes = [self.alternativa_certa] + [e[0] for e in self.opcoes_erradas]
        random.shuffle(opcoes)
        
        self.botao_jogar_novamente.destroy()
        
        # COLOCANDO A BANDEIRA NA TELA
        self.bandeira_tela = tk.PhotoImage(file=self.arquivo_certo)
    
        if "np" in self.arquivo_certo:
            self.bandeira_tela = self.bandeira_tela.subsample(1, 1)
        else:
            self.bandeira_tela = self.bandeira_tela.subsample(2, 2)
    
        self.label_bandeira_tela = tk.Label(self.master, image=self.bandeira_tela, bd=0)
        self.label_bandeira_tela.place(relx=0.5, rely=0.33, anchor="center")
    
        # COLOCANDO OS 4 BOTÕES COM AS OPÇÕES
        self.botao_1 = tk.Button(self.master, text=opcoes[0], font=("Luckiest Guy", 20),
                          fg="black", bg="white", width=16, height=1,
                          command=lambda: self.ClickPais_MEDIO(opcoes[0]))
        self.botao_2 = tk.Button(self.master, text=opcoes[1], font=("Luckiest Guy", 20),
                                  fg="black", bg="white", width=16, height=1,
                                  command=lambda: self.ClickPais_MEDIO(opcoes[1]))
        self.botao_3 = tk.Button(self.master, text=opcoes[2], font=("Luckiest Guy", 20),
                                  fg="black", bg="white", width=16, height=1,
                                  command=lambda: self.ClickPais_MEDIO(opcoes[2]))
        self.botao_4 = tk.Button(self.master, text=opcoes[3], font=("Luckiest Guy", 20),
                                  fg="black", bg="white", width=16, height=1,
                                  command=lambda: self.ClickPais_MEDIO(opcoes[3]))

    
        # POSICIONANDO
        self.botao_1.place(relx=0.41, rely=0.60, anchor="center")
        self.botao_2.place(relx=0.59, rely=0.60, anchor="center")
        self.botao_3.place(relx=0.41, rely=0.68, anchor="center")
        self.botao_4.place(relx=0.59, rely=0.68, anchor="center")
        
    def JogarDeNovo_DIFICIL(self):
        
        # ESCOLHENDO A BANDEIRA E OPCOES CERTAS E ERRADAS
        self.alternativa_certa, self.arquivo_certo = random.choice(bandeiras_dificeis)
        erradas = [item for item in bandeiras_dificeis if item[0] != self.alternativa_certa]
        self.opcoes_erradas = random.sample(erradas, 3)
    
        # JUNTA TODAS AS OPCOES E EMBARALHA
        opcoes = [self.alternativa_certa] + [e[0] for e in self.opcoes_erradas]
        random.shuffle(opcoes)
        
        self.botao_jogar_novamente.destroy()
        
        # COLOCANDO A BANDEIRA NA TELA
        self.bandeira_tela = tk.PhotoImage(file=self.arquivo_certo)
    
        if "np" in self.arquivo_certo:
            self.bandeira_tela = self.bandeira_tela.subsample(1, 1)
        else:
            self.bandeira_tela = self.bandeira_tela.subsample(2, 2)
    
        self.label_bandeira_tela = tk.Label(self.master, image=self.bandeira_tela, bd=0)
        self.label_bandeira_tela.place(relx=0.5, rely=0.33, anchor="center")
    
        # COLOCANDO OS 4 BOTÕES COM AS OPÇÕES
        self.botao_1 = tk.Button(self.master, text=opcoes[0], font=("Luckiest Guy", 20),
                          fg="black", bg="white", width=16, height=1,
                          command=lambda: self.ClickPais_DIFICIL(opcoes[0]))
        self.botao_2 = tk.Button(self.master, text=opcoes[1], font=("Luckiest Guy", 20),
                                  fg="black", bg="white", width=16, height=1,
                                  command=lambda: self.ClickPais_DIFICIL(opcoes[1]))
        self.botao_3 = tk.Button(self.master, text=opcoes[2], font=("Luckiest Guy", 20),
                                  fg="black", bg="white", width=16, height=1,
                                  command=lambda: self.ClickPais_DIFICIL(opcoes[2]))
        self.botao_4 = tk.Button(self.master, text=opcoes[3], font=("Luckiest Guy", 20),
                                  fg="black", bg="white", width=16, height=1,
                                  command=lambda: self.ClickPais_DIFICIL(opcoes[3]))

    
        # POSICIONANDO
        self.botao_1.place(relx=0.41, rely=0.60, anchor="center")
        self.botao_2.place(relx=0.59, rely=0.60, anchor="center")
        self.botao_3.place(relx=0.41, rely=0.68, anchor="center")
        self.botao_4.place(relx=0.59, rely=0.68, anchor="center")
        
class Flagle:
    
    def __init__(self, master):
        self.master = master
        self.master.title("FLAGLE")
        
        #CONTADOR DE TENTATIVAS FLAGLE
        self.contador = 0
        
        # Tela cheia automática
        self.master.attributes('-fullscreen', True)
        
        #Foto do fundo
        self.imagem_fundo_2 = tk.PhotoImage(file="Fundo_quiz_flagle.png")
        self.label_mapa = tk.Label(self.master, image=self.imagem_fundo_2)
        self.label_mapa.place(relx=0.5, rely=0.5, anchor='center')
        #Botoes dos niveis de dificuldade flagle 
        self.botao_flagle_facil = tk.Button(self.master, text="Fácil", font=("Luckiest Guy", 20),
                                            fg="black", bg="white", width=15, height=1, command=self.flagle_facil)
        
        self.botao_flagle_medio = tk.Button(self.master, text="Médio", font=("Luckiest Guy", 20),
                                            fg="black", bg="white", width=15, height=1, command=self.flagle_medio)
        
        self.botao_flagle_dificil = tk.Button(self.master, text="Difícil", font=("Luckiest Guy", 20),
                                               fg="black", bg="white", width=15, height=1, command=self.flagle_dificil)
        
        
        # Posicionamento dos botoes niveis dificuldade flagle 
        self.botao_flagle_facil.place(relx=0.5, rely=0.38, anchor="center")
        self.botao_flagle_medio.place(relx=0.5, rely=0.46, anchor="center")
        self.botao_flagle_dificil.place(relx=0.5, rely=0.54, anchor="center")
        
        
        # Botão para voltar à tela inicial
        self.botao_Sair2 = tk.Button(self.master, text="Sair" ,font=("Luckiest Guy", 24),
                          fg="black", bg="white", width=9, height=1, command=self.sair2)
        self.botao_Sair2.place(relx= 0.50, rely=0.76, anchor="center")
    
    def sair2(self):
        root30 = self.master
        root30.destroy()
        Interface()  # Retorna à tela inicial
        
        
    def flagle_facil(self):
        
        #Destruir botoes de escolha de nivel flagle
        self.botao_flagle_facil.destroy()
        self.botao_flagle_medio.destroy()
        self.botao_flagle_dificil.destroy()
            
        # ESCOLHENDO A BANDEIRA E OPCOES CERTAS E ERRADAS
        self.alternativa_certa_original, self.arquivo_certo = random.choice(bandeiras)
        #NORMALIZANDO OS NOMES EM TUDO MINUSCULA
        self.alternativa_certa = self.alternativa_certa_original.lower()
        # COLOCANDO A BANDEIRA NA TELA
        self.bandeira_tela = tk.PhotoImage(file=self.arquivo_certo)
        
        if "np" in self.arquivo_certo:
            self.bandeira_tela = self.bandeira_tela.subsample(1, 1)
        else:
            self.bandeira_tela = self.bandeira_tela.subsample(2, 2)
        
        #BD=0 pra tirar a borda da imagem    
        self.label_bandeira_tela = tk.Label(self.master, image=self.bandeira_tela, bd=0)
        self.label_bandeira_tela.place(relx=0.5, rely=0.35, anchor="center")
        self.label_bandeira_tela.lift()
        
        #CANVAS BLOQUINHOS
        #BLOQUINHOS DE BAIXO
            
        self.bloco_1 = tk.Canvas(self.master, height=137.5, width=133.5, bg="black",  highlightthickness=2,)
        self.bloco_1.place(relx=0.36, rely=0.349)
            
        self.bloco_2 = tk.Canvas(self.master, height=137.5, width=133.5, bg="black", highlightthickness=2)
        self.bloco_2.place(relx=0.455, rely=0.349)
                          
        self.bloco_3 = tk.Canvas(self.master, height=137.5, width=133.5, bg="black", highlightthickness=2)
        self.bloco_3.place(relx=0.543, rely=0.349)
        
                                        
        #BLOQUINHOS DE CIMA
            
        self.bloco_4 = tk.Canvas(self.master, height=137.5, width=133.5, bg="black",  highlightthickness=2,)
        self.bloco_4.place(relx=0.36, rely=0.191)
            
        self.bloco_5 = tk.Canvas(self.master, height=137.5, width=133.5, bg="black", highlightthickness=2)
        self.bloco_5.place(relx=0.455, rely=0.191)
                          
        self.bloco_6 = tk.Canvas(self.master, height=137.5, width=133.5, bg="black", highlightthickness=2)
        self.bloco_6.place(relx=0.543, rely=0.191)
        
        #lista blocos flagle facil
        self.blocos_Facil = [self.bloco_1, self.bloco_2, self.bloco_3, self.bloco_4, self.bloco_5, self.bloco_6]
        
        
        # CAIXA DE ENTRADA
        self.caixa_Flagle = tk.Entry(self.master, width=16, font=("Luckiest Guy", 18), bg="white", fg="black")
        self.caixa_Flagle.place(relx=0.5, rely=0.6, anchor="center")
        
        
        #BOTAO NA CAIXA DE ENTRADA
        self.botao_caixa_entrada = tk.Button(self.master, text="OK",font=("Luckiest Guy", 20),
                          fg="black", bg="white", width=1, height=1, command = self.tentativa_1)
        self.botao_caixa_entrada.place(relx=0.58, rely=0.6, anchor="center")
        
        self.master.bind("<Return>", self.tentativa_1)
    
    def tentativa_1(self, ev=None):
        
        #SALVA O TEXTO DA CAIXA E APAGA O TEXTO
        self.escolha_usuario = self.caixa_Flagle.get()
        self.caixa_Flagle.delete(0, tk.END)
        
        #COMPARACAO COM A BANDEIRA ESCOLHIDA e revelação da bandeira 
        ### RESPOSTA CERTA
        if self.escolha_usuario == self.alternativa_certa:
            self.bloco_1.destroy() #Revelação das bandeiras
            self.bloco_2.destroy()
            self.bloco_3.destroy()
            self.bloco_4.destroy()
            self.bloco_5.destroy()
            self.bloco_6.destroy()
            
            
            ## Remover caixa e botao 
            self.caixa_Flagle.destroy() #Destruir a caixa de entrada
            self.botao_caixa_entrada.destroy() #Destruir o botao da caixa de entrada
            
            # Revelar nome do país 
            self.label_revelacao_nome= tk.Label(self.master, text=(self.alternativa_certa),font=("Luckiest Guy", 52), bg="#b2dfff", fg="black")
            self.label_revelacao_nome.place(relx=0.5, rely=0.15, anchor="center")
    
            #JOGAR NOVAMENTE
            self.botao_jogar_novamente2 = tk.Button(self.master, text="Jogar novamente",font=("Luckiest Guy", 20),
                              fg="black", bg="white", width=14, height=1, command=self.comando_jogar_novamente_Flagle)
            self.botao_jogar_novamente2.place(relx=0.5, rely=0.6, anchor="center")
            
            
        ## RESPOSTA ERRADA
        elif self.contador < 5:
            self.escolha_bloco_destruir = random.choice(self.blocos_Facil)
            self.escolha_bloco_destruir.destroy()
            self.blocos_Facil.remove(self.escolha_bloco_destruir)
            self.contador += 1
            return
            
        else:
            # Sexta tentativa: fim de jogo
            self.escolha_bloco_destruir = random.choice(self.blocos_Facil)
            self.escolha_bloco_destruir.destroy()
            self.blocos_Facil.remove(self.escolha_bloco_destruir)
    
            # Destruir entrada
            self.caixa_Flagle.destroy()
            self.botao_caixa_entrada.destroy()
    
            # Revelar nome do país
            self.label_revelacao_nome = tk.Label(self.master,text=self.alternativa_certa, font=("Luckiest Guy", 52), bg="#b2dfff", fg="black")
            self.label_revelacao_nome.place(relx=0.5, rely=0.15, anchor="center")
    
            # Botão jogar novamente
            self.botao_jogar_novamente2 = tk.Button(self.master, text="Jogar novamente",
                                                    font=("Luckiest Guy", 20),fg="black", bg="white", width=14, height=1, command=self.comando_jogar_novamente_Flagle)
            self.botao_jogar_novamente2.place(relx=0.5, rely=0.6, anchor="center")
            


        
    def comando_jogar_novamente_Flagle(self):
        root5 = self.master  # salva referência
        root5.destroy()      # destrói a janela inteira

        # cria uma janela nova
        resetar_Flagle = tk.Tk()
        Flagle(resetar_Flagle)
        resetar_Flagle.mainloop()
        
   
    def flagle_medio(self):
    
        #Destruir botoes de escolha de nivel flagle
        self.botao_flagle_facil.destroy()
        self.botao_flagle_medio.destroy()
        self.botao_flagle_dificil.destroy()
            
        # ESCOLHENDO A BANDEIRA E OPCOES CERTAS E ERRADAS
        self.alternativa_certa_original, self.arquivo_certo = random.choice(bandeiras)
        
        #NORMALIZANDO OS NOMES EM TUDO MINUSCULA
        self.alternativa_certa = self.alternativa_certa_original.lower()
        # COLOCANDO A BANDEIRA NA TELA
        self.bandeira_tela = tk.PhotoImage(file=self.arquivo_certo)
        
        if "np" in self.arquivo_certo:
            self.bandeira_tela = self.bandeira_tela.subsample(1, 1)
        else:
            self.bandeira_tela = self.bandeira_tela.subsample(2, 2)

        self.label_bandeira_tela = tk.Label(self.master, image=self.bandeira_tela, bd=0)
        self.label_bandeira_tela.place(relx=0.5, rely=0.35, anchor="center")
        self.label_bandeira_tela.lift()
        
        #CANVAS BLOQUINHOS
        
        # BLOQUINHOS DA PRIMEIRA LINHA
        self.bloco_1 = tk.Canvas(self.master, height=88.3, width=97.4, bg="black", highlightthickness=3)
        self.bloco_1.place(relx=0.3607, rely=0.1973)
        
        self.bloco_2 = tk.Canvas(self.master, height=88.3, width=97.4, bg="black", highlightthickness=3)
        self.bloco_2.place(relx=0.4302, rely=0.1973)
        
        self.bloco_3 = tk.Canvas(self.master, height=88.3, width=97.4, bg="black", highlightthickness=3)
        self.bloco_3.place(relx=0.499, rely=0.1973)
        
        self.bloco_4 = tk.Canvas(self.master, height=88.3, width=97.4, bg="black", highlightthickness=3)
        self.bloco_4.place(relx=0.569, rely=0.1973)
        
        
        # BLOQUINHOS DA SEGUNDA LINHA
        self.bloco_5 = tk.Canvas(self.master, height=88.3, width=97.4, bg="black", highlightthickness=3)
        self.bloco_5.place(relx=0.3608, rely=0.299425)
        
        self.bloco_6 = tk.Canvas(self.master, height=88.3, width=97.4, bg="black", highlightthickness=3)
        self.bloco_6.place(relx=0.4302, rely=0.299425)
        
        self.bloco_7 = tk.Canvas(self.master, height=88.3, width=97.4, bg="black", highlightthickness=3)
        self.bloco_7.place(relx=0.499, rely=0.299425)
        
        self.bloco_8 = tk.Canvas(self.master, height=88.3, width=97.4, bg="black", highlightthickness=3)
        self.bloco_8.place(relx=0.569, rely=0.299425)
            
        
        # BLOQUINHOS DA TERCEIRA LINHA
        self.bloco_9 = tk.Canvas(self.master, height=89, width=97.4, bg="black", highlightthickness=3)
        self.bloco_9.place(relx=0.3607, rely=0.4004)

        
        self.bloco_10 = tk.Canvas(self.master, height=89, width=97.4, bg="black", highlightthickness=3)
        self.bloco_10.place(relx=0.4302, rely=0.4004)
        
        self.bloco_11 = tk.Canvas(self.master, height=89, width=97.4, bg="black", highlightthickness=3)
        self.bloco_11.place(relx=0.499, rely=0.4004)
        
        self.bloco_12 = tk.Canvas(self.master, height=89, width=97.4, bg="black", highlightthickness=3)
        self.bloco_12.place(relx=0.569, rely=0.4004)


        
        #lista blocos flagle medio
        self.blocos_Medio = [self.bloco_1, self.bloco_2, self.bloco_3, self.bloco_4, self.bloco_5, self.bloco_6,
                             self.bloco_7, self.bloco_8, self.bloco_9, self.bloco_10, self.bloco_11, self.bloco_12]
        
        
        # CAIXA DE ENTRADA
        self.caixa_Flagle = tk.Entry(self.master, width=16, font=("Luckiest Guy", 18), bg="white", fg="black")
        self.caixa_Flagle.place(relx=0.5, rely=0.6, anchor="center")
        
        #BOTAO NA CAIXA DE ENTRADA
        self.botao_caixa_entrada = tk.Button(self.master, text="OK",font=("Luckiest Guy", 20),
                          fg="black", bg="white", width=1, height=1, command = self.tentativa_2)
        self.botao_caixa_entrada.place(relx=0.58, rely=0.6, anchor="center")
        
        self.master.bind("<Return>", self.tentativa_2)
    
    def tentativa_2(self, ev=None):
        
        #SALVA O TEXTO DA CAIXA E APAGA O TEXTO
        self.escolha_usuario = self.caixa_Flagle.get()
        self.caixa_Flagle.delete(0, tk.END)
        
        #COMPARACAO COM A BANDEIRA ESCOLHIDA e revelação da bandeira 
        ### RESPOSTA CERTA
        if self.escolha_usuario == self.alternativa_certa:
            self.bloco_1.destroy()
            self.bloco_2.destroy()
            self.bloco_3.destroy()
            self.bloco_4.destroy()
            self.bloco_5.destroy()
            self.bloco_6.destroy()
            self.bloco_7.destroy()
            self.bloco_8.destroy()
            self.bloco_9.destroy()
            self.bloco_10.destroy()
            self.bloco_11.destroy()
            self.bloco_12.destroy()
  
            
            ## Remover caixa e botao 
            self.caixa_Flagle.destroy() #Destruir a caixa de entrada
            self.botao_caixa_entrada.destroy() #Destruir o botao da caixa de entrada
            
            # Revelar nome do país 
            self.label_revelacao_nome= tk.Label(self.master, text=(self.alternativa_certa),font=("Luckiest Guy", 52), bg="#b2dfff", fg="black")
            self.label_revelacao_nome.place(relx=0.5, rely=0.15, anchor="center")
            
            #JOGAR NOVAMENTE
            self.botao_jogar_novamente2 = tk.Button(self.master, text="Jogar novamente",font=("Luckiest Guy", 20),
                              fg="black", bg="white", width=14, height=1, command=self.comando_jogar_novamente_Flagle)
            self.botao_jogar_novamente2.place(relx=0.5, rely=0.6, anchor="center")
            
            # Botão sair
            self.botao_sair_flagle = tk.Button(self.master, text="Sair",
                                                    font=("Luckiest Guy", 20),fg="black", bg="white", width=14, height=1, command=self.SairFagle)
            self.botao_sair_flagle.place(relx=0.5, rely=0.7, anchor="center")
            
        ## RESPOSTA ERRADA
        elif self.contador < 7:
            self.escolha_bloco_destruir = random.choice(self.blocos_Medio)
            self.escolha_bloco_destruir.destroy()
            self.blocos_Medio.remove(self.escolha_bloco_destruir)
            self.contador += 1
            return
            
        else:
            # Oitava tentativa: fim de jogo
            self.escolha_bloco_destruir = random.choice(self.blocos_Medio)
            self.escolha_bloco_destruir.destroy()
            self.blocos_Medio.remove(self.escolha_bloco_destruir)
            
            #Acabar com os bloquinhos que ainda restam
            for bloco in self.blocos_Medio:
                bloco.destroy()

            # limpar lista depois de destruir os bloquinhos
            self.blocos_Medio.clear()
    
            # Destruir entrada
            self.caixa_Flagle.destroy()
            self.botao_caixa_entrada.destroy()
    
            # Destruir entrada
            self.caixa_Flagle.destroy()
            self.botao_caixa_entrada.destroy()
    
            # Revelar nome do país
            self.label_revelacao_nome = tk.Label(self.master,text=self.alternativa_certa, font=("Luckiest Guy", 52), bg="#b2dfff", fg="black")
            self.label_revelacao_nome.place(relx=0.5, rely=0.15, anchor="center")
    
            # Botão jogar novamente
            self.botao_jogar_novamente2 = tk.Button(self.master, text="Jogar novamente",
                                                    font=("Luckiest Guy", 20),fg="black", bg="white", width=14, height=1, command=self.comando_jogar_novamente_Flagle)
            self.botao_jogar_novamente2.place(relx=0.5, rely=0.6, anchor="center")
            
            # Botão sair
            self.botao_sair_flagle = tk.Button(self.master, text="Sair",
                                                    font=("Luckiest Guy", 20),fg="black", bg="white", width=14, height=1, command=self.SairFagle)
            self.botao_sair_flagle.place(relx=0.5, rely=0.7, anchor="center")

        
    def comando_jogar_novamente_Flagle_2(self):
        root5 = self.master  # salva referência
        root5.destroy()      # destrói a janela inteira

        # cria uma janela nova 
        resetar_Flagle = tk.Tk()
        self.flagle_medio(resetar_Flagle)
        resetar_Flagle.mainloop()
        
        
    def flagle_dificil(self):
        
        #Destruir botoes de escolha de nivel flagle
        self.botao_flagle_facil.destroy()
        self.botao_flagle_medio.destroy()
        self.botao_flagle_dificil.destroy()
            
        # ESCOLHENDO A BANDEIRA E OPCOES CERTAS E ERRADAS
        self.alternativa_certa_original, self.arquivo_certo = random.choice(bandeiras)
        
        #NORMALIZANDO OS NOMES EM TUDO MINUSCULA
        self.alternativa_certa = self.alternativa_certa_original.lower()
        # COLOCANDO A BANDEIRA NA TELA
        self.bandeira_tela = tk.PhotoImage(file=self.arquivo_certo)
        
        if "np" in self.arquivo_certo:
            self.bandeira_tela = self.bandeira_tela.subsample(1, 1)
        else:
            self.bandeira_tela = self.bandeira_tela.subsample(2, 2)

        self.label_bandeira_tela = tk.Label(self.master, image=self.bandeira_tela, bd=0)
        self.label_bandeira_tela.place(relx=0.5, rely=0.35, anchor="center")
        self.label_bandeira_tela.lift()
        
        #CANVAS BLOQUINHOS
        
        # BLOQUINHOS PRIMEIRA LINHA
        self.bloco_1 = tk.Canvas(self.master, height=45, width=65, bg="black", highlightthickness=1)
        self.bloco_1.place(relx=0.36, rely=0.195)
        
        self.bloco_2 = tk.Canvas(self.master, height=45, width=65, bg="black", highlightthickness=1)
        self.bloco_2.place(relx=0.406, rely=0.195)
        
        self.bloco_3 = tk.Canvas(self.master, height=45, width=65, bg="black", highlightthickness=1)
        self.bloco_3.place(relx=0.453, rely=0.195)
        
        self.bloco_4 = tk.Canvas(self.master, height=45, width=65, bg="black", highlightthickness=1)
        self.bloco_4.place(relx=0.499, rely=0.195)
        
        self.bloco_5 = tk.Canvas(self.master, height=45, width=65, bg="black", highlightthickness=1)
        self.bloco_5.place(relx=0.546, rely=0.195)
        
        self.bloco_6 = tk.Canvas(self.master, height=45, width=65, bg="black", highlightthickness=1)
        self.bloco_6.place(relx=0.5923, rely=0.195)
        
        
        # BLOCOS 2ª LINHA
        self.bloco_7 = tk.Canvas(self.master, height=45, width=65, bg="black", highlightthickness=1)
        self.bloco_7.place(relx=0.36, rely=0.248)
        
        self.bloco_8 = tk.Canvas(self.master, height=45, width=65, bg="black", highlightthickness=1)
        self.bloco_8.place(relx=0.406, rely=0.248)
        
        self.bloco_9 = tk.Canvas(self.master, height=45, width=65, bg="black", highlightthickness=1)
        self.bloco_9.place(relx=0.453, rely=0.248)
        
        self.bloco_10 = tk.Canvas(self.master, height=45, width=65, bg="black", highlightthickness=1)
        self.bloco_10.place(relx=0.499, rely=0.248)
        
        self.bloco_11 = tk.Canvas(self.master, height=45, width=65, bg="black", highlightthickness=1)
        self.bloco_11.place(relx=0.546, rely=0.248)
        
        self.bloco_12 = tk.Canvas(self.master, height=45, width=65, bg="black", highlightthickness=1)
        self.bloco_12.place(relx=0.5923, rely=0.248)
        
        
        # BLOCOS 3ª LINHA
        self.bloco_13 = tk.Canvas(self.master, height=45, width=65, bg="black", highlightthickness=1)
        self.bloco_13.place(relx=0.36, rely=0.3001)
        
        self.bloco_14 = tk.Canvas(self.master, height=45, width=65, bg="black", highlightthickness=1)
        self.bloco_14.place(relx=0.406, rely=0.3001)
        
        self.bloco_15 = tk.Canvas(self.master, height=45, width=65, bg="black", highlightthickness=1)
        self.bloco_15.place(relx=0.453, rely=0.3001)
        
        self.bloco_16 = tk.Canvas(self.master, height=45, width=65, bg="black", highlightthickness=1)
        self.bloco_16.place(relx=0.499, rely=0.3001)
        
        self.bloco_17 = tk.Canvas(self.master, height=45, width=65, bg="black", highlightthickness=1)
        self.bloco_17.place(relx=0.546, rely=0.3001)
        
        self.bloco_18 = tk.Canvas(self.master, height=45, width=65, bg="black", highlightthickness=1)
        self.bloco_18.place(relx=0.5923, rely=0.3001)
        
        
        # BLOCOS 4ª LINHA
        self.bloco_19 = tk.Canvas(self.master, height=45, width=65, bg="black", highlightthickness=1)
        self.bloco_19.place(relx=0.36, rely=0.352)
        
        self.bloco_20 = tk.Canvas(self.master, height=45, width=65, bg="black", highlightthickness=1)
        self.bloco_20.place(relx=0.406, rely=0.352)
        
        self.bloco_21 = tk.Canvas(self.master, height=45, width=65, bg="black", highlightthickness=1)
        self.bloco_21.place(relx=0.453, rely=0.352)
        
        self.bloco_22 = tk.Canvas(self.master, height=45, width=65, bg="black", highlightthickness=1)
        self.bloco_22.place(relx=0.499, rely=0.352)
        
        self.bloco_23 = tk.Canvas(self.master, height=45, width=65, bg="black", highlightthickness=1)
        self.bloco_23.place(relx=0.546, rely=0.352)
        
        self.bloco_24 = tk.Canvas(self.master, height=45, width=65, bg="black", highlightthickness=1)
        self.bloco_24.place(relx=0.5923, rely=0.352)
        
        
        # BLOCOS 5ª LINHA
        self.bloco_25 = tk.Canvas(self.master, height=45, width=65, bg="black", highlightthickness=1)
        self.bloco_25.place(relx=0.36, rely=0.402)
        
        self.bloco_26 = tk.Canvas(self.master, height=45, width=65, bg="black", highlightthickness=1)
        self.bloco_26.place(relx=0.406, rely=0.402)
        
        self.bloco_27 = tk.Canvas(self.master, height=45, width=65, bg="black", highlightthickness=1)
        self.bloco_27.place(relx=0.453, rely=0.402)
        
        self.bloco_28 = tk.Canvas(self.master, height=45, width=65, bg="black", highlightthickness=1)
        self.bloco_28.place(relx=0.499, rely=0.402)
        
        self.bloco_29 = tk.Canvas(self.master, height=45, width=65, bg="black", highlightthickness=1)
        self.bloco_29.place(relx=0.546, rely=0.402)
        
        self.bloco_30 = tk.Canvas(self.master, height=45, width=65, bg="black", highlightthickness=1)
        self.bloco_30.place(relx=0.5923, rely=0.402)
        
        
        # BLOCOS 6ª LINHA
        self.bloco_31 = tk.Canvas(self.master, height=45, width=65, bg="black", highlightthickness=1)
        self.bloco_31.place(relx=0.36, rely=0.454)
        
        self.bloco_32 = tk.Canvas(self.master, height=45, width=65, bg="black", highlightthickness=1)
        self.bloco_32.place(relx=0.406, rely=0.454)
        
        self.bloco_33 = tk.Canvas(self.master, height=45, width=65, bg="black", highlightthickness=1)
        self.bloco_33.place(relx=0.453, rely=0.454)
        
        self.bloco_34 = tk.Canvas(self.master, height=45, width=65, bg="black", highlightthickness=1)
        self.bloco_34.place(relx=0.499, rely=0.454)
        
        self.bloco_35 = tk.Canvas(self.master, height=45, width=65, bg="black", highlightthickness=1)
        self.bloco_35.place(relx=0.546, rely=0.454)
        
        self.bloco_36 = tk.Canvas(self.master, height=45, width=65, bg="black", highlightthickness=1)
        self.bloco_36.place(relx=0.5923, rely=0.454)

        
        # lista blocos flagle dificil
        self.blocos_Dificil = [self.bloco_1, self.bloco_2, self.bloco_3, self.bloco_4, self.bloco_5,
            self.bloco_6, self.bloco_7, self.bloco_8, self.bloco_9, self.bloco_10,
            self.bloco_11, self.bloco_12, self.bloco_13, self.bloco_14, self.bloco_15,
            self.bloco_16, self.bloco_17, self.bloco_18, self.bloco_19, self.bloco_20,
            self.bloco_21, self.bloco_22, self.bloco_23, self.bloco_24, self.bloco_25,
            self.bloco_26, self.bloco_27, self.bloco_28, self.bloco_29, self.bloco_30,
            self.bloco_31, self.bloco_32, self.bloco_33, self.bloco_34, self.bloco_35,
            self.bloco_36]

        
        # CAIXA DE ENTRADA
        self.caixa_Flagle = tk.Entry(self.master, width=16, font=("Luckiest Guy", 18), bg="white", fg="black")
        self.caixa_Flagle.place(relx=0.5, rely=0.6, anchor="center")
        
        #BOTAO NA CAIXA DE ENTRADA
        self.botao_caixa_entrada = tk.Button(self.master, text="OK",font=("Luckiest Guy", 20),
                          fg="black", bg="white", width=1, height=1, command = self.tentativa_3)
        self.botao_caixa_entrada.place(relx=0.58, rely=0.6, anchor="center")
        
        self.master.bind("<Return>", self.tentativa_3)
    
        
    def tentativa_3(self, ev=None):
        
        #SALVA O TEXTO DA CAIXA E APAGA O TEXTO
        self.escolha_usuario = self.caixa_Flagle.get()
        self.caixa_Flagle.delete(0, tk.END)
        
        #COMPARACAO COM A BANDEIRA ESCOLHIDA e revelação da bandeira 
        ### RESPOSTA CERTA
        if self.escolha_usuario == self.alternativa_certa:
            self.bloco_1.destroy()
            self.bloco_2.destroy()
            self.bloco_3.destroy()
            self.bloco_4.destroy()
            self.bloco_5.destroy()
            self.bloco_6.destroy()
            self.bloco_7.destroy()
            self.bloco_8.destroy()
            self.bloco_9.destroy()
            self.bloco_10.destroy()
            self.bloco_11.destroy()
            self.bloco_12.destroy()
            self.bloco_13.destroy()
            self.bloco_14.destroy()
            self.bloco_15.destroy()
            self.bloco_16.destroy()
            self.bloco_17.destroy()
            self.bloco_18.destroy()
            self.bloco_19.destroy()
            self.bloco_20.destroy()
            self.bloco_21.destroy()
            self.bloco_22.destroy()
            self.bloco_23.destroy()
            self.bloco_24.destroy()
            self.bloco_25.destroy()
            self.bloco_26.destroy()
            self.bloco_27.destroy()
            self.bloco_28.destroy()
            self.bloco_29.destroy()
            self.bloco_30.destroy()
            self.bloco_31.destroy()
            self.bloco_32.destroy()
            self.bloco_33.destroy()
            self.bloco_34.destroy()
            self.bloco_35.destroy()
            self.bloco_36.destroy()
            

            ## Remover caixa e botao 
            self.caixa_Flagle.destroy() #Destruir a caixa de entrada
            self.botao_caixa_entrada.destroy() #Destruir o botao da caixa de entrada
            
            # Revelar nome do país 
            self.label_revelacao_nome= tk.Label(self.master, text=(self.alternativa_certa),font=("Luckiest Guy", 52), bg="#b2dfff", fg="black")
            self.label_revelacao_nome.place(relx=0.5, rely=0.15, anchor="center")
            
            #JOGAR NOVAMENTE
            self.botao_jogar_novamente2 = tk.Button(self.master, text="Jogar novamente",font=("Luckiest Guy", 20),
                              fg="black", bg="white", width=14, height=1, command=self.comando_jogar_novamente_Flagle)
            self.botao_jogar_novamente2.place(relx=0.5, rely=0.6, anchor="center")
            
            
        ## RESPOSTA ERRADA
        elif self.contador < 9:
            self.escolha_bloco_destruir = random.choice(self.blocos_Dificil)
            self.escolha_bloco_destruir.destroy()
            self.blocos_Dificil.remove(self.escolha_bloco_destruir)
            self.contador += 1
            return
            
        else:
            self.escolha_bloco_destruir = random.choice(self.blocos_Dificil)
            self.escolha_bloco_destruir.destroy()
            self.blocos_Dificil.remove(self.escolha_bloco_destruir)
            
            #Acabar com os bloquinhos que ainda restam
            for bloco in self.blocos_Dificil:
                bloco.destroy()

            # limpar lista depois de destruir os bloquinhos
            self.blocos_Dificil.clear()
    
            # Destruir entrada
            self.caixa_Flagle.destroy()
            self.botao_caixa_entrada.destroy()
    
            # Revelar nome do país
            self.label_revelacao_nome = tk.Label(self.master,text=self.alternativa_certa, font=("Luckiest Guy", 52), bg="#b2dfff", fg="black")
            self.label_revelacao_nome.place(relx=0.5, rely=0.15, anchor="center")
    
            # Botão jogar novamente
            self.botao_jogar_novamente2 = tk.Button(self.master, text="Jogar novamente",
                                                    font=("Luckiest Guy", 20),fg="black", bg="white", width=14, height=1, command=self.comando_jogar_novamente_Flagle)
            self.botao_jogar_novamente2.place(relx=0.5, rely=0.6, anchor="center")
            
        
    def comando_jogar_novamente_Flagle_3(self):
        root5 = self.master  # salva referência
        root5.destroy()      # destrói a janela inteira

        # cria uma janela nova
        resetar_Flagle = tk.Tk()
        Flagle(resetar_Flagle)
        resetar_Flagle.mainloop()
        
       
     
# Execução principal
if __name__ == "__main__":
    Interface()






























