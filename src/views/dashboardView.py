import flet as ft

def DashboardView(page, tarea_controller):
    user = page.user_data if page.user_data else {"nombre": "Usuario", "id_usuario": 1}
    lista_tareas = ft.Column(scroll=ft.ScrollMode.ALWAYS, expand=True)
    
    def refresh():
        lista_tareas.controls.clear()
        for t in tarea_controller.obtener_lista(user['id_usuario']):
            lista_tareas.controls.append(
                ft.Card(
                    content=ft.Container(
                        content=ft.ListTile(
                            title=ft.Text(t['titulo'], weight="bold"),
                            subtitle=ft.Text(f"{t['descripcion']}\nPrioridad: {t['prioridad']}"),
                            trailing=ft.Text(t['estado'])
                        ), 
                        padding=10,
                        bgcolor=ft.Colors.ORANGE_300
                    )
                )
            )
        page.update()
        
    txt_titulo = ft.TextField(label="Nueva tarea", expand=True)
    
    def add_task(e):
        success, msg = tarea_controller.guardar_nueva(user['id_usuario'], txt_titulo.value, "", "media", "trabajo")
        if success:
            txt_titulo.value = ""
            refresh()
    try:   
        tareas_db = tarea_controller.obtener_lista(user['id_usuario'])
        for t in tareas_db:
            lista_tareas.controls.append(
                ft.Card(
                    content=ft.Container(
                        content=ft.ListTile(
                            title=ft.Text(t['titulo'], weight="bold"),
                            subtitle=ft.Text(t['descripcion'] if t['descripcion'] else "Sin descripción")
                        ), padding=10
                    )
                )
            )
    except Exception as ex:
        print(f"Error inicial: {ex}")
        lista_tareas.controls.append(ft.Text("Error al conectar con la base de datos"))        
            
    return ft.View(
        route="/dashboard", 
        appbar= ft.AppBar(
            title=ft.Text(f"Bienvenido, {user['nombre']}"),
            actions=[ft.IconButton(ft.Icons.EXIT_TO_APP, on_click=lambda _: page.go("/"))]
        ),
        controls=[
            ft.Column([
                ft.Row([txt_titulo, ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=add_task)]),
                ft.Divider(),
                ft.Text("Mis tareas pendientes", size=20, weight="bold"),
                lista_tareas
            ], expand=True)
        ])