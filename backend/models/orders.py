from pydantic import BaseModel, Field
import uuid

class Order(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), alias='_id')
    name: str
    address: str
    file_path: str
    printer_name: str
    material_name: str
    colored: bool
    price: float