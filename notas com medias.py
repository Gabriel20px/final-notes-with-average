nota = float(int(input("qual é a sua nota do primeiro bimestre?:  ")))
nota2 = float(int(input("qual foi a sua nota do segundo bimetres?: ")))
nota3 = float(int(input("qual foi a sua nota do terceiro bimestre?: ")))
resultado = ((nota + nota2 + nota3)/3)
if nota >=7:
    print(f"você esta aprovado {resultado:.2f}")
elif 5 <= resultado <= 6.9:
    print(f"você esta em recuperação {resultado:.2f}")
else:
    print(f"você esta reprovado {resultado:.2f}")
