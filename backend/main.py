from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from questdb.ingress import Sender

app = FastAPI()
questdb_ip = "localhost"
questdb_port = 19009
templates = Jinja2Templates(directory="templates")


@app.get("/")
def read_form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})


@app.post("/questdb/device/{ip}/{port}d")
async def submit_form(request: Request, value: str = Form(...)):
    with Sender(questdb_ip, questdb_port) as sender:
        sender.row('sensors', symbols={'id': 'torontol'}, columns={'temperature': 20.0, 'humidity': 0.5, 'value': value})
        sender.flush()
    return templates.TemplateResponse("success.html", {"request": request, "value": value})


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8050)
