# messaging_game_plays - Messenger Platform - Documentation - Meta for Developers

Source: https://developers.facebook.com/docs/messenger-platform/reference/webhook-events/messaging_game_plays

# `messaging_game_plays` Webhook Event Reference

This callback occurs after a person played a round of Instant Games. To receive this event, you must subscribe to this callback by selecting the `messaging_game_plays` field when [setting up](/docs/messenger-platform/webhook-reference#setup) your webhook.

```
{
  "sender": {
    "id": "PSID"
  },
  "recipient": {
    "id": "PAGE_ID"
  },
  "timestamp": 1469111400000,
  "game_play": {
    "game_id": "GAME-APP-ID",
    "player_id": "PLAYER-ID",
    "locale": "PLAYER-LOCALE",
    "context_type": "CONTEXT-TYPE:SOLO",
    "context_id": "CONTEXT-ID", # If a Messenger Thread context
    "score": SCORE-NUM, # If a classic score based game
    "payload": "PAYLOAD" # If a rich game
  }
}
```

## Fields

`sender` Field | Description || `id` *string* | The Page-scoped ID for the person who sent a message to your business |

`recipient` Field | Description || `id` *string* | The ID for your Facebook Page |

`game_play` Field | Description || `context_id` *string* | The ID for the social context type if the type is not `SOLO`. This ID is in the Instant Game namespace. |
| `context_type` *string* | The social context of the game; `GROUP`, `SOLO`, `THREAD` |
| `game_id` *string* | The Meta app ID for the game |
| `locale` *string* | The locale for the player |
| `payload` *JSON object* | The JSON encoded object, set using `FBInstant.setSessionData()`. Only available for Rich Games |
| `player_id` *string* | The ID for the player in the Instant Game namespace. |
| `score` *integer* | The best score achieved by this playing during this round of game play. Only available to Classic score based games. |

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)