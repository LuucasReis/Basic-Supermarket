#itens do supermercado
import time
menu_supermercado= []
def cadastroprodutos(nome, valor):
    tupla= (nome,valor)
    menu_supermercado.append(tupla)
    return menu_supermercado
cadastroprodutos('Maracuja', '1.20'), 
cadastroprodutos('Arroz', '5.00'), 
cadastroprodutos('Feijao', '3.00'), 
cadastroprodutos('Frango', '13.00'), 
cadastroprodutos('Pente de ovos', '15.00'),
cadastroprodutos('Meia duzia de ovos', '12.00'), 
cadastroprodutos('Nuggets tradicional', '10.50'), 
cadastroprodutos('Nuggets sabor queijo', '15.95'), 
cadastroprodutos('Requeijao', '7.00'),
cadastroprodutos('Queijo minas', '5.50'),
cadastroprodutos('Mussarela sadia 300g', '7.80'),
cadastroprodutos('Peito de peru seara 300g', '10.90'),  
cadastroprodutos('Presunto sadia 300g', '9.00'), 
cadastroprodutos('Hamburguer de soja', '15.00'), 
cadastroprodutos('Farinha de tapioca', '6.00'), 
cadastroprodutos('Leite em po', '7.50'), 
cadastroprodutos('Sal', '5.95'), 
cadastroprodutos('Iorgute grego', '3.50'), 
cadastroprodutos('Margarina', '3.00'), 
cadastroprodutos('Pao de forma', '5.00'), 
cadastroprodutos('Biscoito oreo', '6.50'), 
cadastroprodutos('Maça', '1.50'), 
cadastroprodutos('Banana', '1.00'), 
cadastroprodutos('Creme de leite', '4.50'), 
cadastroprodutos('Leite condensado', '5.00'), 
cadastroprodutos('Leite', '3.65'), 
cadastroprodutos('Nutela', '10.00'), 
cadastroprodutos('Gotas de chocolate', '4.25'), 
cadastroprodutos('Confete', '2.50'), 
cadastroprodutos('Achocolatado', '5.90'), 
cadastroprodutos('Ovo de pascoa Ferrero Rocher', '70.00'), 
cadastroprodutos('Açucar', '8.00'), 
cadastroprodutos('Azeite', '7.00'), 
cadastroprodutos('Oleo de soja', '8.25'), 
cadastroprodutos('Miojo', '1.50'), 
cadastroprodutos('Sucrilhos', '7.80'), 
cadastroprodutos('Amora', '1.00'), 
cadastroprodutos('Cerveja Brahma', '4.00'), 
cadastroprodutos('Skol beats GT', '5.00'), 
cadastroprodutos('Coca cola 1L', '6.50'),
cadastroprodutos('Brownie 80g', '5.50')

adicionar_produto= input("Gostaria de adicionar algum produto? (Sim ou Nao): ")
while adicionar_produto in ("Sim, s, SIM, sim"):
    cadastroprodutos(input("Insira o nome do produto: "), input("Insira o valor do produto: "))
    adicionar_produto= input("Gostaria de adicionar algum produto? (Sim ou Nao)")
    
else:
    pass


#Extração dos itens do supermercado (MONTANDO A LISTA DE COMPRAS)
lista_compras=[]
def escolherprodutos(item):
    for produtos in menu_supermercado:
        if produtos[0]== item:
            lista_compras.append(produtos)
            return lista_compras
             
        else:
            pass
        
print("Escreva 'Pare' quando terminar suas compras.")     
escolherprodutos(input("Insira um produto:"))

for produtos in lista_compras:
    if lista_compras != "Pare":
        escolherprodutos(input("Insira um produto:"))
    
    else:
        pass
print(lista_compras)
time.sleep(0.5)

#CONFIRMAÇAO DE COMPRA (SE QUER ADICIONAR OU REMOVER ALGUM PRODUTO)

confirmaçao_da_compra= input("Seus itens estao corretos?(Sim ou Nao)")
if confirmaçao_da_compra in ("Sim","sim","s","SIM"):
    print("Otimo, vamos para o proximo passo")
    pass
elif confirmaçao_da_compra in ("Nao", "nao","n","NAO","Não", "não"):
    print("Gostaria de remover um produto ou adicionar um produto?")
    resposta= input("Remover ou Adicionar?:")
    if resposta == "Remover":
        print(lista_compras)
        remover_item= input("Qual item gostaria de remover?:")
        for p in lista_compras:
            if p[0]== remover_item:
                lista_compras.remove(p)
                print(lista_compras)
                cf_remover= input("Gostaria de remover mais algum item? (Sim ou Nao)")
                while cf_remover in ("Sim","sim","s","SIM"):
                    remover_item= input("Qual item gostaria de remover?:")
                    for p in lista_compras:
                        if p[0]== remover_item:
                            lista_compras.remove(p)
                            print(lista_compras)
                            cf_remover= input("Gostaria de remover mais algum item? (Sim ou Nao)") 
                if cf_remover in ("Nao", "nao","n","NAO","Não", "não"):
                    break

    elif resposta== "Adicionar":       
        print(lista_compras)
        adicionar_item= input("Qual item gostaria de adicionar?:")
        for p in menu_supermercado:
            if p[0]== adicionar_item:
                lista_compras.append(p)
                print(lista_compras)
                cf_adicionar= input("Gostaria de adicionar mais algum item?(Sim ou nao)")
                while cf_adicionar in ("Sim","sim","s","SIM"):
                    adicionar_item= input("Qual item gostaria de adicionar?:")
                    for p in menu_supermercado:
                        if p[0]== adicionar_item:
                            lista_compras.append(p)
                            print(lista_compras)
                            cf_adicionar= input("Gostaria de adicionar mais algum item?(Sim ou Nao)")
                if cf_adicionar in ("Nao", "nao","n","NAO","Não", "não"):
                    break


#QUANTIDADE DE PRODUTOS DA LISTA DE COMPRAS + Valor total a ser pago
total_compra=0
for compra in lista_compras:
    produto= compra[0]
    valor= compra[1]
    Quantidade= input(f"Insira a quantidade do item {produto} ")
    novo_valor = float(Quantidade) * float(valor)
    total_compra += novo_valor
print(f"Sua compra deu:R${total_compra}")


time.sleep(0.5)

#FORMA DE PAGAMENTO
                
def formadepagamento(forma):
    if forma== "Cartao de debito":
        confirmaçao_compra= input(f"Podemos efetuar a sua compra no valor de R${total_compra}?(Sim ou Nao):")
        if confirmaçao_compra in ("Sim","sim","s","SIM"):
            print("Obrigado pela preferencia, volte sempre!")
        else:
            cf_debito= input("Gostaria de escolher uma nova forma de pagamento?(Sim ou Nao)")
            if cf_debito in ("Sim","sim","s","SIM"):
                formadepagamento(input("Insira uma forma de pagamento:"))
            else:
                obr_debito= input("Gostaria de desistir das compras ou usar o debito como forma de pagamento?(Desistir ou Debito):")
                if obr_debito == "Debito":
                    print("Obrigado pela preferencia, volte sempre!")
                else:
                    pass
              
    elif forma == "Dinheiro":
        nota= input("Informe o valor para efetuarmos a compra:")
        nota_v= float(nota)
        while nota_v < total_compra:
            print("Valor insuficiente, preencha um novo valor")
            nota= input("Informe o valor para efetuarmos a compra:")
            nota_v= float(nota)
        if nota_v == total_compra:
            print("Obrigado pela preferencia, volte sempre!")
        elif nota_v > total_compra:
                troco= nota_v - total_compra
                print(f"Seu troco é:R${troco}, Obrigado pela preferencia, volte sempre!")
        
    elif forma == "Cartao de credito":
        novo_valor= total_compra *1.1
        print(f"Seu novo valor é: {novo_valor}")
        confirmaçao_credito= input("De acordo com o seu novo valor, podemos confirmar a compra? (Sim ou Nao)")
        if confirmaçao_credito in ("Sim","sim","s","SIM"):
            dividir= float(input("Gostaria de dividir quantas vezes?:"))
            valor_parcela= novo_valor/dividir
            print(f"O valor das parcelas são de R${valor_parcela}")
            print("Obrigado pela preferencia, volte sempre!")  
        else:
            cf_credito= input("Gostaria de escolher uma nova forma de pagamento?(Sim ou Nao)")
            if cf_credito in ("Sim","sim","s","SIM"):
                formadepagamento(input("Insira uma forma de pagamento:"))
            else:
                obr_credito= input("Gostaria de desistir das compras ou usar o credito como forma de pagamento?(Desistir ou Credito)")
                if obr_credito == "Credito":
                    dividir= float(input("Gostaria de dividir quantas vezes?:"))
                    valor_parcela= novo_valor/dividir
                    print(f"O valor das percelas sao de R${valor_parcela}")
                    print("Obrigado pela preferencia, volte sempre!")
                else:
                    pass
    else:
        print("Forma de pagamento nao reconhecida, tente novamente")
        formadepagamento(input("Insira uma forma de pagamento:"))

print("Formas de pagamento: Cartao de credito, Cartao de debito, Dinheiro. ")
print("Cartao de credito : Acrescimo de 10% sobre o valor total da compra.")


formadepagamento(input("Insira uma forma de pagamento:")) 