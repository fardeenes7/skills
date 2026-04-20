# Authentication & App Setup

## Meta App Configuration
To interact with the Messenger Platform, you must first create a Meta App.
- **Recommended Type**: **Business App**. This provides access to the necessary permissions for both Messenger and Instagram.
- **Product Setup**: Add the "Messenger" product in the App Dashboard.

## Permissions Reference
| Permission | Description |
| :--- | :--- |
| `pages_messaging` | Allows the app to send and receive messages from a Facebook Page. |
| `pages_show_list` | Allows the app to see the list of Facebook Pages that a person manages. |
| `pages_manage_metadata` | Required for subscribing to webhooks programmatically. |
| `instagram_manage_messages` | Required for sending and receiving messages on Instagram. |
| `page_utility_messaging` | Required for sending Utility (non-marketing) templates. |
| `marketing_messages_messenger` | Required for Recurring Notifications. |
| `business_management` | Often a dependency for business permissions like `pages_messaging`. |

## Access Tokens
The Messenger Platform uses multiple types of access tokens:

### 1. User Access Token
- Obtained via **Facebook Login**.
- Represents the user (admin of the Page).
- Short-lived (~1 hour) or Long-lived (~60 days).

### 2. Page Access Token
- Required for most Messenger Platform API calls.
- Obtained by calling `GET /{user-id}/accounts` with a User Access Token.
- Can be non-expiring if requested correctly.

### 3. System User Access Token
- Used by **Facebook Login for Business**.
- Never expires by default.
- Recommended for large-scale implementations and Marketing Message campaigns.

## Identity Scoping (PSID & IGSID)
- **PSID (Page-Scoped ID)**: Unique to a user per Facebook Page. If the same user messages two different Pages, they will have two different PSIDs.
- **IGSID (Instagram-Scoped ID)**: Unique to a user per Instagram Professional account.
- **SID (User-Scoped ID)**: Used in the Graph API but NOT for sending messages directly in Messenger. You must always use the scoped ID returned by webhooks.
