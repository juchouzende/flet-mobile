import flet as ft

def main(page: ft.Page):
    # Título que aparece na barra da janela/aba
    page.title = "Cartão de apresentação"

    # Define o tamanho da janela (largura e altura em pixels)
    page.window.width = 320
    page.window.height = 600

    # Cor de fundo da página: roxo escuro
    page.bgcolor = "#2B1B3D"

    # Centraliza os controles no eixo horizontal da página
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Padding vertical de 60px (topo e base)
    page.padding = ft.Padding(top=60, bottom=60, left=0, right=0)

    # Adiciona os elementos visuais à página
    page.add(
        # Nome em destaque: tamanho maior, negrito e cor rosa clara
        ft.Text(
            "Julia Meirelles",
            size=28,
            weight=ft.FontWeight.BOLD,
            color="#E26FFF",
            text_align=ft.TextAlign.CENTER,  # centraliza o texto internamente
        ),
        # Subtítulo/descrição: tamanho menor, cor lilás suave
        ft.Text(
            "Estudante de programação mobile",
            size=14,
            color="#D9C4E8",
            text_align=ft.TextAlign.CENTER,  # centraliza o texto internamente
        ),
    )

# Inicia a aplicação, chamando a função main() como ponto de entrada
ft.run(main)