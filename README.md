# nonebot-plugin-mystere-patch

此插件提供针对 Mystere 的补丁支持，适用于 NoneBot2，开发者无需对现有代码进行任何修改。

插件包含 [mnixry/nonebot-plugin-guild-patch](https://github.com/mnixry/nonebot-plugin-guild-patch)。

## 补丁内容

PS：部分扩展内容正在申请并入 OneBot：[查看详情](https://github.com/orgs/botuniverse/discussions/249)

### OneBot V11

+ 所有事件新增参数：

  | 字段名 | 数据类型   | 说明                                        |
  |-----|--------|-------------------------------------------|
  | id  | string | 事件唯一标识符，当事件类型为 `message` 时值同 `message_id` |

+ `send_message` 动作请求新增参数：

  | 字段名          | 数据类型           | 说明                                            |
  |--------------|----------------|-----------------------------------------------|
  | origin_event | map[string]any | 可选，回复事件，当 `origin_event` 字段存在时则为被动消息，否则为主动消息。 |

  PS：此处提到的回复不同于 [消息段中定义的回复](https://12.onebot.dev/interface/message/segments/#reply)，在 QQ 开放平台中将 [消息段中定义的回复](https://12.onebot.dev/interface/message/segments/#reply) 定义为 [消息引用（message_reference）](https://bot.q.qq.com/wiki/develop/api-v2/server-inter/message/send-receive/send.html)
    
  其中 `origin_event` 定义如下：
    
  | 字段名         | 数据类型   | 说明                                                                                                                         |
  |-------------|--------|----------------------------------------------------------------------------------------------------------------------------|
  | id          | string | 原事件 ID，由 Mystere 分发事件时提供                                                                                                   |
  | type        | string | 原事件类型，同 [OneBot V11 事件类型](https://github.com/botuniverse/onebot-11/tree/master/event#%E5%86%85%E5%AE%B9%E5%AD%97%E6%AE%B5) |
  | detail_type | string | 原事件详细类型 [1]                                                                                                                |
  | sub_type    | string | 原事件子类型（详细类型的下一级类型） [2]                                                                                                     |
     
  1. `detail_type` 定义如下：
     + 当 `type` 为 `meta` 时，值为原事件的 `meta_event_type`；
     + 当 `type` 为 `message` 时，值为原事件的 `message_type`；
     + 当 `type` 为 `notice` 时，值为原事件的 `notice_type`；
     + 当 `type` 为 `request` 时，值为原事件的 `request_type`。

  2. `sub_type` 定义如下：
     + 当 `type` 为 `meta` 时，值为空字符串；
     + 当 `type` 为 `message` 时，值为原事件的 `sub_type`；
     + 当 `type` 为 `notice` 时，值为原事件的 `sub_type`；
     + 当 `type` 为 `meta` 时，值为空字符串；

     简而言之就是当原事件参数存在 `sub_type` 时传递原值，否则传递空字符串。


### OneBot V12

+ `send_message` 动作请求新增参数：

  | 字段名          | 数据类型           | 说明                                            |
  |--------------|----------------|-----------------------------------------------|
  | origin_event | map[string]any | 可选，回复事件，当 `origin_event` 字段存在时则为被动消息，否则为主动消息。 |

  PS：此处提到的回复不同于 [消息段中定义的回复](https://12.onebot.dev/interface/message/segments/#reply)，在 QQ 开放平台中将 [消息段中定义的回复](https://12.onebot.dev/interface/message/segments/#reply) 定义为 [消息引用（message_reference）](https://bot.q.qq.com/wiki/develop/api-v2/server-inter/message/send-receive/send.html)

  其中 `origin_event` 定义如下（同 [OneBot V12 事件类型](https://12.onebot.dev/connect/data-protocol/event/)）：

  | 字段名         | 数据类型   | 说明                 |
  |-------------|--------|--------------------|
  | id          | string | 原事件 ID             |
  | type        | string | 原事件类型              |
  | detail_type | string | 原事件详细类型            |
  | sub_type    | string | 原事件子类型（详细类型的下一级类型） |
