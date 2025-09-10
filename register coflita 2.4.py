import flet as ft

def identificar(e, usu, passw, mensaje, page):
    usuario = usu.value
    contrasena = passw.value
    usuarioss = {"jorge": '123', "pepe": '123', "juan": '456'}

    if usuario in usuarioss and usuarioss[usuario] == contrasena:
        mensaje.value = 'Acceso concedido'
    else:
        mensaje.value = 'Acceso denegado'

    page.update()

def main(page: ft.Page):
    page.title = "registro de usuario"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER   
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor="#9ba3a8"
    titulo = ft.Text("REGISTRO DE USUARIO COFLITA", size=30, weight="bold", color="black")
    usu = ft.TextField(label="Ingresa tu nombre de usuario", width=200)
    gmail = ft.TextField(label="Ingresa tu gmail", width=200)
    passw = ft.TextField(label="Ingresar contraseña", width=200)
    conf_passw = ft.TextField(label="Confirma tu contraseña", width=200)
    button_login1 = ft.ElevatedButton(text="Aceptar", on_click=lambda e: identificar(e, usu, passw, mensaje, page))
    button_login2 = ft.ElevatedButton(text="Cancelar")
    mensaje = ft.Text('')
    

    page.add(
        ft.Column(
            controls=[titulo]
        )
    )
    page.add(
        ft.Column(
            controls=[usu,gmail,passw, conf_passw],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )
    page.add(
        ft.Row(
            controls=[button_login1,button_login2],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

    page.add(mensaje)

ft.app(target=main)