import os

# Definizione della struttura del progetto
project_structure = {
    "my_portfolio_project": {
        "assets": {
            "images": {},
            "icons": {},
            "projects": {},
        },
        "data": {
            "skills.json": "",
            "projects.json": "",
            "categories.json": ""
        },
        "scripts": {
            "main.py": "",
            "utils.py": ""
        },
        "modules": {
            "skills": {
                "__init__.py": "",
                "skills_manager.py": ""
            },
            "projects": {
                "__init__.py": "",
                "projects_manager.py": ""
            },
            "ui": {
                "__init__.py": "",
                "views.py": ""
            }
        },
        "templates": {
            "index.html": "",
            "project_detail.html": "",
            "skills.html": ""
        },
        "styles": {
            "main.css": ""
        },
        "README.md": "",
        ".gitignore": ""
    }
}

def create_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        else:
            # file vuoto
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)

if __name__ == "__main__":
    create_structure(".", project_structure)
    print("Struttura progetto creata con successo!")
