import tkinter as tk
from tkinter import messagebox

def montar_computador():
    def exibir_recomendacao():
        try:
            # Obter valores das respostas
            orcamento = float(var_orcamento.get())
            uso = var_uso.get()
            area = var_area.get()

            # Definir as peças com base nas respostas
            if orcamento < 1000:
                processador = "Intel Core i3 ou equivalente"
                placa_mae = "Placa-mãe básica"
                memoria_ram = "8 GB de memória RAM (2x4GB)"
                armazenamento = "SSD de 240GB"
                fonte = "Fonte de alimentação de 400W"
                gabinete = "Gabinete básico"
                placa_video = "Placa de vídeo integrada"
            elif orcamento < 1500:
                processador = "Intel Core i5 ou equivalente"
                placa_mae = "Placa-mãe intermediária"
                memoria_ram = "16 GB de memória RAM (2x8GB)"
                armazenamento = "SSD de 480GB"
                fonte = "Fonte de alimentação de 500W"
                gabinete = "Gabinete intermediário"
                placa_video = "Placa de vídeo dedicada de entrada"
            elif orcamento < 2500:
                processador = "Intel Core i7 ou equivalente"
                placa_mae = "Placa-mãe intermediária ou avançada"
                memoria_ram = "32 GB de memória RAM (2x16GB)"
                armazenamento = "SSD de 1 TB + HD de 2 TB"
                fonte = "Fonte de alimentação de 600W"
                gabinete = "Gabinete avançado com boa refrigeração"
                placa_video = "Placa de vídeo dedicada de médio desempenho"
            elif orcamento < 5000:
                processador = "Intel Core i9 ou equivalente"
                placa_mae = "Placa-mãe avançada"
                memoria_ram = "64 GB de memória RAM (4x16GB)"
                armazenamento = "SSD de 1 TB + HD de 4 TB"
                fonte = "Fonte de alimentação de 750W"
                gabinete = "Gabinete premium com excelente refrigeração"
                placa_video = "Placa de vídeo dedicada de alto desempenho"
            else:
                processador = "Intel Core i9-10900K ou equivalente"
                placa_mae = "Placa-mãe compatível com o processador"
                memoria_ram = "128 GB de memória RAM (4x32GB)"
                armazenamento = "SSD de 2 TB + HD de 8 TB"
                fonte = "Fonte de alimentação de 1000W"
                gabinete = "Gabinete de alto desempenho com recursos avançados de refrigeração e personalização"
                placa_video = "Placa de vídeo de alto desempenho para aplicações profissionais"

            # Exibir as peças recomendadas na mesma janela
            resposta = "Recomendação:\n\n" \
                       f"Processador: {processador}\n" \
                       f"Placa-mãe: {placa_mae}\n" \
                       f"Memória RAM: {memoria_ram}\n" \
                       f"Armazenamento: {armazenamento}\n" \
                       f"Fonte de alimentação: {fonte}\n" \
                       f"Gabinete: {gabinete}\n" \
                       f"Placa de vídeo: {placa_video}"

            label_resposta.config(text=resposta)

        except ValueError:
            messagebox.showerror("Erro", "Por favor, selecione uma opção para o orçamento.")

    def reiniciar():
        # Limpar as respostas
        var_orcamento.set(None)
        var_uso.set(None)
        var_area.set("")

        label_resposta.config(text="")

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

    var_orcamento = tk.StringVar()
    opcoes_orcamento = [
        ("Até R$ 1000", 1000),
        ("R$ 1000 - R$ 1500", 1500),
        ("R$ 1500 - R$ 2500", 2500),
        ("R$ 2500 - R$ 5000", 5000),
        ("Mais de R$ 5000", 10000)
    ]
    for texto, valor in opcoes_orcamento:
        rb_orcamento = tk.Radiobutton(janela, text=texto, variable=var_orcamento, value=valor)
        rb_orcamento.pack(anchor="w")

    label_uso = tk.Label(janela, text="Qual será o uso principal do computador?")
    label_uso.pack()

    var_uso = tk.StringVar()
    opcoes_uso = [
        ("Uso doméstico", "Doméstico"),
        ("Uso para jogos", "Jogos"),
        ("Uso profissional (edição de vídeo, design gráfico, etc.)", "Profissional"),
        ("Uso para programação e desenvolvimento", "Programação")
    ]
    for texto, valor in opcoes_uso:
        rb_uso = tk.Radiobutton(janela, text=texto, variable=var_uso, value=valor)
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

montar_computador()
