# Advanced Features

## 1. Handover Protocol
Allows multiple apps to manage the same conversation (e.g., a Bot app and a Live Chat app).

### Roles
- **Primary Receiver**: Receives all webhooks by default. Usually the bot.
- **Secondary Receiver**: Receives `standby` webhooks. Usually the CRM/Live Chat.

### Protocol Actions
- **Pass Control**: `POST /me/pass_thread_control`.
- **Take Control**: `POST /me/take_thread_control`.
- **Request Control**: `POST /me/request_thread_control`.
- **Metadata**: You can pass custom strings (e.g., user intent) during handovers.

---

## 2. Marketing Messages (Recurring Notifications)
Send messages outside the 24h window for marketing purposes.

### The Flow
1. **Request Opt-in**: Send a `notification_messages` template.
2. **Handle Opt-in**: Catch `messaging_optins` webhook to get the `notification_messages_token`.
3. **Send Message**: Use the token with the **Marketing Message API**.

### Onboarding Businesses
- **Flow 1**: Using Business Portfolio. Generates non-expiring tokens.
- **Flow 2**: Asset-based. Short-lived tokens.

---

## 3. Utility Messages
Non-promotional templates (e.g., account alerts, order updates).
- **Setup**: Must clone templates from the Meta Library to your Page.
- **Permission**: `page_utility_messaging`.
- **API**: `POST /<PAGE_ID>/messages` with `messaging_type: UTILITY`.

---

## 4. Personas
Virtual identities for your bot/agents.
- **Create**: `POST /me/personas`.
- **Attributes**: `name`, `profile_picture_url`.
- **Usage**: Include `persona_id` in any Send API call to change the avatar/name displayed to the user.

---

## 5. Persistent Menu
A fixed menu at the bottom of the chat for core navigation.
- **Config**: `POST /me/messenger_profile`.
- **Capabilities**: URLs, Postbacks, or Nested Menus.
