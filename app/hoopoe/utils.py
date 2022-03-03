
def slugify(text):
    if not text:
        return ""
    
    return text.lower().replace(" ", "-")
