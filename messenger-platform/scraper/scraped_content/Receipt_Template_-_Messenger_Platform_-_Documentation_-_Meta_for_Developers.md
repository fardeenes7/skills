# Receipt Template  - Messenger Platform - Documentation - Meta for Developers

Source: https://developers.facebook.com/docs/messenger-platform/reference/templates/receipt

# Receipt Template Reference

![](https://scontent.fdac31-2.fna.fbcdn.net/v/t39.2365-6/23208289_889588377870772_7170760265053503488_n.png?_nc_cat=103&ccb=1-7&_nc_sid=e280be&_nc_ohc=NI4GJ7MbIjUQ7kNvwGXqFNL&_nc_oc=AdrV8AnWOENelXcxBZgbotsQEcskTB2_dcbrv7CGB0LG8MWuW6A68W3YB3bNcwC22Pc&_nc_zt=14&_nc_ht=scontent.fdac31-2.fna&_nc_gid=pXeHmdnFsHydUDk7WyHj1g&_nc_ss=7a30f&oh=00_Af3vMTx1wruIt_YPjNoi6CwuAIk6gawXFC9Hq7RIk2VwZw&oe=6A003074)

The receipt template allows you to send an order confirmation as a structured message. For implementation details, see [Receipt Template](/docs/messenger-platform/send-api-reference/receipt-template).

## Request URI

```
https://graph.facebook.com/v25.0/me/messages?access_token={PAGE_ACCESS_TOKEN}
```

## Example Request

```
curl -X POST -H "Content-Type: application/json" -d '{
  "recipient":{
    "id":"<PSID>"
  },
  "message":{
    "attachment":{
      "type":"template",
      "payload":{
        "template_type":"receipt",
        "recipient_name":"Stephane Crozatier",
        "order_number":"12345678902",
        "currency":"USD",
        "payment_method":"Visa 2345",        
        "order_url":"http://originalcoastclothing.com/order?order_id=123456",
        "timestamp":"1428444852",         
        "address":{
          "street_1":"1 Hacker Way",
          "street_2":"",
          "city":"Menlo Park",
          "postal_code":"94025",
          "state":"CA",
          "country":"US"
        },
        "summary":{
          "subtotal":75.00,
          "shipping_cost":4.95,
          "total_tax":6.19,
          "total_cost":56.14
        },
        "adjustments":[
          {
            "name":"New Customer Discount",
            "amount":20
          },
          {
            "name":"$10 Off Coupon",
            "amount":10
          }
        ],
        "elements":[
          {
            "title":"Classic White T-Shirt",
            "subtitle":"100% Soft and Luxurious Cotton",
            "quantity":2,
            "price":50,
            "currency":"USD",
            "image_url":"http://originalcoastclothing.com/img/whiteshirt.png"
          },
          {
            "title":"Classic Gray T-Shirt",
            "subtitle":"100% Soft and Luxurious Cotton",
            "quantity":1,
            "price":25,
            "currency":"USD",
            "image_url":"http://originalcoastclothing.com/img/grayshirt.png"
          }
        ]
      }
    }
  }
}' "https://graph.facebook.com/v25.0/me/messages?access_token=<PAGE_ACCESS_TOKEN>"
```

## Example Response

```
{
  "recipient_id": "1254477777772919",
  "message_id": "AG5Hz2Uq7tuwNEhXfYYKj8mJEM_QPpz5jdCK48PnKAjSdjfipqxqMvK8ma6AC8fplwlqLP_5cgXIbu7I3rBN0P"
}
```

## Properties

### `recipient`

Description of the message recipient. All requests must include one of the following properties to identify the recipient.

Property | Type | Description || `recipient.id` | String | Page Scoped User ID (PSID) of the message recipient. The user needs to have interacted with any of the [Messenger entry points](/docs/messenger-platform/product-overview/entry-points) in order to opt-in into messaging with the Page. Note that [Facebook Login](/docs/facebook-login) integrations return user IDs are app-scoped and will not work with the Messenger platform. |
| `recipient.user_ref` | String | Used for the [checkbox plugin](/docs/messenger-platform/discovery/checkbox-plugin) |
| `recipient.post_id` | String | Used for [Private Replies](https://developers.facebook.com/docs/messenger-platform/discovery/private-replies) to reference the visitor post to reply to. |
| `recipient.comment_id` | String | Used for [Private Replies](https://developers.facebook.com/docs/messenger-platform/discovery/private-replies) to reference the post comment to reply to. |

### `message`

Description of the message to be sent.

Property | Type | Description || `message.attachment` | Object | An object describing attachments to the message. |

### `message.attachment`

Property | Type | Description || `type` | String | Value must be `template` |
| `payload` | Object | [`payload`](#payload) of the template. |

### `message.attachment.payload`

Property | Type | Description || `template_type` | String | Value must be `receipt`. |
| `sharable` | Boolean | ***Optional.*** Set to `true` to enable the native share button in Messenger for the template message. Defaults to `false`. |
| `recipient_name` | String | The recipient's name. |
| `merchant_name` | String | ***Optional.*** The merchant's name. If present this is shown as logo text. |
| `order_number` | String | The order number. Must be unique. |
| `currency` | String | The currency of the payment. |
| `payment_method` | String | The payment method used. Providing enough information for the customer to decipher which payment method and account they used is recommended. This can be a custom string, such as, "Visa 1234". |
| `timestamp` | String | ***Optional.*** Timestamp of the order in seconds. |
| `elements` | Array<[element](#elements)> | ***Optional.*** Array of a maximum of 100 [`element`](#elements) objects that describe items in the order. Sort order of the elements is not guaranteed. |
| `address` | [`address`](#address) object | ***Optional.*** The shipping address of the order. |
| `summary` | Object | The payment summary. See [`summary`](#summary). |
| `adjustments` | Array<[`adjustment`](#adjustments)> | ***Optional.*** An array of [payment](#adjustments) objects that describe payment adjustments, such as discounts. |

### `message.attachment.payload.address`

Property | Type | Description || `street_1` | String | The street address, line 1. |
| `street_2` | String | ***Optional.*** The street address, line 2. |
| `city` | String | The city name of the address. |
| `postal_code` | String | The postal code of the address. |
| `state` | String | The state abbreviation for U.S. addresses, or the region/province for non-U.S. addresses. |
| `country` | String | The two-letter country abbreviation of the address. |

### `message.attachment.payload.summary`

The property values of the `summary` object should be valid, well-formatted decimal numbers, using '`.`' (dot) as the decimal separator. Please note that most currencies only accept up to 2 decimal places.

Property | Type | Description || `subtotal` | Number | ***Optional.*** The sub-total of the order. |
| `shipping_cost` | Number | ***Optional.*** The shipping cost of the order. |
| `total_tax` | Number | ***Optional.*** The tax of the order. |
| `total_cost` | Number | The total cost of the order, including sub-total, shipping, and tax. |

### `message.attachment.payload.adjustments`

Property | Type | Description || `name` | String | Required if the `adjustments` array is set. Name of the adjustment. |
| `amount` | Number | Required if the `adjustments` array is set. The amount of the adjustment. |

### `message.attachment.payload.elements`

Property | Type | Description || `title` | String | The name to display for the item. |
| `subtitle` | String | ***Optional.*** The subtitle for the item, usually a brief item description. |
| `quantity` | Number | ***Optional.*** The quantity of the item purchased. |
| `price` | Number | The price of the item. For free items, '0' is allowed. |
| `currency` | String | ***Optional.*** The currency of the item price. |
| `image_url` | String | ***Optional.*** The URL of an image to be displayed with the item. |

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)