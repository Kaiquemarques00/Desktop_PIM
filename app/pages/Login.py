import flet as ft
import requests

API_URL = "https://api-pim.onrender.com"
SECRET_KEY = "0d8689404a2c83325a0353496caafcdfa01abd76f4511037bad2a66ed3dd6050"

class TelaLogin:
    def __init__(self,page, app_state):
        self.page=page
        self.app_state=app_state

    def login(self):

        def snack_erro_API(e, message):
            self.page.snack_bar=ft.SnackBar(
                ft.Text(
                    message,
                    text_align=ft.TextAlign.CENTER
                ),
                bgcolor="#DA4E49"
            )
            self.page.snack_bar.open=True
            self.page.update()

        def autenticar_usuario(e):
            dados_login={
                "email":input_email.value,
                "senha":input_senha.value
            }

            try:
                response = requests.post(f"{API_URL}/auth/login", json=dados_login)
                response_data = response.json()
                
                if response.status_code == 200 and "token" in response_data:
                    token = response_data["token"]
                    self.app_state.token = token

                    self.page.go("/home")

                else:
                    snack_erro_API(e, response_data)

            except requests.exceptions.RequestException as e:
                snack_erro_API(e, response_data)

            self.page.update()

        logo=ft.Container(
            alignment=ft.alignment.top_center,
            content=ft.Image(src="app/assets/logo2.png"),
            width=250,
            height=250,
            padding=ft.Padding(left=20,right=20,bottom=20,top=0)
        )

        input_email=ft.TextField(label="Insira seu E-mail: ",color=ft.colors.BLACK,label_style=ft.TextStyle(color=ft.colors.BLACK))
        input_senha=ft.TextField(label="Insira sua senha: ",color=ft.colors.BLACK,label_style=ft.TextStyle(color=ft.colors.BLACK),password=True,can_reveal_password=True)
        btn_login=ft.Container(
            alignment=ft.alignment.center_right,
            padding=ft.Padding(left=20,right=20,bottom=20,top=0),
            content=ft.TextButton("LOGIN",on_click=autenticar_usuario),
            ##content=ft.TextButton("LOGIN",on_click=lambda e:self.page.go("/home"),style=ft.ButtonStyle(bgcolor="#1C1C1C"))
        )

        #bloco de login e senha com imagem e fundo
        elemento_login=ft.Container(
            width=500,
            height=500,
            bgcolor="#D9D9D9",
            border_radius=10,
            padding=30,
            content=ft.Column(
                [
                    logo,
                    input_email,
                    input_senha,
                    btn_login, 
                ],
                alignment=ft.MainAxisAlignment.CENTER,  # Centraliza os itens dentro da coluna
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Centraliza na horizontal
            )
        )

        #####################################################################################
        #####################################################################################

        tela=ft.Container(
            expand=True,
            bgcolor="#1D3331",
            content=ft.ResponsiveRow(
                col={"xs":12,"sm":6,"md":4},
                controls=[
                    ft.Container(
                        content=elemento_login,
                        alignment=ft.alignment.center #joga os elementos pro centro da tela, sem expandir nada
                    ),
                ]
            )
        )

        return tela