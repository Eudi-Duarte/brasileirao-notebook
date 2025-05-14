from jinja2 import Environment, FileSystemLoader
import pandas as pd
import os

templates_dir = "./templates"
env = Environment(loader=FileSystemLoader(templates_dir))

def render_home():
    '''
    This function aims to render Home static HTML files using Jinja templates
    and data processed via a notebook.
    '''
    brasileirao_matches = pd.read_csv("data/clean/brasileirao_matches.csv").to_dict(orient="records")
    home_template = env.get_template("home.html")
    rendered_home_template = home_template.render(matches=brasileirao_matches)
    
    # Save it into the public folder
    with open("public/home.html", "w") as f:
        f.write(rendered_home_template)

def render_teams_rundown():
    teams_path = "data/clean/teams/"
    for team_file in os.listdir(teams_path):
        team_name = team_file.replace(".csv", "")

        team_rundown = pd.read_csv(teams_path+team_file)
        team_rundown["x"] = "x"
        team_rundown_html = team_rundown[["mandante", "mandante_Placar", "x", "visitante_Placar", "visitante", "data", "hora"]].to_html(index=False, border=0, classes="team_rundown", header=False)

        # team stats
        # host
        team_rundown_host = team_rundown.loc[team_rundown["mandante"].str.lower() == team_name]
        team_rundown_away = team_rundown.loc[team_rundown["visitante"].str.lower() == team_name.lower()]

        gols_host = int(team_rundown_host["mandante_Placar"].sum())
        gols_away = int(team_rundown_away["visitante_Placar"].sum())

        team_stats = {
            # "Gols Como Mandante": gols_host,
            # "Gols Como Visitante": gols_away
            "Gols": gols_away + gols_host
        }

        # team_rundown = team_rundown.to_dict(orient="records")
        team_template = env.get_template("team.html")
        rendered_team_template = team_template.render(team_rundown=team_rundown_html, team_name=team_name, team_stats=team_stats)

        with open(f"public/teams/{team_name}.html", "w") as f:
            f.write(rendered_team_template)

if __name__ == "__main__":

    ## Render Home
    try:
        render_home()
    except Exception as e:
        print("Error while rendering home.html")
    else:
        print("'home.html' rendered successufully")

    ## Render teams_rundown
    render_teams_rundown()