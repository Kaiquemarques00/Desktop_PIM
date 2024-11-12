import flet as ft

def main(page: ft.Page):
    # Sem padding
    container1 = ft.Container(
        content=ft.Text("Sem Padding"),
        width=200,
        height=200,
        bgcolor=ft.colors.GREEN,
        alignment=ft.alignment.center,  # Alinhamento centralizado
    )
    
    # Com padding
    container2 = ft.Container(
        content=ft.Text("Com Padding"),
        width=200,
        height=200,
        bgcolor=ft.colors.BLUE,
        alignment=ft.alignment.center,  # Alinhamento centralizado
        padding=20,  # Adiciona padding de 20 pixels
    )

    page.add(container1, container2)

ft.app(target=main)
