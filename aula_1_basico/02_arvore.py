import flet as ft

def main(page: ft.Page):
    page.title = "Árvore de controles"

    # Define o tamanho da janela
    page.window.width = 320
    page.window.height = 600

    # Cor de fundo da página: verde-azulado 
    page.bgcolor = "#16bA4A"

    # Centralizar elementos
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Padding
    page.padding = ft.Padding(top=60, bottom=60, left=0, right=0)

    # Container principal que representa o cartão visual
    cartao = ft.Container(
        # conteúdo do cartão organizado em coluna
        content=ft.Column(
            horizontal_alignment = ft.CrossAxisAlignment.CENTER,
            controls=[
                # título do cartão
                ft.Text(
                        "Título do cartão",
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        color="#E26FFF",
                ),
                # texto descritivo
                ft.Text("Descrição do cartão", color="#CFEFE9"),

                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.ElevatedButton(
                            "Ação 1",
                            bgcolor="#1FE0C4",
                            color="#0B3D3A"
                        ), # Botão de destaque
                        ft.OutlinedButton("Ação 2") # Segundo botão
                    ]
                ),
            ]
        ),
    padding=16,
    bgcolor="#123C3C",
    border_radius=12,
    )
    # Adiciona o cartão à página
    page.add(cartao)

ft.run(main)