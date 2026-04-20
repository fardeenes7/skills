# messaging_optins  - Messenger Platform - Documentation - Meta for Developers

Source: https://developers.facebook.com/docs/messenger-platform/reference/webhook-events/messaging_optins

# `messaging_optins` Webhook Event Reference

A Messaging Opt In Webhook Event is triggered when a person opts in to receiving Marketing Messages or taps on a Send to Messenger plugin.

When using the Send to Messenger plugin, the `optin.ref` parameter is set by the `data-ref` field on the "Send to Messenger" plugin. This field can be used by the developer to associate a click event on the plugin with a callback.

## Message Opt In Webhook Notification

Your app will receive opt in webhook notification when the following occurs:

* A person opts-in
* A person re-opts in by clicking the **Continue messages** button shown before the notification message token expires
* A person changes their opt in status, stopping notifications or resuming notifications

```
{
  "sender": {
    "id": "PSID",
  },
  "recipient": {
    "id": "PAGE-ID",
  },
  "timestamp": "TIMESTAMP",
  "optin": {
    "type": "notification_messages", 
    "payload": "ADDITIONAL-INFORMATION",
    "notification_messages_token": "NOTIFICATION-MESSAGES-TOKEN", 
    "notification_messages_frequency": "FREQUENCY",  
    "notification_messages_timezone": "TIMEZONE-ID",
    "token_expiry_timestamp": "TIMESTAMP",
    "user_token_status": "TOKEN-STATUS",  
    "notification_messages_status": "NOTIFICATION-STATUS",
    "title": "TITLE" 
    }
}
```

### `optin`

Property | Description || `payload` *string* | Additional information that you want to include in the webhooks notification |
| `title` *string* | The title displayed in the template |
| `notification_messages_token` *string* | The token that represents the person who opted in, with the specific topic and message frequency, that is used to send Marketing Messages |
| `notification_messages_frequency` *enum { `DAILY, WEEKLY, MONTHLY` }* | The value can be one of the following:   * **DAILY** - send 1 notification per 24 hour period for 6 months from opt in date * **WEEKLY** - send 1 notification per week for 9 months from the opt in date * **MONTHLY**  - send 1 notification per month for 12 months from the opt in date   (Removed in API v16) |
| `notification_messages_timezone` *string* | Timezone for the person receiving the message |
| `notification_messages_status` *enum { `STOP NOTIFICATIONS, RESUME NOTIFICATIONS` }* | **This field is present only when the user stops or resumes Marketing Messages.** The value can be one of the following:   * **STOP NOTIFICATIONS** - User has clicked "Stop these messages" * **RESUME NOTIFICATIONS** - User has clicked "Resume these messages" |
| `token_expiry_timestamp` *unix timestamp* | Date when the the notification message token expires |
| `type` *string* | Value must be `notification_messages` |
| `user_token_status` *enum { `REFRESHED, NOT_REFRESHED` }* | The value can be one of the following:   * **REFRESHED** - This is set when the user chooses to re opt-in to receiving Marketing Messages after the token has expired * **NOT\_REFRESHED** - Default value and is set when the user does not re opt-in to receiving Marketing Messages after the token has expired |

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)