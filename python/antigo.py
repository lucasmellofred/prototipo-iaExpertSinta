import tkinter as tk
from tkinter import messagebox

def exibir_recomendacao():
    try:
        # Obter valores das respostas
        orçamento = float(entry_orcamento.get())
        uso = var_uso.get()
        area = var_area.get()

        # Definir as peças com base nas respostas
        if orçamento < 1000:
            messagebox.showerror("Erro", "O orçamento mínimo é de R$1000.")
            return

        # Lista de peças necessárias de acordo com as respostas
        if orçamento <= 1000:
            processador = "Intel Core i3-9100F ou equivalente"
            placa_mae = "Placa-mãe compatível com o processador"
            memoria_ram = "8 GB de memória RAM (2x4GB)"
            armazenamento = "HD de 1 TB"
            fonte = "Fonte de alimentação de 400W"
            gabinete = "Gabinete básico com refrigeração adequada"
            perifericos = "Teclado, mouse e monitor básicos"

            if area == "design" or uso == "design":
                placa_video = "Placa de vídeo dedicada para design gráfico"
            else:
                placa_video = "Placa de vídeo integrada ao processador"

        elif orçamento <= 2000:
            processador = "AMD Ryzen 5 2600 ou equivalente"
            placa_mae = "Placa-mãe compatível com o processador"
            memoria_ram = "16 GB de memória RAM (2x8GB)"
            armazenamento = "SSD de 240 GB + HD de 1 TB"
            fonte = "Fonte de alimentação de 500W"
            gabinete = "Gabinete intermediário com boa circulação de ar"
            perifericos = "Teclado, mouse e monitor intermediários"

            if area == "design" or uso == "design":
                placa_video = "Placa de vídeo dedicada para design gráfico"
            else:
                placa_video = "Placa de vídeo integrada ao processador"

        elif orçamento <= 4000:
            processador = "Intel Core i7-9700K ou equivalente"
            placa_mae = "Placa-mãe compatível com o processador"
            memoria_ram = "32 GB de memória RAM (2x16GB)"
            armazenamento = "SSD de 480 GB + HD de 2 TB"
            fonte = "Fonte de alimentação de 600W"
            gabinete = "Gabinete avançado com excelente fluxo de ar e opções de expansão"
            perifericos = "Teclado, mouse e monitor avançados"

            if area == "design" or uso == "design":
                placa_video = "Placa de vídeo dedicada para design gráfico"
            elif area == "engenharia" or uso == "engenharia":
                placa_video = "Placa de vídeo dedicada para modelagem 3D"
            else:
                placa_video = "Placa de vídeo dedicada para jogos"

        elif orçamento <= 8000:
            processador = "AMD Ryzen 9 5900X ou equivalente"
            placa_mae = "Placa-mãe compatível com o processador"
            memoria_ram = "64 GB de memória RAM (4x16GB)"
            armazenamento = "SSD de 1 TB + HD de 4 TB"
            fonte = "Fonte de alimentação de 750W"
            gabinete = "Gabinete premium com excelente refrigeração e recursos de personalização"
            perifericos = "Teclado, mouse e monitor avançados"

            if area == "design" or uso == "design":
                placa_video = "Placa de vídeo dedicada de alto desempenho para design gráfico"
            elif area == "engenharia" or uso == "engenharia":
                placa_video = "Placa de vídeo dedicada de alto desempenho para modelagem 3D"
            elif area == "jogos" or uso == "jogos":
                placa_video = "Placa de vídeo dedicada de alto desempenho para jogos"
            else:
                placa_video = "Placa de vídeo dedicada para uso geral"

        else:
            processador = "Intel Core i9-10900K ou equivalente"
            placa_mae = "Placa-mãe compatível com o processador"
            memoria_ram = "128 GB de memória RAM (4x32GB)"
            armazenamento = "SSD de 2 TB + HD de 8 TB"
            fonte = "Fonte de alimentação de 1000W"
            gabinete = "Gabinete de alto desempenho com recursos avançados de refrigeração e personalização"
            perifericos = "Teclado, mouse e monitor premium"

            if area == "design" or uso == "design":
                placa_video = "Placa de vídeo dedicada profissional para design gráfico"
            elif area == "engenharia" or uso == "engenharia":
                placa_video = "Placa de vídeo dedicada profissional para modelagem 3D"
            elif area == "jogos" or uso == "jogos":
                placa_video = "Placa de vídeo dedicada de alto desempenho para jogos"
            else:
                placa_video = "Placa de vídeo dedicada para uso geral"

        # Exibir as peças recomendadas na mesma janela
        resposta = "Recomendação:\n\n" \
                   f"Processador: {processador}\n" \
                   f"Placa-mãe: {placa_mae}\n" \
                   f"Memória RAM: {memoria_ram}\n" \
                   f"Armazenamento: {armazenamento}\n" \
                   f"Fonte de alimentação: {fonte}\n" \
                   f"Gabinete: {gabinete}\n" \
                   f"Placa de vídeo: {placa_video}\n" \
                   f"{perifericos}"

        label_resposta.config(text=resposta)

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um valor numérico válido para o orçamento.")

def reiniciar():
    # Limpar as respostas
    entry_orcamento.delete(0, tk.END)
    var_uso.set("")
    var_area.set("")

janela = tk.Tk()
janela.title("Montagem de Computador")

# Definir tamanho fixo para a janela
janela.geometry("500x700")

# Centralizar a janela na tela do monitor
janela.update_idletasks()
width = janela.winfo_width()
height = janela.winfo_height()
x = (janela.winfo_screenwidth() // 2) - (width // 2)
y = (janela.winfo_screenheight() // 2) - (height // 2)
janela.geometry(f"{width}x{height}+{x}+{y}")

# Adicionar margem interna
janela.configure(padx=20, pady=20)

label_orcamento = tk.Label(janela, text="Qual é o seu orçamento?")
label_orcamento.pack()

entry_orcamento = tk.Entry(janela)
entry_orcamento.pack()

label_uso = tk.Label(janela, text="Qual será o uso principal do computador?")
label_uso.pack()

var_uso = tk.StringVar()
opcoes_uso = [
    "Uso doméstico",
    "Uso para jogos",
    "Uso profissional (edição de vídeo, design gráfico, etc.)",
    "Uso para programação e desenvolvimento"
]

entry_uso = tk.OptionMenu(janela, var_uso, *opcoes_uso)
entry_uso.pack()

for opcao in opcoes_uso:
    rb_uso = tk.Radiobutton(janela, text=opcao, variable=var_uso, value=opcao)
    rb_uso.pack(anchor="w")

label_area = tk.Label(janela, text="Qual é a sua área de atuação? (opcional)")
label_area.pack()

entry_area = tk.Entry(janela)
entry_area.pack()
var_area = tk.StringVar()

botao_confirmar = tk.Button(janela, text="Confirmar", command=exibir_recomendacao)
botao_confirmar.pack()

label_resposta = tk.Label(janela, text="")
label_resposta.pack()

botao_reiniciar = tk.Button(janela, text="Reiniciar", command=reiniciar)
botao_reiniciar.pack(side="bottom")

janela.mainloop()
