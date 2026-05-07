import flet as ft

def LoginView(page: ft.Page, auth_controller):
    email_input = ft.TextField(label="Correo Electronico", width = 350, border_radius=10)
    pass_input = ft.TextField(label="Constraseña", password=True, can_reveal_password=True, width=350, border_radius=10)
    
    def login_click(e):
        if not email_input.value or not pass_input.value:
            page.snack_bar = ft.SnackBar(ft.Text("Por favor, llene todos los campos"))
            page.snack_bar.open = True
            page.update()
            return
        usuario = email_input.value
        contraseña = pass_input.value
        
        user, msg = auth_controller.login(usuario, contraseña)

        if user:
            page.user_data = user
            page.go("/dashboard")
        else:
            page.snack_bar = ft.SnackBar(ft.Text(msg))
            page.snack_bar.open = True
            page.update()
                        
    login_button = ft.ElevatedButton("Entrar", on_click=login_click, width=350, bgcolor="cyan", color = "black", icon=(ft.Icon(ft.Icons.MAIL, color=ft.Colors.WHITE, size=25)))
    registrar_button = ft.ElevatedButton("Crear una nueva cuenta", on_click=lambda _: page.go("/registrarse"), width=350, bgcolor="green", color = "black", icon=(ft.Icon(ft.Icons.PASSWORD, color=ft.Colors.WHITE, size=25)))
    
    pass_input.on_submit = login_click
        
    
    return ft.View(
        route = "/",
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        appbar=ft.AppBar(title=ft.Text("SIGE - Login - Cuando va a ganar el cruz azul - ya gano😍"), bgcolor="green", color= "white"),
        controls=[
            ft.Column(
                [
                    ft.Text("Acceso al sistema", size=24, weight="bold"),
                    email_input,
                    pass_input,
                    login_button,
                    registrar_button,
                    ft.TextButton("Se te olvido a contraseña?", on_click=lambda _: page.go("/registrarse"))
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                tight=True,
                spacing=20
            )
        ]
    )