import flet as ft

class Appbar:

    def __init__(self, page):
        self.page=page

    def appBar(self):

        alerta_logout=ft.AlertDialog(
            modal=True,
            bgcolor="#2A383E",
            title=ft.Text("CONFIRMAR LOGOUT"),
            content=ft.Text("Você realmente deseja fazer Logoff do aplicativo?"),
            actions=[
                ft.TextButton("Sim", on_click=lambda _:self.page.go("/")),
                ft.TextButton("Não", on_click=lambda e:self.page.close(alerta_logout)),
            ]
        )

        icone_sair=ft.Container(
            padding=20,
            on_click=lambda e:self.page.open(alerta_logout),
            content=ft.Image("app/assets\icone_sair.svg"),
        )

        appbar=ft.Container(
            height=75,
            bgcolor="#1D3331",
            content=ft.Row(
                [
                    ft.Container(),
                    icone_sair
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            ),
            padding=0
        )

        return appbar