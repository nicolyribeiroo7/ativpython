import flet as ft
def main (page:ft.Page):
    page.title = "meu primeiro appzinho fofinho di mamae"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = "black"
    # criando funcoes
    def diminuir(e):
        caixa_texto.value = str(int(caixa_texto.value) - 1)
    def aumentar(e):
        caixa_texto.value = str(int(caixa_texto.value) + 1)
    # criando os itens da pagina 
    botao_menos = ft.IconButton(ft.Icons.REMOVE, on_click=diminuir)
    caixa_texto = ft.TextField(value="0", width=100, text_align=ft.TextAlign.CENTER)
    botao_mais = ft.IconButton(ft.Icons.ADD)

    page.add(
    ft.Row(
        [botao_menos, caixa_texto, botao_mais],
        alignment=ft.MainAxisAlignment.CENTER,
    )
)
ft.run(main)