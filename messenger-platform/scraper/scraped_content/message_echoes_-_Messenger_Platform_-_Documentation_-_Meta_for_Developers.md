# message_echoes - Messenger Platform - Documentation - Meta for Developers

Source: https://developers.facebook.com/docs/messenger-platform/reference/webhook-events/message-echoes

# `message_echoes` Webhook Event Reference

This callback will occur when a message has been sent by your page. You may receive `text` messages or messages with attachments (`image`, `video`, `audio`, `template` or `fallback`). The payload will also include an optional custom `metadata` sent by the sender, and the corresponding `app_id`.  
You can subscribe to this callback by selecting the `message_echoes` field when [setting up](/docs/messenger-platform/webhook-reference#setup) your webhook.

Multiple types of messages are supported:

* [Text message](#text)
* [Message with image, audio, video or file attachment](#binary)
* [Message with appointment booking](#appointment)
* [Message with template attachment](#template)
* [Message with fallback attachment](#fallback)
* [Message with products](#products)
* [Message which is a reply to another message](#reply)

## Common Format

### Example 1

```
{
  "sender":{
    "id":"<PAGE_ID>"
  },
  "recipient":{
    "id":"<PSID>"
  },
  "timestamp":1457764197627,
  "message":{
    "is_echo":true,
    "app_id":1517776481860111,
    "metadata": "<DEVELOPER_DEFINED_METADATA_STRING>",
    "mid":"mid.1457764197618:41d102a3e1ae206a38",
    ...
  }
}
```

### Example 2

```
{
    "object": "page",
    "entry": [
        {
            "id": "<PAGE_ID>",
            "time": 1570053170926,
            "standby": [
                {
                    "sender": {
                        "id": "<PAGE_ID>"
                    },
                    "recipient": {
                        "id": "<PSID>"
                    },
                    "timestamp": 1570053170673,
                    "message": {
                        "mid": "qT7ywaKpO9kkQR7Gv-nM8LIfLZDamVrALniheUYEDdHJXjDXEAyaS1xxONzb2Iv-DFzmTihfWJV012P5pK0AhQ",
                        "is_echo": true,
                        "app_id": <APPID>,
                        "attachments": [
                            {
                                "title": "",
                                "url": "https:\/\/www.facebook.com\/commerce\/update\/",
                                "type": "template",
                                "payload": {
                                    "template_type": "media",
                                    "elements": [
                                        {
                                            "media_type": "image",
                                            "attachment_id": 2457235337685388
                                        }
                                    ]
                                }
                            }
                        ]
                    }
                }
            ]
        }
    ]
}
```

### Properties

### `sender`

`sender` Field | Description || `id` *string* | The ID for your Facebook Page |

### `recipient`

`recipient` Field | Description || `id` *string* | The Page-scoped ID for the person who received a message from your business |

### `message`

Field Name | Type | Description || `is_echo` | Boolean | Indicates the message sent from the page itself |
| `app_id` | String | ID of the app from which the message was sent. Starting Graph API `v12.0`+, `app_id` field will return Facebook Page inbox app id (`26390203743090`) whenever the message is sent via Facebook Page inbox. |
| `metadata` | String | Custom string passed to the [Send API](/docs/messenger-platform/send-api-reference#request) as the `metadata` field. Only present if the `metadata` property was set in the original message. |
| `mid` | String | Message ID |

## Text message

### Example

```
{
  "sender":{
    "id":"<PAGE_ID>"
  },
  "recipient":{
    "id":"<PSID>"
  },
  "timestamp":1457764197627,
  "message":{
    "is_echo":true,
    "app_id":1517776481860111,
    "metadata": "<DEVELOPER_DEFINED_METADATA_STRING>",
    "mid":"mid.1457764197618:41d102a3e1ae206a38",
    "text":"hello, world!"
  }
}
```

### Properties

### `message`

Property | Type | Description || `text` | String | Text of message |

## Message with image, audio, video or file attachment

### Example

```
{
  "sender":{
    "id":"<PAGE_ID>"
  },
  "recipient":{
    "id":"<PSID>"
  },
  "timestamp":1458696618268,
  "message":{
    "is_echo":true,
    "app_id":1517776481860111,
    "metadata": "<DEVELOPER_DEFINED_METADATA_STRING>",
    "mid":"mid.1458696618141:b4ef9d19ec21086067",
    "attachments":[
      {
        "type":"image",
        "payload":{
          "url":"<IMAGE_URL>"
        }
      }
    ]
  }
}
```

### Properties

### `message.attachments`

Properties | Type | Description || `type` | String | Type of attachment: `image`, `audio`, `video` or `file` |
| `payload.url` | String | URL of attachment |

## Message with appointment booking

### Example

```
{
  "sender":{
    "id":"<PAGE_ID>"
  },
  "recipient":{
    "id":"<PSID>"
  },
  "timestamp":1458696618268,
  "message":{
    "is_echo":true,
    "app_id":1517776481860111,
    "metadata": "<DEVELOPER_DEFINED_METADATA_STRING>",
    "mid":"mid.1458696618141:b4ef9d19ec21086067",
    "attachments":[
      {
        "type":"appointment_booking",
        "payload": {
           "booking_id": "<BOOKING_ID>"
           "status": "<requested|confirmed|declined|cancelled>",
           "start_time": 1739612400,
           "end_time": 1739616000,
           "timezone": "America/Los_Angeles"
        }
      }
    ]
  }
}
```

### Properties

### `message.attachments`

Properties | Type | Description || `type` | String | Type of attachment: `appointment_booking` |
| `payload.booking_id` | String | ID of the booking associated with the appointment |
| `payload.status` | String | Current status of the appointment. Can be `requested`, `confirmed`, `declined`, `cancelled` |
| `payload.start_time` | Integer | Appointment start time as a Unix timestamp (seconds). |
| `payload.end_time` | Integer | Appointment end time as a Unix timestamp (seconds). |
| `payload.timezone` | String | IANA timezone identifier (e.g., `America/Los_Angeles`) |

## Message with template attachment

### Example

```
{
  "sender":{
    "id":"<PAGE_ID>"
  },
  "recipient":{
    "id":"<PSID>"
  },
  "timestamp":1458696618268,
  "message":{
    "is_echo":true,
    "app_id":1517776481860111,
    "metadata": "<DEVELOPER_DEFINED_METADATA_STRING>",
    "mid":"mid.1458696618141:b4ef9d19ec21086067",
    "attachments":[
      {
        "type":"template",
        "payload":{
          "template_type":"button",
          "buttons":[
            {
              "type":"web_url",
              "url":"https:\/\/www.messenger.com\/",
              "title":"Visit Messenger"
            }
          ]
        }
      }
    ]
  }
}
```

### Properties

### `message.attachments`

Property | Type | Description || `type` | String | `template` |
| `payload` | String | Template payload as described in the [Send API Reference](/docs/messenger-platform/send-api-reference#request) |

Note that in the case of a `payload` with attachments, the attachment id sent is a number not a string. See [example 2](#example_2)

This does not match the format of [Send API](/docs/messenger-platform/send-api-reference#request) that needs the attachment id to be sent as a string.

## Message with fallback attachment

A fallback attachment is any attachment not currently recognized or supported by the Message Echo feature.

### Example

```
{
  "sender":{
    "id":"<PAGE_ID>"
  },
  "recipient":{
    "id":"<PSID>"
  },
  "timestamp":1458696618268,
  "message":{
    "is_echo":true,
    "app_id":1517776481860111,
    "metadata": "<DEVELOPER_DEFINED_METADATA_STRING>",
    "mid":"mid.1458696618141:b4ef9d19ec21086067",
    "attachments":[
      {
        "title":"Legacy Attachment",
        "url":"https:\/\/www.messenger.com\/",
        "type":"fallback",
        "payload":null
      }
    ]
  }
}
```

### Properties

### `message.attachments`

Property | Type | Description || `type` | String | `fallback` |
| `title` | String | Title of attachment (optional) |
| `url` | String | URL of attachment (optional) |
| `payload` | String | Payload of attachment (optional) |

## Message with products

Message with products echo webhook is only available on Graph API v8.0+

App will need to have [`catalog_management`](https://developers.facebook.com/docs/permissions/reference/catalog_management) permission approved to receive product details in webhooks.

### Example

```
{
  "sender":{
    "id":"<PAGE_ID>"
  },
  "recipient":{
    "id":"<PSID>"
  },
  "timestamp":1458696618268,
  "message":{
    "is_echo":true,
    "app_id":1517776481860111,
    "metadata": "<DEVELOPER_DEFINED_METADATA_STRING>",
    "mid":"mid.1458696618141:b4ef9d19ec21086067",
    "attachments":[
      {
        "type":"template",
        "payload":{
          "product":{
             "elements":[ // multiple elements for Hscroll
               {
                 "id":"<PRODUCT_ID>",
                 "retailer_id":"<EXTERNAL_ID>",
                 "image_url":"https://fb.cdn.com/sdsd",
                 "title":"Some product title",
                 "subtitle": "40",
               },
               {...},
             ]
            }

          ]
        }
      }
    ]
  }
}
```

### Properties

### `product.elements`

Property | Type | Description || `id` | String | Product ID from [product catalog](https://developers.facebook.com/docs/marketing-api/catalog/overview) |
| `retailer_id` | String | External ID that is associated with the Product. (ex: SKU/ Content ID) |
| `image_url` | String | URL of product image |
| `title` | String | Title of product |
| `subtitle` | String | Subtitle of product |

## Message which is a reply to another message

A fallback attachment is any attachment not currently recognized or supported by the Message Echo feature.

### Example

```
{
  "sender":{
    "id":"<PAGE_ID>"
  },
  "recipient":{
    "id":"<PSID>"
  },
  "timestamp":1458696618268,
  "message":{
    "is_echo":true,
    "app_id":1517776481860111,
    "metadata": "<DEVELOPER_DEFINED_METADATA_STRING>",
    "mid":"mid.1458696618141:b4ef9d19ec21086067",
    "reply_to": {
      "mid": "QUOTED-MESSAGE-ID",
      "is_self_reply" : false  
     } 
   }
}
```

### Properties

### `message.reply_to`

Property | Type | Description || `mid` | String | Reference to the message id that this message is replying to |
| `is_self_reply` | Boolean | Indicates whether the message is a self reply or not. |

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)