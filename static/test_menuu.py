import flet as ft

def main(page: ft.Page):
    page.title = "Информатика"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.START
    page.bgcolor = '#FFFFFF'

    # Создаем выдвижную панель с фиксированной высотой
    sidebar = ft.NavigationRail(
        selected_index=0,
        bgcolor=ft.colors.BLUE,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.icons.HOME,
                selected_icon=ft.icons.HOME,
                label="Главная"
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.INFO,
                selected_icon=ft.icons.INFO,
                label="Информация"
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.SETTINGS,
                selected_icon=ft.icons.SETTINGS,
                label="Настройки"
            ),
        ],
        on_change=lambda e: update_content(e.control.selected_index)
    )

    # Оборачиваем NavigationRail в Container с фиксированной высотой
    sidebar_container = ft.Container(
        content=sidebar,
        height=1000  # Установите желаемую высоту
    )

    # Контент, который будет обновляться
    content = ft.Column()

    def update_content(selected_index):
        content.controls.clear()
        if selected_index == 0:
            content.controls.append(ft.Text("ЗАГОЛОВОК: Главная страница", size=24))
            content.controls.append(ft.Text("Добро пожаловать на уроки по информатике!", size=18))
        elif selected_index == 1:
            content.controls.append(ft.Text("ЗАГОЛОВОК: Информация", size=24))
            content.controls.append(ft.Text("Здесь вы найдете информацию о курсах.", size=18))
        elif selected_index == 2:
            content.controls.append(ft.Text("ЗАГОЛОВОК: Настройки", size=24))
            content.controls.append(ft.Text("Настройки приложения.", size=18))

        page.update()

    # Добавляем боковую панель и контент на страницу
    page.add(
        ft.Row([
            sidebar_container,
            ft.VerticalDivider(),
            ft.Column([
                content  # Здесь мы помещаем контент в Column
            ], expand=True)  # Позволяем Column занимать оставшееся пространство
        ], alignment=ft.MainAxisAlignment.START)
    )

# Запуск приложения
ft.app(target=main)
