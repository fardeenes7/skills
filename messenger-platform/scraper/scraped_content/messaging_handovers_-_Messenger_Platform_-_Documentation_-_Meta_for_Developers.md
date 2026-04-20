# messaging_handovers - Messenger Platform - Documentation - Meta for Developers

Source: https://developers.facebook.com/docs/messenger-platform/reference/webhook-events/messaging_handovers

# `messaging_handovers` Webhook Event Reference

The `messaging_handovers` webhook event is used to notify your webhook when certain actions are taken using the Messenger Platform's [handover protocol](/docs/messenger-platform/handover-protocol), including [pass thread control](/docs/messenger-platform/handover-protocol#pass_thread_control), [take thread control](/docs/messenger-platform/handover-protocol#take_thread_control), and [role change](/docs/messenger-platform/handover-protocol#app_roles) events.

For more information on the handover protocol, see [Handover Protocol](https://developers.facebook.com/docs/messenger-platform/handover-protocol).

### Contents

* [pass\_thread\_control](#pass_thread_control)
* [take\_thread\_control](#take_thread_control)
* [app\_roles](#app_roles)
* [request\_thread\_control](#request_thread_control)

## `pass_thread_control`

This callback will occur when thread ownership for a user has been passed to your application.

For details on implementing pass thread control, see [Pass Thread Control](/docs/messenger-platform/handover-protocol/pass-thread-control).

```
{
   "sender":{
      "id":"<PSID>"
   },
   "recipient":{
      "id":"<PAGE_ID>"
   },
   "timestamp":1458692752478,
   "pass_thread_control":{
      "previous_owner_app_id":"<previous_app_id or null (idle_mode)>",
      "new_owner_app_id":"123456789",
      "metadata":"Additional content that the caller wants to set"
   }
}
```

### Properties

### `sender`

`sender` Field | Description || `id` *string* | The Page-scoped ID for the person who sent a message to your business |

### `recipient`

`recipient` Field | Description || `id` *string* | The ID for your Facebook Page |

### `pass_thread_control`

Property | Type | Description || `new_owner_app_id` | String | App ID that thread control is passed to. |
| `previous_owner_app_id` | String | App ID that thread control is passed from. |
| `metadata` | String | Custom string specified in the API request. |

## `take_thread_control`

This callback will occur when thread ownership for a user has been taken away from your application.

For details on implementing take thread control, see [Take Thread Control](/docs/messenger-platform/handover-protocol/take-thread-control).

```
{
  "sender":{
    "id":"<PSID>"
  },
  "recipient":{
    "id":"<PAGE_ID>"
  },
  "timestamp":1458692752478,
  "take_thread_control":{
    "previous_owner_app_id":"123456789", //could be null if thread was in idle mode
    "new_owner_app_id": <new_app_id>,
    "metadata":"additional content that the caller wants to set"
  }
}
```

### Properties

### `sender`

`sender` Field | Description || `id` *string* | The Page-scoped ID for the person who sent a message to your business |

### `recipient`

`recipient` Field | Description || `id` *string* | The ID for your Facebook Page |

### `take_thread_control`

Property | Type | Description || `previous_owner_app_id` | String | App ID that thread control was taken from. |
| `new_owner_app_id` | String | App ID that thread control was given to. |
| `metadata` | String | Custom string specified in the API request. |

## `request_thread_control`

This callback will be sent to the Primary Receiver app when a Secondary Receiver app calls the [Request Thread Control API](/docs/messenger-platform/handover-protocol/request-thread-control). The Primary Receiver may then choose to honor the request and pass thread control, or ignore the request.

For details on implementing take thread control, see [Take Thread Control](/docs/messenger-platform/handover-protocol/request-thread-control).

```
{
  "sender":{
    "id":"<USER_ID>"
  },
  "recipient":{
    "id":"<PSID>"
  },
  "timestamp":1458692752478,
  "request_thread_control":{
    "requested_owner_app_id":123456789,
    "metadata":"additional content that the caller wants to set"
  }
}
```

### Properties

### `sender`

`sender` Field | Description || `id` *string* | The Page-scoped ID for the person who sent a message to your business |

### `recipient`

`recipient` Field | Description || `id` *string* | The ID for your Facebook Page |

### `request_thread_control`

Property | Type | Description || `requested_owner_app_id` | String | App ID of the Secondary Receiver that is requesting thread control. |
| `metadata` | String | Custom string specified in the API request. |

## `app_roles`

This callback will occur when a page admin changes the role of your application. An app can be assigned the roles of `primary_receiver` or `secondary_receiver`.

For information on assigning app roles, see [Assign App Roles](/docs/messenger-platform/handover-protocol/assign-app-roles).

```
{
  "recipient":{
    "id":"<PSID>"
  },
  "timestamp":1458692752478,
  "app_roles":{
    "123456789":["primary_receiver"]
  }
}
```

### Properties

### `sender`

`sender` Field | Description || `id` *string* | The Page-scoped ID for the person who sent a message to your business |

### `recipient`

`recipient` Field | Description || `id` *string* | The ID for your Facebook Page |

### `app_roles`

Property | Type | Description || `id` | String | Your Page ID. |

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)