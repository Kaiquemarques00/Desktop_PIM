import flet as ft
import requests

from ..components.appbar import Appbar
from ..components.sidebar import Sidebar

API_URL = "https://api-pim.onrender.com"
SECRET_KEY = "0d8689404a2c83325a0353496caafcdfa01abd76f4511037bad2a66ed3dd6050"

class UsuariosAPI(ft.Column):
    def __init__(self, app_state):
        self.app_state=app_state
        super().__init__()


        self.users_column = ft.Column(
            expand=True,
        )

        self.controls = [
            self.users_column
        ]

        self.lista_users()
        self.create_users()

    def lista_users(self):
        print(self.app_state.token)
        params = {
            "Authorization": f"Bearer {self.app_state.token}"
        }

        res = requests.get(f"{API_URL}/users", headers=params)

        usuarios = res.json()

        for user in usuarios:
            item_container=ft.Container(
                ft.Text(
                    user,
                    color="#000000"
                    ),
                    padding=50,
                    border=ft.border.all(2),
                )

            self.users_column.controls.append(item_container)

    def create_users(self):
        btn_create=ft.ElevatedButton("Criar",)

        self.users_column.controls.append(btn_create)

class TelaUsuarios:

    def __init__(self,page, app_state):
        self.page=page
        self.app_state=app_state

    def usuarios(self):
        appbar = Appbar(self.page).appBar()
        sidebar = Sidebar(self.page).sideBar("usuarios")
        users = UsuariosAPI(self.app_state)

        tela = ft.Container(
            expand=True,
            bgcolor="#D9D9D9",
            content=ft.Row(
                [
                    sidebar,
                    ft.Column(
                        [
                            appbar,
                            users
                        ],
                        expand=True
                    )
                ],
                spacing=0
            )
        )

        return tela