import dash
from dash import html

app = dash.Dash(__name__)

app.layout = html.Div("Bonjour, Binder!")

if __name__ == '__main__':
    # Binder expose le port 8050 sur l'hôte, il faut donc écouter sur toutes les interfaces.
    app.run_server(debug=True, host='0.0.0.0', port=8050)
