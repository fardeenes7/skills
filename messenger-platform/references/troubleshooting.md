# Troubleshooting, Policy, and Operations

## Common Error Codes
| Code | Subcode | Typical Meaning | Suggested Action |
| :--- | :--- | :--- | :--- |
| `10` | `2534022` | Messaging window/policy restriction | Use valid tag/token path or wait for user re-engagement. |
| `100` | `2018001` | No matching user found | Verify PSID belongs to the same Page + app context. |
| `190` | `-` | Invalid/expired OAuth token | Refresh or regenerate the Page token; validate scope. |
| `200` | `-` | Permission error | Confirm app mode/review status and granted permissions. |
| `613` | `-` | Rate limit reached | Apply retry with backoff and queue shaping. |
| `551` | `-` | User blocked Page | Suppress sends to that user. |
| `100` | `2018109` | Attachment too large | Reduce file size and retry. |

## Reliability Practices
1. **Deduplicate events** using `mid` + idempotency handling.
2. **Allowlist domains** for webview/extensions via Messenger Profile.
3. **Version consciously** against current Graph API versions.
4. **Return webhook `200 OK` quickly** and process asynchronously.
5. **Track delivery/read lifecycle** using `message_deliveries` and `message_reads`.

## Policy and Compliance Checks
- Enforce 24-hour standard messaging boundaries.
- Use Message Tags only for approved use cases.
- Keep records for consent/token-based outbound paths (marketing and notification flows).
- Ensure automated experience disclosure where legally required.
- Review developer/platform policy notices in Page Support Inbox and act before enforcement deadlines.

## FAQ-Style Debugging Shortcuts
- **Webhook not arriving**: verify both webhook configuration and Page subscription state.
- **Invalid ID / no user found**: check PSID scope and token/Page pairing.
- **Multiple bots on one Page**: use handover protocol + standby channel handling.
- **One-time/recurring notification confusion**: confirm token lifecycle and consent webhook capture.

## Support and Escalation Paths
- **Meta Status**: https://metastatus.com/
- **Graph API Explorer**: https://developers.facebook.com/tools/explorer/
- **Developer Support + Bug Reporting**: Meta developer support surfaces.
- **Developer Community Forum / FAQ resources**: for known issues and implementation patterns.

## Operational Monitoring Notes
- Monitor outbound/inbound latency and availability trends.
- Alert on webhook retry spikes, signature failures, and opt-in token state transitions.
- Keep runbooks for policy restriction notices and token outage response.
