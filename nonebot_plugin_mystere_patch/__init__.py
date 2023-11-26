from typing import Union, Any

from nonebot_plugin_guild_patch import Bot as BotV11, Event as EventV11, Message as MessageV11, \
    MessageSegment as MessageSegmentV11
from nonebot_plugin_guild_patch import Bot as BotV12, Event as EventV12, Message as MessageV12, \
    MessageSegment as MessageSegmentV12
from nonebot_plugin_guild_patch import logger

origin_v11_send = BotV11.send
origin_v12_send = BotV12.send


async def v11_send(
        self: BotV11,
        event: EventV11,
        message: Union[str, MessageV11, MessageSegmentV11],
        **params: Any,
) -> Any:
    event_dict = event.dict()
    if "id" not in event_dict:
        logger.warning("事件 ID 字段不存在，事件可能由非 Mystere 分发，放弃适配。")
    else:
        event.id = event_dict["id"]
        sub_type = ""
        if "sub_type" in event_dict:
            sub_type = event_dict["sub_type"]

        origin_type = event_dict["post_type"]
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
            "type": origin_type,
            "detail_type": detail_type,
            "sub_type": sub_type,
        }
    await origin_v11_send(self, event, message, **params)


async def v12_send(
        self: BotV12,
        event: EventV12,
        message: Union[str, MessageV12, MessageSegmentV12],
        **params: Any,
) -> Any:
    event_dict = event.dict()
    params["origin_event"] = {
        "id": event_dict["id"],
        "type": event_dict["type"],
        "detail_type": event_dict["detail_type"],
        "sub_type": event_dict["sub_type"],
    }
    await origin_v12_send(self, event, message, **params)


BotV11.send = v11_send
BotV12.send = v12_send
