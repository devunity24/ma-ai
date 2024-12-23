from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_items():
    return {"items": ["Item1", "Item2", "Item3"]}

@router.get("/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id, "name": "Item1"}
