import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def montar_computador():
    def exibir_recomendacao():
        try:
            # Obter valores das respostas
            orcamento_texto = combo_orcamento.get()
            if orcamento_texto.startswith("Acima"):
                orcamento = float(orcamento_texto[orcamento_texto.find("R$")+2:])
            else:
                orcamento = float(orcamento_texto[orcamento_texto.find("R$")+2:orcamento_texto.find(" -")])

            uso = combo_uso.get()
            area = combo_area.get()

            # Definir as peças com base nas respostas
            if orcamento == 2000: #Opção acima de R$ 2000
                processador = "Ryzen 5 4600G"
                placa_mae = "Placa-mãe A520"
                memoria_ram = "8 GB de memória RAM (2x4GB)"
                armazenamento = "SSD M.2 NVMe 512GB"
                fonte = "Fonte de alimentação de 450W"
                placa_video = "Placa de vídeo é integrada nesse processador"
            elif orcamento < 2500: #Opção R$ 2001 - R$ 2500
                processador = "Intel Core i3 10100F "
                placa_mae = "Placa-mãe A320"
                memoria_ram = "Memória RAM 2x8GB DDR4 @3200MHz"
                armazenamento = "SSD M.2 NVMe 512GB"
                fonte = "Fonte de 550W"
                placa_video = "GTX 1650 ou RX 6400"
            elif orcamento < 3000: #Opcão R$ 2500 - R$ 3000
                processador = "Ryzen 5 5500"
                placa_mae = "Placa-mãe intermediária ou avançada"
                memoria_ram = "32 GB de memória RAM (2x16GB)"
                armazenamento = "SSD NVMe 1TB Kingston NV2"
                fonte = "Fonte de alimentação de 600W"
                placa_video = "RX 6600 ou RTX 2060 ou  RTX 3050"
            elif orcamento < 4000: #Opção R$ 3001 - R$ 4000
                processador = "Ryzen 5 5500"
                placa_mae = "Placa-mãe H610 "
                memoria_ram = "Memória RAM 2x8GB DDR4 @3200MHz"
                armazenamento = "SSD NVMe 1TB Kingston NV2"
                fonte = "Fonte de 550W"
                placa_video = "RX 6650 XT ou RTX 3060 12GB"
            elif orcamento < 4700: #Opção R$ 4001 - R$ 4700
                processador = "Intel Core i5 13400F"
                placa_mae = "Placa-mãe avançada"
                memoria_ram = "64 GB de memória RAM (4x16GB)"
                armazenamento = "SSD de 1 TB + HD de 4 TB"
                fonte = "Fonte de alimentação de 750W"
                placa_video = "RX 6600"
            elif orcamento < 5000: #Opção R$ 4701 - R$ 5000
                processador = "Ryzen 5 5600 ou Intel Core i5 12400F"
                placa_mae = "Placa-mãe A520"
                memoria_ram = "Memória RAM: 2x 8GB DDR4 @3200MHz "
                armazenamento = "SSD M.2 NVMe 512GB"
                fonte = "Fonte de alimentação de 550W"
                placa_video = " RX 6700 XT ou RTX 3060 Ti"
            elif orcamento < 6000: #Opção R$ 5001 - R$ 6000
                processador = "Ryzen 5 7600 ou Intel Core i5 13600KF"
                placa_mae = "Placa-mãe H610"
                memoria_ram = "Memória RAM 2x8GB DDR4 @3200MHz"
                armazenamento = "SSD de 2 TB + HD de 8 TB"
                fonte = "Fonte de alimentação de 7500W"
                placa_video = "RX 7900 XT ou RTX 4070 TI"
            elif orcamento < 10000: #Opção R$ 6001 - R$ 10000
                processador = "Ryzen 5 7600 ou Intel Core i5 13600KF"
                placa_mae = "Placa-mãe B550"
                memoria_ram = "Memória RAM 2x 16GB DDR4 @3200MHz ou DDR5 @5200MHz"
                armazenamento = "SSD NVMe 1TB Kingston NV2"
                fonte = "Fonte de alimentação de 750W"
                placa_video = "RX 7900 XT ou RTX 4070 TI"

            # Verificar uso selecionado para ajustar recomendações
            uso = combo_uso.get()
            if uso == "Doméstico":
                if orcamento == 2000:
                    memoria_ram = "16 GB de memória RAM (2x8GB)"
                    armazenamento = "SSD de 480GB"
            elif uso == "Jogos":
                if orcamento > 2500:
                    processador = "Intel Core i9 ou equivalente"
                    placa_mae = "Placa-mãe avançada"
                    memoria_ram = "32 GB de memória RAM (2x16GB)"
                    armazenamento = "SSD de 1 TB + HD de 2 TB"
                    fonte = "Fonte de alimentação de 600W"
                    placa_video = "Placa de vídeo dedicada de médio desempenho"
            elif uso == "Profissional":
                if orcamento > 5000:
                    processador = "Intel Core i9-10900K ou equivalente"
                    placa_mae = "Placa-mãe compatível com o processador"
                    memoria_ram = "128 GB de memória RAM (4x32GB)"
                    armazenamento = "SSD de 2 TB + HD de 8 TB"
                    fonte = "Fonte de alimentação de 1000W"
                    placa_video = "Placa de vídeo de alto desempenho para aplicações profissionais"

            # Verificar área selecionada para ajustar recomendações
            area = combo_area.get()
            if area == "Design, Fotografia e Videomaker":
                if orcamento > 2000:
                    placa_mae = "Placa-mãe com suporte a cores RGB"
            elif area == "Arquitetura e Engenharias":
                if orcamento > 3000:
                    memoria_ram = "32 GB de memória RAM (4x8GB)"
                    armazenamento = "SSD de 1 TB + HD de 4 TB"
                    placa_video = "Placa de vídeo dedicada de médio desempenho"

            # Exibir as peças recomendadas na mesma janela
            resposta = "Recomendação:\n\n" \
                       f"Processador: {processador}\n" \
                       f"Placa-mãe: {placa_mae}\n" \
                       f"Memória RAM: {memoria_ram}\n" \
                       f"Armazenamento: {armazenamento}\n" \
                       f"Fonte de alimentação: {fonte}\n" \
                       f"Placa de vídeo: {placa_video}"

            label_resposta.config(text=resposta)

        except ValueError:
            messagebox.showerror("Erro", "Por favor, selecione uma opção para o orçamento.")

    def reiniciar():
        # Limpar as respostas
        combo_orcamento.set("")
        combo_uso.set("")
        combo_area.set("")

        label_resposta.config(text="")

    janela = tk.Tk()
    janela.title("Montagem de Computador")

    # Definir tamanho fixo para a janela
    janela.geometry("500x500")

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

    opcoes_orcamento = [
        "Acima de R$ 2000",
        "R$ 2001 - R$ 2500",
        "R$ 2501 - R$ 3000",
        "R$ 3001 - R$ 4000",
        "R$ 4001 - R$ 4700",
        "R$ 4701 - R$ 5000",
        "R$ 5001 - R$ 6000",
        "R$ 6001 - R$ 10000"
    ]

    combo_orcamento = ttk.Combobox(janela, values=opcoes_orcamento)
    combo_orcamento.pack()
    combo_orcamento.configure(width=40)

    label_uso = tk.Label(janela, text="Qual será o uso principal do computador?")
    label_uso.pack()

    opcoes_uso = [
        ("Doméstico"),
        ("Jogos"),
        ("Profissional"),
        ("Programação")
    ]
    combo_uso = ttk.Combobox(janela, values=opcoes_uso)
    combo_uso.pack()
    combo_uso.configure(width=40) 
    
    label_area = tk.Label(janela, text="Qual é a sua área de atuação? (opcional)")
    label_area.pack()    
    opcoes_area = [
        ("Design, Fotografia e Videomaker"),
        ("Arquitetura e Engenharias"),
        ("Odontologia"),
        ("Engenharia"),
        ("Ciências da Computação"),
        ("Marketing e Publicidade"),
        ("Finanças e Contabilidade"),
        ("Ciências Biológicas"),
        ("Medicina e Saúde"),
        ("Educação e Pedagogia"),
        ("Direito"),
        ("Ciências Sociais e Humanas"),
        ("Gestão de Projetos"),
        ("Consultoria"),
        ("Turismo e Hotelaria"),
        ("Comércio e Vendas"),
        ("Logística e Supply Chain"),
        ("Música e Artes Cênicas")
    ]
    combo_area = ttk.Combobox(janela, values=opcoes_area)
    combo_area.pack()
    combo_area.configure(width=40) 
    
    botao_confirmar = tk.Button(janela, text="Confirmar", command=exibir_recomendacao)
    botao_confirmar.pack()

    label_resposta = tk.Label(janela, text="")
    label_resposta.pack()

    botao_reiniciar = tk.Button(janela, text="Reiniciar", command=reiniciar)
    botao_reiniciar.pack(side="bottom")

    janela.mainloop()

montar_computador()
