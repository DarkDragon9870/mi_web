def on_page_markdown(markdown, page, config, files):
    if not markdown.strip():
        return "Pendiente de añadir contenido."
    return markdown