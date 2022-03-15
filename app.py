from datetime import datetime
from neomodel import config
from starlette.routing import Mount, Route
from starlette.applications import Starlette
from starlette.staticfiles import StaticFiles
from starlette.responses import JSONResponse

config.DATABASE_URL = 'bolt://neo4j:neoadmin@localhost:7687'

from models import Contributor, SalavatCollection

def resolve_send_salavat(request) -> JSONResponse:
    name = request.path_params['name']
    number = request.path_params['number']
    contrib = Contributor.nodes.get_or_none(name=name)
    if contrib is None:
        contrib = Contributor(name=name).save()
    salavats = SalavatCollection(number=number, date_contributed=datetime.now()).save()
    if contrib.salavats.connect(salavats):
        return JSONResponse({'ok': True})
    else:
        return JSONResponse({'ok': False})

app = Starlette(debug=True, routes=[
    Route('/send_salavat/{name}/{number:int}', resolve_send_salavat, methods=['POST', 'GET']),
    Mount('/', app=StaticFiles(directory='./client', html=True))
])