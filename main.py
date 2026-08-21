from collections import defaultdict
from datetime import datetime

# Listas de dados
lista_carros = ["Fiat Mobi", "Fiat Argo", "Fiat Pulse", "Fiat Cronos", "Fiat Strada", "Fiat Fastback", "Fiat Fiorino", "Fiat Toro", "Fiat Titano", "Chevrolet S10", "Chevrolet Silverado", "Chevrolet Equinox", "Chevrolet Captiva", "Chevrolet Spark", "Chevrolet Montana", "Chevrolet Tracker", "Chevrolet Spin", "Chevrolet Onix", "Chevrolet Trailblazer", "Toyota Yaris", "Toyota Yaris Cross", "Toyota Corolla", "Toyota Corolla Cross", "Toyota Hilux", "Toyota Rav4", "Toyota Gr Yaris", "Toyota Gr Corolla", "Toyota Hilux Sw4", "Hyundai Hb20", "Hyundai Hb20s", "Hyundai Creta", "Hyundai Tucson", "Hyundai Palisade", "Hyundai Kona", "Volkswagen Polo", "Volkswagen Tera", "Volkswagen Saveiro", "Volkswagen Virtus", "Volkswagen Nivus", "Volkswagen T-Cross", "Volkswagen Jetta", "Volkswagen Tiguan", "Volkswagen Amarok", "Jeep Renegade", "Jeep Compass", "Jeep Commander", "Jeep Gladiator", "Jeep Wrangler", "Renault Kwid", "Renault Logan", "Renault Kwid E-Tech", "Renault Duster", "Honda City", "Honda Wr-V", "Honda Hr-V", "Honda Civic", "Honda Accord", "Honda Crv", "Nissan Kicks", "Nissan Versa", "Nissan Sentra", "Nissan Frontier", "Peugeot 208", "Peugeot 2008", "Citroen C3", "Citroen Basalt", "Ford Maverick", "Ford Territory", "Ford Ranger", "Ford F-150", "Ford Mustang"]
lista_bancos = ["Banco do Brasil", "Bradesco", "Caixa Econômica", "Itaú", "Santander"]
min_parcelas = 20
max_parcelas = 120
# Dicionarios de preços e juros
precos = {
    "Fiat Mobi": 85990,
    "Fiat Argo": 111990,
    "Fiat Pulse": 162490,
    "Fiat Cronos": 124990,
    "Fiat Strada": 151990,
    "Fiat Fastback": 183990,
    "Fiat Fiorino": 130990,
    "Fiat Toro": 235490,
    "Fiat Titano": 285990,
    "Chevrolet S10": 348790,
    "Chevrolet Silverado": 483990,
    "Chevrolet Equinox": 349990,
    "Chevrolet Captiva": 291190,
    "Chevrolet Spark": 154990,
    "Chevrolet Montana": 171390,
    "Chevrolet Tracker": 119900,
    "Chevrolet Spin": 165590,
    "Chevrolet Onix": 139390,
    "Chevrolet Trailblazer": 422590,
    "Toyota Yaris": 135090,
    "Toyota Yaris Cross": 189990,
    "Toyota Corolla": 206990,
    "Toyota Corolla Cross": 222690,
    "Toyota Hilux": 357890,
    "Toyota Rav4": 349290,
    "Toyota Gr Yaris": 354990,
    "Toyota Gr Corolla": 399990,
    "Toyota Hilux Sw4": 475990,
    "Hyundai Hb20": 132490,
    "Hyundai Hb20s": 138890,
    "Hyundai Creta": 206990,
    "Hyundai Tucson": 199490,
    "Hyundai Palisade": 479990,
    "Hyundai Kona": 239990,
    "Volkswagen Polo": 138690,
    "Volkswagen Tera": 146190,
    "Volkswagen Saveiro": 134190,
    "Volkswagen Virtus": 176690,
    "Volkswagen Nivus": 189690,
    "Volkswagen T-Cross": 203490,
    "Volkswagen Jetta": 278490,
    "Volkswagen Tiguan": 299990,
    "Volkswagen Amarok": 399890,
    "Jeep Renegade": 189490,
    "Jeep Compass": 278990,
    "Jeep Commander": 329990,
    "Jeep Gladiator": 529990,
    "Jeep Wrangler": 529990,
    "Renault Kwid": 89090,
    "Renault Logan": 101000,
    "Renault Kwid E-Tech": 99990,
    "Renault Duster": 171990,
    "Honda City": 155300,
    "Honda Wr-V": 155300,
    "Honda Hr-V": 214000,
    "Honda Civic": 430500,
    "Honda Accord": 333000,
    "Honda Crv": 353500,
    "Nissan Kicks": 199000,
    "Nissan Versa": 146490,
    "Nissan Sentra": 198790,
    "Nissan Frontier": 317990,
    "Peugeot 208": 138990,
    "Peugeot 2008": 184990,
    "Citroen C3": 112590,
    "Citroen Basalt": 129890,
    "Ford Maverick": 239900,
    "Ford Territory": 219900,
    "Ford Ranger": 499000,
    "Ford F-150": 580000,
    "Ford Mustang": 649000
}
juros = {
    "Banco do Brasil": 0.0207,
    "Bradesco": 0.0174,
    "Caixa Econômica": 0.0197,
    "Itaú": 0.0212,
    "Santander": 0.0190
}

# Organiza os carros por marca
separados = defaultdict(list)
for carro in lista_carros:
    marca = carro.split()[0]
    separados[marca].append(carro)

# 1. Seleção da Marca
selecao = input("Selecione uma marca (Fiat, Ford, Toyota, Chevrolet, Hyundai, Volkswagen, Jeep, Renault, Honda, Nissan, Peugeot, Citroen): ").strip()

modelos = separados.get(selecao)
if modelos:
    print(f"Modelos da {selecao}: {', '.join(modelos)}")

    # 2. Seleção do Modelo
    modelo_escolhido = input("Escolha o modelo para financiar: ").strip()
    if modelo_escolhido in modelos:
        print("Modelo selecionado com sucesso!")

        valor = precos[modelo_escolhido]
        print(f"Preço do carro: R$ {valor:.2f}")

        # 3. Seleção do Banco
        print(f"Bancos disponíveis: {lista_bancos}")
        banco = input("Escolha a instituição financeira: ").strip()

        if banco in lista_bancos:
            print(f"Banco escolhido: {banco}")
            print(f"Taxa de juros do banco:{juros[banco]*100:.2f}%")

            # 4. Seleção de Parcelas (Validação entre 20 e 120)
            parcelas = int(input("Escolha o número de parcelas (20 até 120): "))
            if min_parcelas <= parcelas <= max_parcelas:

                # Data atual
                data_atual = datetime.now()

                # Calcula mês e ano final
                mes_final = data_atual.month + parcelas
                ano_final = data_atual.year + (mes_final - 1) // 12
                mes_final = ((mes_final - 1) % 12) + 1

                print(f"Você terminará de pagar em: {mes_final:02d}/{ano_final}")

                # 5. Escolha da forma de financiamento
                financiamento = input("Escolha a forma de financiamento (Price ou Sac): ").strip()
                if financiamento == "Price":
                  print("Financiamento Price selecionado.")
                  print(f"Financiamento Price de {modelo_escolhido} em {parcelas}x pelo {banco} aprovado!")

                  # 6. Cálculos price
                  parcela_valor = valor*juros[banco] / (1 - (1 + juros[banco]) ** (-parcelas))
                  print(f"Valor de cada parcela: R$ {parcela_valor:.2f}")
                  total = parcela_valor * parcelas
                  print(f"Valor total a ser pago: R$ {total:.2f}")
                  total_juros = total - valor
                  print(f"Valor total de juros: R$ {total_juros:.2f}")

                  print("\n===== RESUMO DO FINANCIAMENTO =====")
                  print(f"Carro escolhido: {modelo_escolhido}")
                  print(f"Preço do carro: R$ {valor:.2f}")
                  print(f"Banco: {banco}")
                  print(f"Quantidade de parcelas: {parcelas}x")
                  print(f"Valor total pago: R$ {total:.2f}")
                  print(f"Total de juros pagos: R$ {total_juros:.2f}")
                  print(f"Última parcela: {mes_final:02d}/{ano_final}")

                elif financiamento == "Sac":
                  print("Financiamento Sac selecionado.")
                  print(f"Financiamento Sac de {modelo_escolhido} em {parcelas}x pelo {banco} aprovado!")

                  # 7. Cálculos Sac
                  saldo_devedor = valor
                  prestaçoes = []
                  amortizaçao = valor/parcelas
                  for i in range(parcelas):
                    taxa_aplicada = juros[banco] * saldo_devedor
                    prestaçoes.append(amortizaçao + taxa_aplicada)
                    saldo_devedor = saldo_devedor - prestaçoes[i]

                    if(i == 0):
                      print(f"O valor da primeira parcela será: R${prestaçoes[i]:.2f}")
                    if(i == parcelas - 1):
                      print(f"O valor da última parcela será: R${prestaçoes[i]:.2f}")
                      total = sum(prestaçoes)
                      print(f"Valor total a ser pago: R$ {total:.2f}")
                      total_juros = total - valor
                      print(f"Valor total de juros: R$ {total_juros:.2f}")

                      print("\n===== RESUMO DO FINANCIAMENTO =====")
                      print(f"Carro escolhido: {modelo_escolhido}")
                      print(f"Preço do carro: R$ {valor:.2f}")
                      print(f"Banco: {banco}")
                      print(f"Quantidade de parcelas: {parcelas}x")
                      print(f"Valor da primeira parcela será: R${prestaçoes[0]:.2f}")
                      print(f"Valor da última parcela será: R${prestaçoes[i]:.2f}")
                      print(f"Valor total pago: R$ {total:.2f}")
                      print(f"Total de juros pagos: R$ {total_juros:.2f}")
                      print(f"Última parcela: {mes_final:02d}/{ano_final}")

                else:
                    print("Forma de financiamento inválida.")
            else:
                print(f"Número de parcelas inválido! Escolha entre {min_parcelas} e {max_parcelas}.")
        else:
            print("Banco não encontrado.")
    else:
        print("O modelo não consta no banco de dados desta marca.")
else:
    print("Marca não encontrada.")