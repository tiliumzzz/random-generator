from pydantic mport BaseModel
class Quote(BaseModel):
    id: int
    text: str
    author: str