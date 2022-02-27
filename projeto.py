from time import sleep 
import os

nome = str(input('Para iniciar o programa digite seu nome: '))  
sleep(2)
print(f'\n\033[1;35mOlá, {nome}. Este programa foi feito para ajudar no estudo da pontuação e auxiliar  no desenvolvimento da escrita. ')
sleep(2)
print('\nVamos começar!\033[m')
sleep(2)
print('\n\033[1;36mA pontuação é feita através dos sinais de pontuação sendo eles: ponto final, dois pontos, reticências, parênteses, ponto de exclamação, ponto de interrogação, vírgula, ponto e vírgula, travessão e aspas. Esses sinais desempenham a função de manifestar a fala na escrita, atribuindo ritmo, entonação, pausa e construção sintática, gerando a coesão entre as estruturas das orações.\033[m\n')
input('\n\033[1;35mPressione qualquer tecla para continuar...\033[m\n')
sleep(2)
os.system('clear')
print('\033[1;35mPara continuar a execução do programa escolha uma opção do menu que será apresentado. \033[m')
sleep(3)

while True:
    print('\nESCOLHA UMA OPÇÃO:')
    print('---' * 10)
    print('[1] - Ponto final (.)')
    print('[2] - Dois-pontos (:)')
    print('[3] - Reticências (...)')
    print('[4] - Parênteses (())')
    print('[5] - Ponto de exclamação (!)')
    print('[6] - Ponto de interrogação (?)')
    print('[7] - Vírgula (,)')
    print('[8] - Ponto e vírgula (;)')
    print('[9] - Travessão (—)')
    print('[10] - Aspas (“ ”)')
    print('[11] - Exercícios')
    print('[12] - Fontes')
    print('[13] - Encerrar programa')
    print('---' * 10)
    opcao = int(input())
    print('---' * 10)

    if opcao == 1:
        sleep(2)
        os.system('clear')
        sleep(1)
        print('''\n\033[1;30;43m[1] - Ponto final (.)\033[m

    O ponto ou ponto-final é utilizado das seguintes maneiras: 

    a) Encerrar uma frase declarativa: 
    Ex. Gosto de assistir filmes.
 
    b) Separar e encerrar períodos:
    Ex. Ainda é cedo. Vou dormir mais um pouco
  
    c) Abreviar palavras:
    Ex. Sr. Pedro, você chegou cedo hoje.\n''')
        input('\n\033[1;35mPressione qualquer tecla para continuar...\033[m\n')
        sleep(2)
        os.system('clear')
        sleep(1)
    elif opcao == 2:
        sleep(2)
        os.system('clear')
        sleep(1)
        print('''\n\033[1;30;43m[2] - Dois-pontos (:)\033[m
        
    Os dois-pontos são usados das seguintes formas:

    a) Citações:
 
    Ex. É como disse Sócrates: “Só sei que nada sei.”

    b) Introduzir uma enumeração::
 
    Ex. Os planetas do sistema solar são: Mercúrio, Vênus, Terra, Marte, Júpiter, Saturno, Urano e Netuno.

    c) Exemplos:
 
    Ex. O substantivo é uma classe de palavra que nomeia os seres, por exemplo: casa, carro, móvel.

    d) Explicações:
 
    Ex. O empreendedorismo corresponde a um conceito novo que inclui conceitos essenciais: a proatividade e a capacidade de criar algo inovador.

    e) Discursos diretos:
 
    Ex. Após ouvir atentamente a pergunta da professora, José respondeu: — Não estou preparado para a prova.

    f) Após vocativos:
 
    Ex. Senhora Daiana: Podemos participar do evento no sábado?\n''')
        input('\n\033[1;35mPressione qualquer tecla para continuar...\033[m\n')
        sleep(2)
        os.system('clear')
        sleep(1)
    elif opcao == 3:
        sleep(2)
        os.system('clear')
        sleep(1)
        print('''\n\033[1;30;43m[3] - Reticências (...)\033[m
        
    As reticências são usadas para: 

    a) Interromper ideias:

    Ex. Quantas atividades… “Tô” cansado só de pensar.

    b) Indicar indecisões:

    Ex. Não sei se como este bolo… Posso ficar com dor de barriga.

    c) Realçar discursos
 
    Ex. Esse bolo… é delicioso.

    d) Transmissão de sentimentos:

    Ex. Tanto fiz por ele... sem ajuda... sozinha... consegui!\n''')
        input('\n\033[1;35mPressione qualquer tecla para continuar...\033[m\n')
        sleep(2)
        os.system('clear')
        sleep(1)
    elif opcao == 4:
        sleep(2)
        os.system('clear')
        sleep(1)
        print('''\n\033[1;30;43m[[4] - Parênteses (())\033[m

    Os parênteses são usados das seguintes formas:

    a) Para separar palavras ou frases que acrescente alguma informação ou explicação: 

    Ex. Cheguei em casa cansada, jantei (um prato de e um suco) e adormeci no sofá.

    b) Em citações, indicando autores, obras, capítulos e páginas referentes a citação:

    Ex. “A imaginação é mais importante que o conhecimento.” (Albert Einstein)

    c) Indicar alternativas para palavras:

    Ex. Caro(s) Senhor(es), agradecemos o contato.\n''')
        input('\n\033[1;35mPressione qualquer tecla para continuar...\033[m\n')
        sleep(2)
        os.system('clear')
        sleep(1)
    elif opcao == 5:
        sleep(2)
        os.system('clear')
        sleep(1)
        print('''\n\033[1;30;43m[5] - Ponto de exclamação (!)\033[m]
    A exclamação, como seu próprio diz, é usada para exclamar sendo utilizada das seguintes formas:

    a) Expressar sentimentos diversos como: ordem, alegria, espanto e etc.

    Ex. Que nojo!
        Amei!
        Suma!

    b) Após vocativo:
    Obs. Vocativo é o termo que serve para chamar, invocar ou interpelar um ouvinte real ou hipotético, normalmente separado por vírgula.

    Ex. Bom dia, Maria!

    c) Após interjeição:
    Obs. Interjeição é a expressão de diferentes emoções.

    Ex.  Ui! que susto você me deu.\n''')
        input('\n\033[1;35mPressione qualquer tecla para continuar...\033[m\n')
        sleep(2)
        os.system('clear')
        sleep(1)
    elif opcao == 6:
        sleep(2)
        os.system('clear')
        sleep(1)
        print('''\n\033[1;30;43m[6] - Ponto de interrogação (?)\033[m

    O ponto de interrogação é usado em frases interrogativas e é utilizado das seguintes formas

    a) Em perguntas diretas:
    Obs. Perguntas diretas começam com palavras interrogativas e terminam com a interrogação. Já as perguntas indiretas insinuam uma indagação e terminam com ponto final.

    Ex. Qual sua música preferida ?

    b) Junto com a exclamação com para causar enfatize:

    Ex. Não acredito, é sério?!\n''')
        input('\n\033[1;35mPressione qualquer tecla para continuar...\033[m\n')
        sleep(2)
        os.system('clear')
        sleep(1)
    elif opcao == 7:
        sleep(2)
        os.system('clear')
        sleep(1)
        print('''\033[1;30;43m\n [7] - Vírgula (,)\033[m

    A vírgula é usada das seguintes formas:

    a) Separar elementos em uma enumeração:
 
    Ex. Meus sabores de sorvetes prediletos são os de chocolate, flocos e morango.

    b) Separar o vocativo:

    Ex. Maria, vá à padaria comprar pães para o jantar.
 
    c) Separar o aposto
    Obs. O aposto é o nome que se dá ao termo que exemplifica ou especifica melhor outro de valor substantivo ou pronominal.

    Ex. João, professor do Ensino Médio, está de licença.

    d) Após dos advérbios “sim” e “não”, quando são usadas como resposta: 

    Ex. Sim, o almoço está delicioso.

    e) Separar locais e datas:

    Ex. Arapiraca, 21 de janeiro de 2022.

    f) Separar orações subordinadas adverbiais:
    Obs. As orações subordinadas adverbiais são aquelas que possuem a função do advérbio, funcionando como adjunto adverbial na frase.

    Obs. O Adjunto adverbial é o termo que tem a função de advérbio nas orações. Indicando circunstâncias, como tempo, modo e finalidade.

    Ex. Embora estivesse mau tempo, foram à praia.

    h) Separar orações subordinadas adjetivas explicativas:
    Obs. Oração subordinada adjetiva é aquela que se encaixa na oração principal, funcionando como adjunto adnominal. Classificam-se em: explicativas e restritivas. 
         Explicativas: acrescentam uma qualidade acessória ao antecedente e são separadas da oração principal por vírgulas.

     Obs. Adjunto adnominal é o termo acessório da oração que tem a função de caracterizar ou determinar um substantivo. Isso pode ser feito através de artigos, adjetivos e outros elementos que desempenhem a função adjetiva.

     Ex. Os jogadores de futebol, que são iniciantes, não recebem salários.

     i) Omitir verbos para evitar repetições:

     Ex. Vamos de carro; eles, de ônibus.''')
        input('\n\033[1;35mPressione qualquer tecla para continuar...\033[m\n')
        sleep(2)
        os.system('clear')
        sleep(1)
    elif opcao == 8:
        sleep(2)
        os.system('clear')
        sleep(1)
        print('''\n\033[1;30;43m[8] - Ponto e vírgula (;)\033[m

    O ponto e vírgula é usado das seguintes formas:

    a) Separar oraçẽos coordenadas onde se faz muito uso da vírgula, ou ainda, textos extensos: 
    Obs. Orações Coordenadas são orações encontradas em um mesmo período, mas entre si são independentes sintaticamente.

    Ex. As sete maravilhas do mundo moderno representam monumentos que fazem parte da história da humanidade: o Coliseu, na Itália; a Chichén Itzá, no México; o Machu Picchu, no Peru; o Cristo Redentor, no Brasil; a Muralha da China, na China; as Ruínas de Petra, na Jordânia; o Taj Mahal, na Índia.

    b) Separar ou enumerar elementos:

    Ex. No capítulo a seguir estudaremos os seguintes temas: Idade Antiga; Idade Média; Idade Contemporânea.

    c)  Omitir verbos evitando a repetição:

    Ex. Na hora do crime Rafaela estava com os amigos; José (estava) com seus pais. 

    d) Separar conjunções adverbiais:
    Obs.  As conjunções adversativas ligam duas orações independentes fazendo uso de oposições.

    Ex. Amanhã vou ao trabalho; entretanto, não terminei o relatório.\n''')
        input('\n\033[1;35mPressione qualquer tecla para continuar...\033[m\n')
        sleep(2)
        os.system('clear')
        sleep(1)
    elif opcao == 9:
        sleep(2)
        os.system('clear')
        sleep(1)
        print('''\n\033[1;30;43m[9] - Travessão (—)\033[m

    O travessão é  utilizado das seguintes formas:

    a) Iniciar e indicar a troca de interlocutores em um diálogo:
    Obs. Interlocutor é quem participa de uma conversa, diálogo.

    Ex. - Você fez a atividade de casa ?
        - Tinha atividade de casa ?

    b) Substituir a vírgula em frases explicativas:

    Ex. Seiya – o cavaleiro de pégasus – Seiya – o cavaleiro de pégasus – caiu, mais uma vez.\n''' )
        input('\n\033[1;35mPressione qualquer tecla para continuar...\033[m\n')
        sleep(2)
        os.system('clear')
        sleep(1)
    elif opcao == 10:
        sleep(2)
        os.system('clear')
        sleep(1)
        print('''\n\033[1;30;43m[10] - Aspas (“ ”)\033[m
        
    As aspas são utilizadas das seguintes formas:    

    a) Fazer citações:

    Ex. “Ia viajar! Viajei. Trinta e quatro vezes, às pressas, bufando, com todo o sangue na face, desfiz e refiz a mala”. (O prazer de viajar - Eça de Queirós)

    b) Uso de expressões estrangeiras, neologismos, gírias:

    Ex. A aula do professor foi “irada”
        Fiz o “backup” dos arquivos.

    c) b) Expressar ironia:

    Ex. Eles são uns “anjinhos”. \n''')
        input('\n\033[1;35mPressione qualquer tecla para continuar...\033[m\n')
        sleep(2)
        os.system('clear')
        sleep(1)
    elif opcao == 11:
        sleep(2)
        os.system('clear')
        sleep(1)
        print('''\n\033[1;30;43m[11] - Exercícios\033[m
    
\033[1;35mOs exercícios são feitos com dez questões, você começará com 0 pontos. Para cada questão respondida corretamente você ganhará 10 pontos, caso contrário perderá 10 pontos.  \n'''
              )

        sleep(3)
        print('Vamos começar! Boa Sorte!\033[m\n')
        sleep(2)

        gab = ["A", "C", "ponto final", "E", "B", "C", "interrogativa", "virgula","D", "C"]
        resp = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
        acertos = 0
        pontos = 100

        print('''\n1. Marque a opção onde os sinais de pontuação correspondentes a cada frase estão corretos.

# Você gosta de melancia __
# Muitos parabéns _ 
# Estamos esperando por você há duas horas _
# As horas passavam _

a) ? - ! - . - …
b) . - ? - … - ! 
c) ! - … - ? - .
d) … - . - ! - ? ''')
        resp[0] = str(input('Digite: ')).upper()
        sleep(2)

        print('''\n2. Marque a alternativa onde o uso da vírgula está incorreto.

a) Paula Marques, a professora mais exigente da escola, foi homenageada pelos alunos.
b) Cansado da vida que tinha, Rodrigo decidiu que estava na hora de recomeçar.
c) D. Helena e Sr. Paulo, são os melhores funcionários da empresa.
d) Amanhã chegam meus primos preferidos, meus companheiros de infância, meus melhores amigos.'''
        )
        resp[1] = str(input('Digite: ')).upper()
        sleep(2)

        print('\n3. Qual sinal de pontuação é usado para finalizar uma frase declarativa ?')
        resp[2] = str(input('Digite: ')).lower()
        sleep(2)

        print(
            '''\n4. Аѕѕіnаlе а аltеrnаtіvа соrrеtа еm rеlаçãо ао uѕо dа vírgulа nа ѕеguіntе frаѕе:

a) "Fіlhа quаl é о nоmе dо аmіgо dо ѕеu раі, mеѕmо?"
b) "Fіlhа quаl é о nоmе, dо аmіgо dо ѕеu раі mеѕmо?"
c) "Fіlhа quаl é о nоmе dо аmіgо, dо ѕеu раі mеѕmо?"
d) "Fіlhа quаl, é о nоmе dо аmіgо dо ѕеu раі mеѕmо?"
e) "Fіlhа, quаl é о nоmе dо аmіgо dо ѕеu раі mеѕmо?"''')
        resp[3] = str(input('Digite: ')).upper()
        sleep(2)

        print('''\n5. Аѕѕіnаlе а аltеrnаtіvа quе арrеѕеntе еrrо dе роntuаçãо

a) А mаtérіа dа рrоvа еrа dо соnhесіmеntо dе tоdоѕ; muіtоѕ nãо еѕtudаrаm, роrém.
b) Еrа dо соnhесіmеntо dе tоdоѕ а mаtérіа dа рrоvа, mаѕ, muіtоѕ nãо еѕtudаrаm.
c) Тоdоѕ ѕаbеm а mаtérіа dа рrоvа; еѕtudеm, роіѕ.
d) Тоdоѕ ѕаbеm а mаtérіа dа рrоvа, роrtаntо еѕtudеm!''')
        resp[4] = str(input('Digite: ')).upper()
        sleep(2)

        print(
            '''\n6. Аѕѕіnаlе а аltеrnаtіvа соrrеtа utilizando ѕеuѕ соnhесіmеntоѕ ѕоbrе оѕ ѕіnаіѕ dе роntuаçãо.

a) Раrа introduzir uma еnumеrаçãо, uѕаmоѕ аѕраѕ.
b) Раrа fіnаlіzаr umа frаѕе dесlаrаtіvа соm ѕеntіdо соmрlеtо, uѕаmоѕ роntо dе іntеrrоgаçãо.
c) Раrа introduzir uma еnumеrаçãо, uѕаmоѕ dois роntоs.
d) Uѕаmоѕ роntо fіnаl раrа fіnаlіzаr umа frаѕе еxсlаmaаtіvа.''')
        resp[5] = str(input('Digite: ')).upper()
        sleep(2)

        print(
            '''\n7. Em que tipo de frase é usado o ponto de interrogação ?''')
        resp[6] = str(input('Digite: ')).lower()
        sleep(2)

        print(
            '''\n8.  Separar os advérbios sim e não em respostas é função de qual sinal de pontuação ?''')
        resp[7] = str(input('Digite: ')).lower()
        sleep(2)

        print('''\n9. Ѕоbrе о роntо fіnаl роdеmоѕ аfіrmаr...

a) é utіlіzаdо раrа tеrmіnаr а іdеіа оu dіѕсurѕо.
b) é utіlіzаdо раrа іndісаr о fіnаl dе um реríоdо.
c) é, аіndа, utіlіzаdо nаѕ аbrеvіаçõеѕ.
d)tоdаѕ аѕ орçõеѕ асіmа''')
        resp[8] = str(input('Digite: ')).upper()
        sleep(2)

        print('''\n10. Quаl frаѕе арrеѕеntа а роntuаçãо іnсоrrеtа?

a) Јоаnа ехрlісоu: — Nãо dеvеmоѕ ріѕаr nа grаmа dо раrquе.
b) Јоаquіm сеlеbrоu ѕеu аnіvеrѕárіо nа рrаіа; nãо gоѕtа dо frіо е nеm dаѕ mоntаnhаѕ.
c) Оntеm, ѕоnhеі соm, ѕuа mãе.
d) Nãо ѕеі… Рrесіѕо реnѕаr nо аѕѕuntо''')
        resp[9] = str(input('Digite: ')).upper()
        sleep(2)

        for i in range(0, 10, 1):
            if gab[i] == resp[i]:
                acertos += 1
            else:
                pontos -= 10

        sleep(2)
        print(f'\n\033[mSuas respostas foram:\033[m\n{resp}\n')
        sleep(1)
   
        print('\033[1;32m*****************************************')
        sleep(1)
        print(f'Você acertou {acertos} questões e conseguiu {pontos}\033[m')
        sleep(1)
        if acertos < 5:
            print('\033[1;31m********* VAMOS ESTUDAR MAIS ************\033[m')
            sleep(1)
        print('\033[1;32m*****************************************\033[m\n')
        sleep(2)
        input('\n\033[1;35mPressione qualquer tecla para continuar...\033[m\n')
        sleep(1)
        os.system('clear')
        sleep(2)   

    elif opcao == 12:
        sleep(2)
        os.system('clear')
        sleep(1)
        print('''\n\033[1;30;43m[12] - Fontes\033[m
        
    \033[1;36mVídeos do Youtube:\033[m

    https://www.youtube.com/watch?v=ODkVN0kRciE
    https://www.youtube.com/watch?v=9tdpcfdr244
    https://www.youtube.com/watch?v=HwMYC5pFJGo

    \033[1;36mSites:\033[m

    https://www.todamateria.com.br/sinais-de-pontuacao/
    https://www.todamateria.com.br/uso-dos-parenteses/
    https://www.infoescola.com/portugues/pontuacao/
    https://www.portugues.com.br/gramatica/pontuacao.html
    https://brasilescola.uol.com.br/redacao/pontuacao.htm
    https://www.soportugues.com.br/secoes/sint/sint23.php
    https://www.jurisway.org.br/v2/pergunta.asp?idmodelo=8149
    https://www.todamateria.com.br/uso-das-reticencias/
    https://www.todamateria.com.br/dois-pontos/
    https://www.todamateria.com.br/usos-da-virgula-aprenda-os-truques/
    https://www.todamateria.com.br/oracoes-subordinadas-adverbiais/
    https://www.todamateria.com.br/adjunto-adverbial/
    https://mundoeducacao.uol.com.br/gramatica/oracao-subordinada-adjetiva.htm
    https://www.todamateria.com.br/adjunto-adnominal/
    https://www.todamateria.com.br/ponto-e-virgula/
    https://www.educamaisbrasil.com.br/enem/lingua-portuguesa/oracoes-coordenadas 
    https://www.significados.com.br/conjuncao/ 
    https://www.normaculta.com.br/sinais-de-pontuacao-exercicios/
    https://www.quiz.com.br/quiz/3688/exercicios-sobre-sinais-de-pontuacao-i/3g23nw16/\n''')
        input('\n\033[1;35mPressione qualquer tecla para continuar...\033[m\n')
        sleep(1)
        os.system('clear')
        sleep(2)
    elif opcao == 13:
        sleep(2)
        os.system('clear')
        sleep(1)
        print('\n\033[1;35mObrigado por usar o pragrama!')
        sleep(2)
        print('Encerrando...')
        sleep(2)
        print('TCHAU!\033[m')
        break
    else:
        sleep(2)
        os.system('clear')
        sleep(1)
        print('\n\033[1;31m**********************************')
        print('OPÇÃO INVÁLIDA. ESCOLHA NOVAMENTE')
        print('**********************************\033[m')
        input('\n\033[1;35mPressione qualquer tecla para continuar...\033[m\n')
        sleep(1)
        os.system('clear')
        sleep(2)