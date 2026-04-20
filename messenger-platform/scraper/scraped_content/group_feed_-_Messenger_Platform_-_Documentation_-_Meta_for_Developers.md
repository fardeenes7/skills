# group_feed - Messenger Platform - Documentation - Meta for Developers

Source: https://developers.facebook.com/docs/messenger-platform/reference/webhook-events/group-feed

# `group_feed`

This guide shows you the webhook notification properties sent when a person comments on a post, published as the business' Facebook Page, in your business' Facebook Group.

To receive webhooks for private replies, the group settings for private replies must be on. Private replies are **On** by default. To confirm this setting, the admin of the Facebook Page can go to the Facebook Group, tap **Manage** in the left panel and scroll down to **Settings**. Tap **Group settings**, scroll down to **Manage discussion** and look for **On** under **Private replies**.

The `group_feed` field for
[the Page topic webhooks
![](https://scontent.fdac31-2.fna.fbcdn.net/v/t39.2365-6/310307727_3347317042262105_1088877051262827250_n.png?_nc_cat=107&ccb=1-7&_nc_sid=e280be&_nc_ohc=Z7ccbX1p3loQ7kNvwHiQSsW&_nc_oc=AdocFmbfze0Zj9pfOimB6lf4-mmboYtmd9R6Nmn6CUn2pNEytDZIu-0vwvXkqALuTYM&_nc_zt=14&_nc_ht=scontent.fdac31-2.fna&_nc_gid=Jk7yr7o3ScMe6yvfT91jVw&_nc_ss=7a30f&oh=00_Af2H9IXfnV8mVChrRf4Z7YWAOGCDyVUBrv9mUd_w4EHx5w&oe=6A003862)](https://developers.facebook.com/docs/graph-api/webhooks/reference/page/)
returns information about comments published by a person on your business' Facebook Group. With this information you can privately reply to the person who published the comment.

### Example Webhooks Notification

The following is an example webhook notification sent to your server when a person comments on a post in a business' Facebook group.

```
[
  {
    "object": "page",
    "entry": [
      {
        "time": 1680575902263,
        "id": "PAGE-ID",
        "messaging": [
          {
           "recipient": {
              "id": "PAGE-ID"
            },
            "from": {
              "id": "USER-ID",
              "name": "Cinderella Hoover"
            },
            "group_id": "GROUP-ID",
            "comment_id": "COMMENT-ID",
            "parent_id": "PARENT-ID",
            "post_id": "POST-ID",
            "created_time": 1680575789,
            "item": "comment",
            "verb": "add",
            "message": "Does this shirt come in blue?",
            "field": "group_feed"
          }
        ],
        "hop_context": null
      }
    ]
  }
]
```

## Messaging Properties

The following `messaging` properties are included in the webhooks notification.

Property Name | Description || `comment_id` | The ID for the comment made by a person on a business' Facebook group post |
| `created_time` | The time the update was made |
| `field` | The value `group_feed` for the Page messaging webhook |
| `group_id` | The ID for the Facebook group where the post or comment was published |
| `item` | The value for the item published in the Facebook group is `comment` |
| `message` | The text of the comment made by the person |
| `post_id` | The ID for the post that the person commented on |
| `parent_id` | The ID for the parent post or comment to which the reply was made |
| `recipient` | The field representing ID for the Facebook Page for the business that owns or administers the Facebook Group |
| `from` | The field representing ID and name of the person that commented on business' Facebook group post |
| `verb` | The action take that triggered the webhook. The value `add` is the action for publishing comment in the group |

## See Also

* Find more [messaging webhooks fields](https://developers.facebook.com/docs/graph-api/webhooks/reference/page) that your app should subscribe to.
* Learn how to [set up your server to accept](https://developers.facebook.com/docs/messenger-platform/webhooks) Webhooks notifications from Meta.

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)