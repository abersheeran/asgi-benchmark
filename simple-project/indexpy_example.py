from indexpy import Index
from pydantic import BaseModel

app = Index()


class Path(BaseModel):
    name: str


@app.router.http("/hi/{name}", method="get")
async def sayhi(request, path: Path):
    return f"hi {path.name}"
