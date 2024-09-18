from tortoise import fields
from tortoise.models import Model


class Client(Model):
    id = fields.IntField(pk=True)
    client_name = fields.CharField(max_length=255)

    class Meta:
        table = "clients"


class Endpoint(Model):
    id = fields.IntField(pk=True)
    endpoint_name = fields.CharField(max_length=255)

    class Meta:
        table = "endpoints"


class EndpointStates(Model):
    id = fields.IntField(pk=True)
    endpoint = fields.ForeignKeyField("models.Endpoint", on_delete=fields.CASCADE)
    client = fields.ForeignKeyField("models.Client", on_delete=fields.CASCADE)
    state_name = fields.CharField(max_length=255)
    state_reason = fields.CharField(max_length=255)
    state_start = fields.IntField()
    state_end = fields.IntField(null=True)
    state_id = fields.CharField(max_length=255)
    group_id = fields.CharField(max_length=255)
    reason_group = fields.CharField(max_length=255, null=True)
    info = fields.JSONField(null=True)

    class Meta:
        table = "endpoint_states"
