#Pedir a distancia da viagem
distancia = float(input("Por favor, digite a distância percorrida: "))

#Pedir o tempo da viagem
tempo = float(input("Por favor, informe o tempo necessário para a viagem: "))

#Dividir a distância pelo tempo
velocidade_media = distancia / tempo

#Exibir o resultado para o usúario
print(f"A velocidade média foi de {velocidade_media:.2f} km/h ")