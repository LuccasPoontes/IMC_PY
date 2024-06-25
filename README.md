# Calculadoras de IMC

Este repositório contém dois projetos de calculadora de IMC (Índice de Massa Corporal) desenvolvidos em Python. Um dos projetos utiliza interação via terminal e o outro possui uma interface gráfica desenvolvida com Tkinter.

## Estrutura do Repositório

- `2.IMC_INTERFACE_TKINTER/`: Contém o código que utiliza a biblioteca Tkinter para criar uma interface gráfica.
- `3.IMC_TERMINAL/`: Contém o código que interage com o usuário via terminal.

## Calculadora de IMC com Interface Gráfica

### Localização do Código

- Diretório: `2.IMC_INTERFACE_TKINTER/`
- Arquivo: `tkinter_valida_imc.py`

### Descrição

Esta versão da calculadora de IMC oferece uma interface gráfica amigável onde os usuários podem inserir seu peso e altura para calcular e exibir seu IMC juntamente com uma classificação de peso.

### Como usar

1. Certifique-se de ter o Python instalado em sua máquina.
2. Instale a biblioteca Tkinter, caso ainda não tenha. Tkinter geralmente vem incluído na instalação padrão do Python.
3. Navegue até o diretório `2.IMC_INTERFACE_TKINTER/`.
4. Execute o arquivo `tkinter_valida_imc.py`.

```bash
cd 2.IMC_INTERFACE_TKINTER
python tkinter_valida_imc.py
```
- Uma janela aparecerá onde você pode inserir seu peso (em kg) e altura (em metros).
- Clique no botão "Calcular IMC" para ver o resultado.

```codigo
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def calcular_imc():
    try:
        peso = float(entrada_peso.get())
        altura = float(entrada_altura.get())
        imc = peso / (altura ** 2)
        if imc < 18.5:
            resultado = f"IMC: {imc:.2f} - Abaixo do peso"
        elif imc < 24.9:
            resultado = f"IMC: {imc:.2f} - Peso normal"
        elif imc < 29.9:
            resultado = f"IMC: {imc:.2f} - Sobrepeso"
        else:
            resultado = f"IMC: {imc:.2f} - Obesidade"
        mensagem['text'] = resultado
    except ValueError:
        messagebox.showerror("Erro de valor", "Por favor, insira valores válidos para peso e altura.")

# Configuração da janela principal
janela = tk.Tk()
janela.title("Calculadora de IMC")

frame = ttk.Frame(janela, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Configuração da grade de redimensionamento
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=2)

# Label e entrada para peso
ttk.Label(frame, text="Peso (kg):").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
entrada_peso = ttk.Entry(frame)
entrada_peso.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=5, pady=5)

# Label e entrada para altura
ttk.Label(frame, text="Altura (m):").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
entrada_altura = ttk.Entry(frame)
entrada_altura.grid(row=1, column=1, sticky=(tk.W, tk.E), padx=5, pady=5)

# Botão para calcular IMC
botao_calcular = ttk.Button(frame, text="Calcular IMC", command=calcular_imc)
botao_calcular.grid(row=2, column=0, columnspan=2, pady=10)

# Label para exibir o resultado
mensagem = ttk.Label(frame, text="")
mensagem.grid(row=3, column=0, columnspan=2, pady=5)

# Inicia o loop principal da interface gráfica
janela.mainloop()
```
# Calculadora de IMC via Terminal
## Localização do Código
- Diretório: 3.IMC_TERMINAL/
- Arquivo: calcular_imc.py
## Descrição
Esta versão da calculadora de IMC permite que os usuários insiram seu peso e altura diretamente no terminal para calcular e exibir seu IMC juntamente com uma classificação de peso.

## Como usar
1. Certifique-se de ter o Python instalado em sua máquina.
2. Navegue até o diretório 3.IMC_TERMINAL/.
3. Execute o arquivo calcular_imc.py.

```Bash
cd 3.IMC_TERMINAL
python calcular_imc.py
```
4. Siga as instruções no terminal para inserir seu peso e altura.
5. O resultado do IMC e sua classificação serão exibidos no terminal.

```Codigo
def calcular_imc():
    try:
        peso = float(input("Digite seu peso (kg): "))
        altura = float(input("Digite sua altura (m): "))
        imc = peso / (altura ** 2)
        if imc < 18.5:
            print(f"IMC: {imc:.2f} - Abaixo do peso")
        elif imc < 24.9:
            print(f"IMC: {imc:.2f} - Peso normal")
        elif imc < 29.9:
            print(f"IMC: {imc:.2f} - Sobrepeso")
        else:
            print(f"IMC: {imc:.2f} - Obesidade")
    except ValueError:
        print("Por favor, insira valores válidos para peso e altura.")

if __name__ == "__main__":
    calcular_imc()
```

## Autor

Este projeto foi desenvolvido por Luccas Pontes. Se você tiver alguma dúvida ou sugestão, sinta-se à vontade para entrar em contato.


## Licença

Esse README.md fornece uma visão geral completa do que o projeto faz, como configurá-lo e usá-lo, além de detalhes sobre o código e autoria. Se precisar de mais alguma coisa ou de ajustes, me avise!

