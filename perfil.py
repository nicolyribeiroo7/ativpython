import flet as ft

def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Criando o container
    meu_container = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("Gertrudes Kardashian", size=24, no_wrap=True),
                ft.Text("Desenvolvedora mobile", color=ft.Colors.BLUE_900),
                ft.Row(
                    controls=[
                        ft.Icon(ft.Icons.EMAIL, color=ft.Colors.LIGHT_BLUE_400),
                        ft.Text("ge.kardashian@gmail.com"),
                    ]
                ),
                ft.Row(
                    controls=[
                        ft.Icon(ft.Icons.PHONE, color=ft.Colors.LIGHT_BLUE_400),
                        ft.Text("(11)4002-8922"),
                    ]
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        bgcolor=ft.Colors.BLUE_200,
        padding=30,
        margin=10,
        border_radius=10
    )
    
    # Adicionando à página
    page.add(meu_container)

ft.run(main)