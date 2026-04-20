# messaging_account_linking  - Messenger Platform - Documentation - Meta for Developers

Source: https://developers.facebook.com/docs/messenger-platform/reference/webhook-events/messaging_account_linking

# `messaging_account_linking` Webhook Event Reference

When using [Account Linking](/docs/messenger-platform/account-linking), this callback will occur when the [Link Account](/docs/messenger-platform/account-linking/link-account) or [Unlink Account](/docs/messenger-platform/account-linking/unlink-account) button have been tapped.

The `status` parameter tells you whether the user linked or unlinked their account. The `authorization_code` is a pass-through parameter. allowing you to match the business user entity to the page-scoped ID (PSID) of the `sender`.

### Example

```
{
  "sender":{
    "id":"USER_ID"
  },
  "recipient":{
    "id":"PAGE_ID"
  },
  "timestamp":1234567890,
  "account_linking":{
    "status":"linked",
    "authorization_code":"PASS_THROUGH_AUTHORIZATION_CODE"
  }
}
```

```
{
  "sender":{
    "id":"USER_ID"
  },
  "recipient":{
    "id":"PAGE_ID"
  },
  "timestamp":1234567890,
  "account_linking":{
    "status":"unlinked"
  }
}
```

## Properties

### `sender`

`sender` Field | Description || `id` *string* | The Page-scoped ID for the person who sent a message to your business |

### `recipient`

`recipient` Field | Description || `id` *string* | The ID for your Facebook Page |

### `account_linking`

Property | Description | Type || `status` | `linked` or `unlinked` | String |
| `authorization_code` | Value of pass-through `authorization_code` provided in the [Account Linking](/docs/messenger-platform/account-linking/link-account) flow | String |

Note: `authorization_code` is only available when `status` is `linked`

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)