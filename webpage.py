import flet as ft

# Define a function to create the main page view
def create_main_view(page: ft.Page, on_submit):
    page.title = "Fake News Detection"
    page.bgcolor = ft.colors.ORANGE_100

    # Create the TextField and submit button
    tb = ft.TextField(
        multiline=True,
        expand=True,
        border_color=ft.colors.TRANSPARENT,
        border_width=0,
        hint_text="Please enter text here",
        max_lines=10,
        text_style=ft.TextStyle(color=ft.colors.BLACK)
    )

    # Define the button click handler
    def button_clicked(e):
        input_text = tb.value
        result_text = f"Processed Result: {input_text.upper()}"  # Example processing
        on_submit(result_text)

    # Row 1: Heading with larger font size
    row1 = ft.Row(
        controls=[
            ft.Container(
                content=ft.Text(
                    "Fake News Detection",
                    size=48,
                    color=ft.colors.WHITE
                ),
                padding=20,
                bgcolor=ft.colors.ORANGE_500,
                alignment=ft.alignment.center,
                width=page.width
            )
        ],
        alignment=ft.alignment.center
    )

    # Row 2: Larger Input Box with Border
    row2 = ft.Row(
        controls=[
            ft.Container(
                content=tb,
                padding=20,
                bgcolor=ft.colors.WHITE,
                width=page.width,
                height=page.height * 0.5
            )
        ],
        alignment=ft.alignment.center
    )

    # Row 3: Submit Button
    row3 = ft.Row(
        controls=[
            ft.Container(
                content=ft.ElevatedButton(
                    text="Submit",
                    bgcolor=ft.colors.ORANGE_600,
                    color=ft.colors.WHITE,
                    on_click=button_clicked
                ),
                padding=20,
                alignment=ft.alignment.center
            )
        ]
    )

    # Add rows to the page
    page.add(
        ft.Column(
            controls=[row1, row2, row3],
            spacing=10,
            alignment=ft.alignment.center
        )
    )

# Define a function to create the result view
def create_result_view(page: ft.Page, result: str):
    page.title = "Result Page"
    page.bgcolor = ft.colors.ORANGE_100

    # Create a Container to hold the result
    result_container = ft.Container(
        content=ft.Text(
            result,
            size=24,
            color=ft.colors.BLACK
        ),
        padding=20,
        bgcolor=ft.colors.WHITE,
        width=page.width * 0.8,
        height=page.height * 0.6
    )

    # Add the result container to the page
    page.add(
        ft.Column(
            controls=[result_container],
            alignment=ft.alignment.center,
            spacing=20
        )
    )

# Define the main function to handle the application
def main(page: ft.Page):
    # Function to handle submission and show the result view
    def handle_submit(result_text: str):
        page.controls.clear()
        create_result_view(page, result_text)
        page.update()

    # Create and display the main page view
    create_main_view(page, handle_submit)

# Run the app
ft.app(target=main)
