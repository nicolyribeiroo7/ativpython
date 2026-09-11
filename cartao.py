import flet as ft
def main (page:ft.Page):
    page.title = "Cartão de Apresentação"
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = "black"
    page.window.width = 400
    page.window.height = 1000
    page.add(ft.Text("Gertrudes Lima Kardashian",size= 30, color="pink",))
    page.padding = ft.Padding(0, 200, 0, 0)
    page.add(ft.Text("Estudante de programação mobile",size= 15, color="white"))
   
ft.run(main) 