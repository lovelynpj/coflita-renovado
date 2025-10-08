import flet as ft

def identificar(e, usu, passw, mensaje, page, navigate=None):
    usuario = usu.value
    contrasena = passw.value
    usuarioss = {"jorge": '123', "pepe": '123', "juan": '456'}

    if usuario in usuarioss and usuarioss[usuario] == contrasena:
        mensaje.value = 'Acceso concedido'
        page.update()
        if navigate:
            # Actualizar el estado del usuario en la función navigate
            navigate(e, "login_success", usuario)
    else:
        mensaje.value = 'Acceso denegado'
        page.update()

def login_view(page: ft.Page, navigate=None):
    page.title = "inicio de sesion"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER   
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor="#9ba3a8"
    
    titulo = ft.Text("INICIO DE SESION COFLITA", size=30, weight="bold", color="black")
    usu = ft.TextField(label="Ingresar usuario", width=200)
    passw = ft.TextField(label="Ingresar contraseña", width=200, password=True)
    mensaje = ft.Text('')
    
    button_login1 = ft.ElevatedButton(text="Aceptar", on_click=lambda e: identificar(e, usu, passw, mensaje, page, navigate))
    button_login2 = ft.ElevatedButton(text="Cancelar", on_click= lambda e: navigate(e, "home") if navigate else None)

    login_content = ft.Column(
        controls=[
            ft.Container(
                content=titulo,
                alignment=ft.alignment.center,
                padding=ft.padding.only(top=50, bottom=30)
            ),
            ft.Container(
                content=ft.Column(
                    controls=[usu, passw],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                ),
                alignment=ft.alignment.center,
                padding=ft.padding.only(bottom=20)
            ),
            ft.Container(
                content=ft.Row(
                    controls=[button_login1, button_login2],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                alignment=ft.alignment.center,
                padding=ft.padding.only(bottom=20)
            ),
            ft.Container(
                content=mensaje,
                alignment=ft.alignment.center
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=0
    )
    
    page.add(login_content)
    page.update()

