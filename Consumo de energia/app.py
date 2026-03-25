#Introduçao (Saudação)

print("💠 BEM-VINDO À CALCULADORA DE CONSUMO ELÉTRICO INTELIGENTE.💠")
print("ESTOU PRONTO PARA AJUDAR VOCÊ A ENTENDER SEUS GASTOS E ECONOMIZAR ENERGIA.")
print("-" * 90)

#Usuario insere os dados

eletrodmestico=input("💡Informe o aparelho utilizado: ")
potencia=int(input("⚡Informe a potência do seu aparelho em Watts (W): "))
tempo=float(input("⏳ Informe o tempo médio de uso diário em horas (Utlize ponto (.) em vez de virgula (,)): "))
consumoM=(potencia*tempo*30)/1000
valor=consumoM*0.68
print("="*90)

#Resultado na tela do usuario

print("NOME DO APARELHO:", eletrodmestico)

if potencia<1000:
    print("🟢 Esse aparelho consome pouca energia.✅")


if potencia>=1000 and potencia<3000:
    print("🟡 Esse aparelho consome uma quantia consideravel de energia.⚠️")

if potencia>=3000:
    print("🔴 Esse aparelho consome muita energia, use com cautela!.🚨")

#Usuario

print("⚡",consumoM, "kWh/mês.")
print(f"💵 R$ {valor:.2f} serão gastos por mês." \
"")
