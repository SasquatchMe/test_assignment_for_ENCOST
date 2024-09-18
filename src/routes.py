from fastapi.routing import APIRouter

from src.repo import EndpointStateRepo
from src.schemas import Schema, FilteredResponse

router = APIRouter(
    prefix="/endpoints",
    tags=["Filtered Endpoints States"],
)


@router.post("/", response_model=FilteredResponse)
async def get_filtered_counted(data: Schema):
    response = await EndpointStateRepo.get_filtered_states_by_input_start(data)
    return response
