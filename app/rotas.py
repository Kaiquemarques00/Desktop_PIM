import flet as ft

from app.pages.Login import TelaLogin
from app.pages.Home import TelaHome
from app.pages.Usuarios import TelaUsuarios

class AppState:
    def __init__(self):
        self.token = None

def registro_rotas(page:ft.Page):
    app_state = AppState()

    def mudar_rotas(route):

        page.views.clear()

        if page.route=="/":
            obj_login=TelaLogin(page, app_state)
            page.views.append(ft.View(route="/",controls=[obj_login.login()]))

        elif page.route=="/home":
            obj_home=TelaHome(page, app_state)
            page.views.append(ft.View(route="/home",controls=[obj_home.home()]))
        
        elif page.route=="/usuarios":
            obj_usuarios=TelaUsuarios(page, app_state)
            page.views.append(ft.View(route="/usuarios",controls=[obj_usuarios.usuarios()]))

        page.update()

    page.on_route_change=mudar_rotas