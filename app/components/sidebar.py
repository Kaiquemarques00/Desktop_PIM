import flet as ft

class Sidebar:

    def __init__(self, page):
        self.page=page

    def sideBar(self, current):

        status_colors = {
        "currentPage": "#1C1C1C",
        "otherPage": "#2E2E2E",
        }

        def hover_btn(e):
            if e.control.bgcolor == "#111111":
                e.control.bgcolor="111111"
            if e.data=="true": 
                e.control.bgcolor="#1C1C1C"
            else:
                e.control.bgcolor=None

            ##e.control.bgcolor="#1C1C1C" if e.data=="true" else None
            e.control.update()

        def navigation(path):
            self.page.go(path)
            self.page.update()

        logo=ft.Image("app/assets/logo3.png")
            
        btn_home=ft.Container(
            padding=10,
            on_hover=hover_btn,
            on_click=lambda e:navigation("/home"),
            content=ft.Row(
                [
                    ft.Image("app/assets/icone_home.svg",width=30,height=30),
                    ft.Text("Home")
                ]
            )
        )

        btn_usuarios=ft.Container(
            padding=10,
            on_hover=hover_btn,
            on_click=lambda e:navigation("/usuarios"),
            content=ft.Row(
                [
                    ft.Image("app/assets/icone_perfil_2.svg",width=30,height=30),
                    ft.Text("Usuários")
                ]
            )
        )

        btn_culturas=ft.Container(
            padding=10,
            on_hover=hover_btn,
            content=ft.Row(
                [
                    ft.Image("app/assets/icone_cultura.svg",width=30,height=30),
                    ft.Text("Culturas")
                ]
            )
        )

        btn_plantios=ft.Container(
            padding=10,
            on_hover=hover_btn,
            content=ft.Row(
                [
                    ft.Image("app/assets/icone_plantio.svg",width=30,height=30),
                    ft.Text("Plantios")
                ]
            )
        )

        btn_colheitas=ft.Container(
            padding=10,
            on_hover=hover_btn,
            content=ft.Row(
                [
                    ft.Image("app/assets/icone_colheita.svg",width=30,height=30),
                    ft.Text("Colheitas")
                ]
            )
        )

        btn_insumos=ft.Container(
            padding=10,
            on_hover=hover_btn,
            content=ft.Row(
                [
                    ft.Image("app/assets/icone_insumos.svg",width=30,height=30),
                    ft.Text("Insumos")
                ]
            )
        )

        btn_fornecedores=ft.Container(
            padding=10,
            on_hover=hover_btn,
            content=ft.Row(
                [
                    ft.Image("app\/assets/icone_fornecedores.svg",width=30,height=30),
                    ft.Text("Fornecedores")
                ]
            )
        )

        btn_pedidos=ft.Container(
            padding=10,
            on_hover=hover_btn,
            content=ft.Row(
                [
                    ft.Image("app/assets/icone_financeiro.svg",width=30,height=30),
                    ft.Text("Pedidos")
                ]
            )
        )

        btn_relatorios=ft.Container(
            padding=10,
            on_hover=hover_btn,
            content=ft.Row(
                [
                    ft.Image("app/assets/icone_prancheta.svg",width=30,height=30),
                    ft.Text("Relatórios")
                ]
            )
        )

        if current == "home":
            btn_home.bgcolor = "#111111"
            btn_home.on_hover = None

        elif current == "usuarios":
            btn_usuarios.bgcolor = "#111111"
            btn_usuarios.on_hover = None
        
        elif current == "culturas":
            btn_culturas.bgcolor = "#111111"
            btn_culturas.on_hover = None

        elif current == "plantios":
            btn_plantios.bgcolor = "#111111"
            btn_plantios.on_hover = None
        
        elif current == "colheitas":
            btn_colheitas.bgcolor = "#1C1C1C"
            btn_colheitas.on_hover = None
        
        elif current == "insumos":
            btn_insumos.bgcolor = "#1C1C1C"
            btn_insumos.on_hover = None
        
        elif current == "fornecedores":
            btn_fornecedores.bgcolor = "#1C1C1C"
            btn_fornecedores.on_hover = None
        
        elif current == "pedidos":
            btn_pedidos.bgcolor = "#1C1C1C"
            btn_pedidos.on_hover = None
        
        elif current == "relatorios":
            btn_relatorios.bgcolor = "#1C1C1C"
            btn_relatorios.on_hover = None

        sidebar=ft.Container(
            width=160,
            bgcolor="#2E2E2E",
            content=ft.Column(
                [
                    logo,
                    btn_home,
                    btn_usuarios,
                    btn_culturas,
                    btn_plantios,
                    btn_colheitas,
                    btn_insumos,
                    btn_fornecedores,
                    btn_pedidos,
                    btn_relatorios
                ]
            ),
            padding=0
        )

        return sidebar