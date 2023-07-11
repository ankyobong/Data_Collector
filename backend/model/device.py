from pydantic import BaseModel


class Item(BaseModel):
    containmentId: str
    deviceId: str
    manufacturer: str
    model: str
    name: str
    port: str
    rackRowId: str
    # sensors: list()
