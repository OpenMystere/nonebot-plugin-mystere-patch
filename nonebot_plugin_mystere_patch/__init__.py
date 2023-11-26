from typing import Union, Any

from nonebot.adapters.onebot.v11 import Bot as BotV11, Event as EventV11, Message as MessageV11, \
    MessageSegment as MessageSegmentV11
from nonebot.adapters.onebot.v12 import Bot as BotV12, Event as EventV12, Message as MessageV12, \
    MessageSegment as MessageSegmentV12

origin_v11_send = BotV11.send
origin_v12_send = BotV12.send


async def v11_send(
        self: BotV11,
        event: EventV11,
        message: Union[str, MessageV11, MessageSegmentV11],
        proactive: bool = False,
        **params: Any,
) -> Any:
    event_dict = event.dict()
    event.id = event_dict["id"]
    # 如果不是主动消息，则添加 origin_event 字段
    if not proactive:
        sub_type = ""
        if "sub_type" in event_dict:
            sub_type = event_dict["sub_type"]

        origin_type = event_dict["type"]
        if origin_type == "meta":
            detail_type = event_dict["meta_event_type"]
        elif origin_type == "message":
            detail_type = event_dict["message_type"]
        elif origin_type == "notice":
            detail_type = event_dict["notice_type"]
        elif origin_type == "request":
            detail_type = event_dict["request_type"]
        else:
            raise ValueError("Unknown type of event: " + event_dict["type"])
        params["origin_event"] = {
            "id": event_dict["id"],
            "type": event_dict["type"],
            "detail_type": detail_type,
            "sub_type": sub_type,
        }
    await origin_v11_send(self, event, message, **params)


async def v12_send(
        self: BotV12,
        event: EventV12,
        message: Union[str, MessageV12, MessageSegmentV12],
        proactive: bool = False,
        **params: Any,
) -> Any:
    event_dict = event.dict()
    # 如果不是主动消息，则添加 origin_event 字段
    if not proactive:
        params["origin_event"] = {
            "id": event_dict["id"],
            "type": event_dict["type"],
            "detail_type": event_dict["detail_type"],
            "sub_type": event_dict["sub_type"],
        }
    await origin_v12_send(self, event, message, **params)


BotV11.send = v11_send
BotV12.send = v12_send
