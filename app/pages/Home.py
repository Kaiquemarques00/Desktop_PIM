import flet as ft

from ..components.appbar import Appbar
from ..components.sidebar import Sidebar

class TelaHome:

    def __init__(self,page, app_state):
        self.page=page
        self.app_state=app_state

    def home(self):
        appbar = Appbar(self.page).appBar()
        sidebar = Sidebar(self.page).sideBar("home")

        tela = ft.Container(
            expand=True,
            bgcolor="#D9D9D9",
            content=ft.Row(
                [
                    sidebar,
                    ft.Column(
                        [
                            appbar,
                        ],
                        expand=True
                    )
                ],
                spacing=0
            )
        )

        return tela