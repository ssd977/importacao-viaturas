import flet as ft
import asyncio


def main(page: ft.Page):
    page.title = "Importação de Viaturas"
    page.bgcolor = "black"

    carro = ft.Container(
        content=ft.Image(
        src="assets/carro_grande-1.png",
            width=320,
            fit=ft.BoxFit.CONTAIN,
        ),
        left=-350,
        top=100,
    )

    pista = ft.Stack(
        controls=[carro],
        expand=True,
    )

    page.add(pista)

    async def mover_carro():
        while True:
            carro.left = -350

            while carro.left < page.width:
                carro.left += 8
                pista.update()
                await asyncio.sleep(0.03)

            await asyncio.sleep(1)

    page.run_task(mover_carro)


ft.run(main)