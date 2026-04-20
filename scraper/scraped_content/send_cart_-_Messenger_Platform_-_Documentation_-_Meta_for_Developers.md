# send_cart - Messenger Platform - Documentation - Meta for Developers

Source: https://developers.facebook.com/docs/messenger-platform/reference/webhook-events/send_cart

# `send_cart` Webhook Event Reference

This callback will occur when a message containing cart information has been sent to your Page. Messages are always sent in order.

You can subscribe to this callback by selecting `send_cart` when [setting up](/docs/messenger-platform/webhook-reference#setup) your webhook.

## Example

```
{
  "sender": {
    "id": "<PSID>"
  },
  "recipient": {
    "id": "<PAGE_ID>"
  },
  "timestamp": 1458692752478,
  "order": {
    "products": [
      {
        "id": 123,
        "retailer_id": "retailer_id_1",
        "name": "name1",
        "unit_price": 11,
        "currency": "THB",
        "quantity": 1,
      },
      {
        "id": 456,
        "retailer_id": "retailer_id_2",
        "name": "name2",
        "unit_price": 22,
        "currency": "THB",
        "quantity": 2,
      },
    ],
    "note": "foobar",
  }
}
```

## Properties

### `sender`

`sender` Field | Description || `id` *string* | The Page-scoped ID for the person who sent a message to your business |

### `recipient`

`recipient` Field | Description || `id` *string* | The ID for your Facebook Page |

### `order`

Property | Type | Description || `products` | Array<`product`> | Array containing product data |
| `note` | String | Optional note about the order |

### `order.products`

Property | Type | Description || `id` | String | Product ID from [Facebook product catalog](https://developers.facebook.com/docs/marketing-api/catalog/overview) |
| `retailer_id` | String | External ID that is associated with the Product (for example, SKU/Content ID) |
| `name` | String | Product name |
| `unit_price` | Float | Numeric price per unit |
| `currency` | String | Currency short string (for example, USD) |
| `quantity` | Int | The count of this product in the order |

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)