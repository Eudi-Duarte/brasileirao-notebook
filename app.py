from jinja2 import Environment, FileSystemLoader
import pandas as pd

brasileirao_matches = pd.read_csv("data/clean/brasileirao_matches.csv").to_dict(orient="records")

templates_dir = "./templates"
env = Environment(loader=FileSystemLoader(templates_dir))

def render_home():
    '''
    This function aims to render Home static HTML files using Jinja templates
    and data processed via a notebook.
    '''
    home_template = env.get_template("home.html")
    rendered_home_template = home_template.render(matches=brasileirao_matches)
    
    # Save it into the public folder
    with open("public/home.html", "w") as f:
        f.write(rendered_home_template)

if __name__ == "__main__":
    render_home()