import flet as ft


def main(page: ft.Page):

    page.title = "Appzinho da Pzilda"
    page.bgcolor = ft.Colors.PINK_50

    # Lista de produtos
    itens = []

    # Lista que mostra os produtos
    lista = ft.Column(
        spacing=15
    )

    # INPUT
    campo_item = ft.TextField(
        hint_text="Novo item",
        expand=True,
        height=60,
        border_radius=5,
        color=ft.Colors.WHITE,
        hint_style=ft.TextStyle(color=ft.Colors.WHITE),
    )

    # Função para atualizar a lista
    def atualizar_lista():
        lista.controls.clear()

        for item in itens:

            def diminuir(e, item=item):
                if item["quantidade"] > 1:
                    item["quantidade"] -= 1

                atualizar_lista()
                page.update()

            def aumentar(e, item=item):
                item["quantidade"] += 1

                atualizar_lista()
                page.update()

            def excluir(e, item=item):
                itens.remove(item)

                atualizar_lista()
                page.update()

            linha = ft.Row(
                [
                    # Nome
                    ft.Text(
                        item["nome"],
                        size=20,
                        color=ft.Colors.WHITE,
                        expand=True,
                    ),

                    # Menos
                    ft.IconButton(
                        icon=ft.Icons.REMOVE,
                        icon_color=ft.Colors.PINK_400,
                        icon_size=30,
                        on_click=diminuir,
                    ),

                    # Quantidade
                    ft.Text(
                        str(item["quantidade"]),
                        size=20,
                        color=ft.Colors.WHITE,
                        width=25,
                        text_align=ft.TextAlign.CENTER,
                    ),

                    # Mais
                    ft.IconButton(
                        icon=ft.Icons.ADD,
                        icon_color=ft.Colors.PINK_400,
                        icon_size=30,
                        on_click=aumentar,
                    ),

                    # Excluir
                    ft.IconButton(
                        icon=ft.Icons.DELETE_OUTLINE,
                        icon_color=ft.Colors.PINK_700,
                        icon_size=28,
                        on_click=excluir,
                    ),
                ],
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            )

            lista.controls.append(linha)

    # Adicionar item
    def adicionar(e):
        nome = campo_item.value.strip()

        if nome != "":
            itens.append({
                "nome": nome,
                "quantidade": 1
            })

            campo_item.value = ""

            atualizar_lista()
            page.update()

    # BOTÃO
    botao_adicionar = ft.Button(
        content="Adicionar",
        on_click=adicionar,
        bgcolor=ft.Colors.PINK_400,
        color="white",
        width=140,
        height=60,
    )

    # CAMPO + BOTÃO
    entrada = ft.Row(
        [
            campo_item,
            botao_adicionar,
        ],
        expand=True,
        spacing=15,
    )

    # TELA
    page.add(
        ft.Container(
            content=ft.Column(
                [
                    entrada,
                    lista,
                ],
                spacing=25,
            ),

            # CORREÇÃO DO ERRO:
            padding=ft.Padding(
                left=30,
                right=30,
                top=80,
                bottom=30,
            ),

            expand=True,
        )
    )


ft.run(main, view=ft.AppView.WEB_BROWSER)