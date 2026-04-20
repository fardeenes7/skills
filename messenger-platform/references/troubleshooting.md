# Troubleshooting & Error Codes

## Common Error Codes

| Code | Subcode | Message | Solution |
| :--- | :--- | :--- | :--- |
| **10** | **2534022** | Outside allowed window | Use a Message Tag or wait for user to message first. |
| **100** | **2018001** | No matching user found | Ensure the PSID is for the correct Page and app. |
| **190** | **-** | Invalid OAuth access token | Refresh the Page Access Token; check for expiry. |
| **200** | **-** | Permission error | Ensure the app is Live or user has a Role on the app. |
| **613** | **-** | Rate limit reached | Implement exponential backoff. Formula: 200 * MAU. |
| **551** | **-** | User block error | User has blocked the Page. You cannot send messages. |
| **100** | **2018109** | Attachment too large | Reduce file size below 25MB. |

## Best Practices for Stability
1. **Deduplication**: Use `mid` in webhooks to ignore retries.
2. **Domain Allowlisting**: Always allowlist your domain via `POST /me/messenger_profile` to enable Webview/Extensions.
3. **App Review**: Ensure all required permissions (`pages_messaging`, etc.) are approved for Live usage.
4. **Graph API Versioning**: Use the latest version (e.g., `v25.0`) to avoid using deprecated fields.

## Status Checks
- [Meta Status Page](https://metastatus.com/)
- [Graph API Explorer](https://developers.facebook.com/tools/explorer/)
