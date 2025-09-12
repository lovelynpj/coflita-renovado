import flet as ft

def identificar(e, usu, passw, mensaje, page, navigate=None):
    usuario = usu.value
    contrasena = passw.value
    usuarioss = {"jorge": '123', "pepe": '123', "juan": '456'}

    if usuario in usuarioss and usuarioss[usuario] == contrasena:
        mensaje.value = 'Acceso concedido'
        page.update()    
        if navigate:
            navigate(e, "home")
    else:
        mensaje.value = 'Acceso denegado'

    page.update()
    

def register_view(page: ft.Page, navigate=None):
    page.title = "registro de usuario"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER   
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor="#9ba3a8"
    titulo = ft.Text("REGISTRO DE USUARIO COFLITA", size=30, weight="bold", color="black")
    usu = ft.TextField(label="Ingresa tu nombre de usuario", width=200)
    gmail = ft.TextField(label="Ingresa tu gmail", width=200)
    passw = ft.TextField(label="Ingresar contraseña", width=200)
    conf_passw = ft.TextField(label="Confirma tu contraseña", width=200)

    def registrar(e):
        if passw.value != conf_passw.value:
            mensaje.value = "❌ Las contraseñas no coinciden"
        elif not usu.value or not gmail.value or not passw.value:
            mensaje.value = "⚠️ Completa todos los campos"
        else:
            mensaje.value = f"✅ Usuario {usu.value} registrado correctamente"
            page.update()
            return
        page.update()

    button_login1 = ft.ElevatedButton(text="Aceptar", on_click=lambda e: identificar(e, usu, passw, mensaje, page, navigate))
    button_login2 = ft.ElevatedButton(text="Cancelar", on_click= lambda e: navigate(e, "home")if navigate else None)
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
    page.update()
