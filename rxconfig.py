import reflex as rx

config = rx.Config(
    app_name="tracker",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ],
)