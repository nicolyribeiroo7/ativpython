import flet as ft


def main(page: ft.Page):
	page.title = "Formulário"
	page.bgcolor = ft.Colors.PINK_50
	page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
	page.vertical_alignment = ft.MainAxisAlignment.CENTER

	nome = ft.TextField(
		label="Seu nome",
		hint_text="Digite seu nome",
		border_color=ft.Colors.PINK_300,
		focused_border_color=ft.Colors.PINK_500,
		label_style=ft.TextStyle(color=ft.Colors.WHITE),
		hint_style=ft.TextStyle(color=ft.Colors.WHITE),
	)
	termos = ft.Checkbox(
		label="Aceito os termos de uso",
		fill_color=ft.Colors.PINK_300,
		label_style=ft.TextStyle(color=ft.Colors.WHITE),
	)
	saudacao = ft.Text(color=ft.Colors.WHITE)

	def enviar_nome(e):
		if termos.value:
			saudacao.value = f"Olá, {nome.value}!"
		else:
			saudacao.value = "Aceite os termos de uso para continuar."
		page.update()

	page.add(
		ft.Container(
			bgcolor=ft.Colors.PINK_100,
			padding=30,
			border_radius=16,
			content=ft.Column(
			controls=[
				nome,
				termos,
				ft.ElevatedButton(
					"Enviar",
					on_click=enviar_nome,
					style=ft.ButtonStyle(
						bgcolor=ft.Colors.PINK_300,
						color=ft.Colors.WHITE,
					),
				),
				saudacao,
			],
			horizontal_alignment=ft.CrossAxisAlignment.CENTER,
			),
		)
	)


ft.run(main)
