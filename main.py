import flet as ft


def main(page: ft.Page):
    page.title = "Aplicativo"
    page.padding = 30

    nome = ft.TextField(
        label="Nome do cliente",
        width=350
    )

    email = ft.TextField(
        label="E-mail do cliente",
        width=350
    )

    codigo = ft.TextField(
        label="Código do cliente",
        width=350
    )

    pais = ft.TextField(
        label="País",
        width=350
    )

    mensagem = ft.Text("")

    def entrar(e):
        if nome.value and email.value and codigo.value and pais.value:
            mensagem.value = "Dados preenchidos com sucesso!"
        else:
            mensagem.value = "Preencha todos os campos."

        page.update()

    botao = ft.ElevatedButton(
        text="Entrar",
        on_click=entrar
    )

    page.add(
        ft.Text(
            "Cadastro do Cliente",
            size=25,
            weight=ft.FontWeight.BOLD
        ),
        nome,
        email,
        codigo,
        pais,
        botao,
        mensagem
    )


ft.run(main)