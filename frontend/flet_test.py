import flet as ft


def main(page):
    device_ip = ft.TextField(label="device_ip", autofocus=True)
    device_port = ft.TextField(label="device_port")
    greetings = ft.Column()

    def btn_click(e):
        greetings.controls.append(ft.Text(f"insert, {device_ip.value} : {device_port.value}"))
        device_ip.value = ""
        device_port.value = ""
        page.update()
        device_ip.focus()

    page.add(
        device_ip,
        device_port,
        ft.ElevatedButton("insert", on_click=btn_click),
        greetings,
    )


ft.app(target=main)
