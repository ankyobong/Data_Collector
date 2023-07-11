from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from questdb.ingress import Sender
from model import device

app = FastAPI()
questdb_ip = "localhost"
questdb_port = 19009
templates = Jinja2Templates(directory="templates")


@app.get("/")
def read_form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})


# @app.post("/questdb/device/items")
# async def submit_form(request: Request, item: dict):
#     item_data = device.Item(**item)
#     with Sender(questdb_ip, questdb_port) as sender:
#         sender.row('device', symbols={'id': 'torontol'}, columns=item_data)
#         sender.flush()
#     return templates.TemplateResponse("success.html", {"request": request})
@app.post("/questdb/device/items")
async def submit_form(request: Request, containmentId: str = Form(...),
                      deviceId: str = Form(...),
                      manufacturer: str = Form(...),
                      model: str = Form(...),
                      name: str = Form(...),
                      port: str = Form(...),
                      rackRowId: str = Form(...)):
    item = {'containmentId': containmentId,
            'deviceId': deviceId,
            'manufacturer': manufacturer,
            'model': model,
            'name': name,
            'port': port,
            'rackRowId': rackRowId,
            }
    with Sender(questdb_ip, questdb_port) as sender:
        sender.rsow('device', symbols={'deviceId': deviceId}, columns=item)
        sender.flush()
    return templates.TemplateResponse("success.html", {"request": request})


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
