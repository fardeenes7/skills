# Advanced Features

## 1) Handover Protocol (Multi-App Routing)
Allows multiple apps to manage one conversation thread.

### Roles
- **Primary Receiver**: receives messaging callbacks by default.
- **Secondary Receiver**: receives `standby` events when not thread owner.

### Control APIs
- **Pass Control**: `POST /me/pass_thread_control`
- **Take Control**: `POST /me/take_thread_control`
- **Request Control**: `POST /me/request_thread_control`
- Include metadata for routing context and CRM/bot handoff reasons.

---

## 2) Marketing Messages (Recurring Notifications)
Send marketing content outside the standard window with explicit user consent.

### Core Flow
1. Request opt-in using notification templates.
2. Capture `messaging_optins` webhook and token state.
3. Send via the Marketing Messages API using the issued token.

### Business Onboarding Modes
- **Business portfolio flow**: supports long-lived operational setups.
- **Asset-based flow**: often short-lived token patterns.

---

## 3) Utility Messages
Non-promotional templates such as account alerts and order updates.
- **Permission**: `page_utility_messaging`
- **API pattern**: utility messaging requests on Page message endpoints.
- Clone and manage approved templates before sending at scale.

---

## 4) Personas
Virtual sender identities for differentiated agent experiences.
- **Create**: `POST /me/personas`
- **Use**: include `persona_id` in Send API calls.

---

## 5) Messenger Profile API
Configure profile-level behavior for your Page messaging surfaces.
- Endpoint: `POST/GET/DELETE /me/messenger_profile`
- Common properties:
  - `get_started`
  - `greeting`
  - `ice_breakers`
  - `persistent_menu`
  - `whitelisted_domains`
  - `account_linking_url`
  - `commands`
- Practical note: profile writes are rate-limited per page.

---

## 6) Conversations API
Read and manage thread history across Messenger and Instagram Messaging contexts.
- List conversations: `GET /<PAGE_ID>/conversations?platform=...`
- Filter by person (`user_id`) to find specific threads.
- Read messages from conversation and fetch detailed message metadata.
- Ownership-aware processing can use fields like `is_owner` with conversation routing.

---

## 7) Persistent Menu and Account Linking Strategy
- Persistent menu improves evergreen navigation and escalation pathways.
- Account linking aligns external business identity to Messenger scoped users.
- Combine both with handover and profile controls to support bot + human hybrid systems.
