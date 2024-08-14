from fastapi import APIRouter

router = APIRouter(prefix="/task",
                   tags=["task"])


@router.get("/")
async def get_all_tasks():
    pass


@router.get("/task_id")
async def get_task_by_id():
    pass


@router.post("/create")
async def create_task():
    pass


@router.put("/update")
async def update_task():
    pass


@router.put("/delete")
async def delete_task():
    pass
