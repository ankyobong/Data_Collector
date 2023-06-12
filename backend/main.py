from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from questdb.ingress import Sender

app = FastAPI()
questdb_writer = Sender()
templates = Jinja2Templates(directory="templates")


@app.get("/")
def read_form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})


@app.post("/submit")
async def submit_form(request: Request, value: str = Form(...)):
    questdb_writer.insert(table='data', value=value)
    return templates.TemplateResponse("success.html", {"request": request, "value": value})


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
