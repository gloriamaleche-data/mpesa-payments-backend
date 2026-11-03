from pydantic import BaseModel

class NestedItemsModel(BaseModel):
    Name: str
    Value: int | str |float

class CallbackMetadataModel(BaseModel):
    Item: list[NestedItemsModel]

class STkCallBackModel(BaseModel):
    MerchantRequestID: str
    CheckoutRequestID: str
    ResultCode: int
    ResultDesc: str
    CallbackMetadata: CallbackMetadataModel | None = None

class StkBodyModel(BaseModel):
    stkCallback: STkCallBackModel

class DarajaCallBackModel(BaseModel):
    Body: StkBodyModel

