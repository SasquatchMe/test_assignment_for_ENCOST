import pytz
from tortoise.expressions import Q

from src.models import EndpointStates
from src.schemas import Schema, FilteredResponse


class EndpointStateRepo:

    @classmethod
    async def get_filtered_states_by_input_start(cls, data: Schema):
        input_start_data = data.model_dump()
        moscow_timezone = pytz.timezone("Europe/Moscow")
        input_start = moscow_timezone.localize(input_start_data["input_start"])
        input_start_unix = int(input_start.timestamp() * 1000)

        endpoints = await EndpointStates.filter(
            Q(state_start__gte=input_start_unix) & Q(endpoint_id=139)
        ).order_by("-state_start")

        filtered_endpoints = [ep for ep in endpoints if ep.id % 3 == 0]
        state_id = filtered_endpoints[2].id if len(filtered_endpoints) > 3 else None

        return FilteredResponse(
            filtered_counts=len(filtered_endpoints), state_id=state_id
        )
