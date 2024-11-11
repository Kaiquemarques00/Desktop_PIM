import flet as ft

def main(page: ft.Page):
    # Definindo controles que expandem
    page.add(
        ft.Container(ft.Text("Expande para preencher"), expand=True),
        ft.Container(ft.Text("50% da largura"), width="50%"),
    )

ft.app(target=main)