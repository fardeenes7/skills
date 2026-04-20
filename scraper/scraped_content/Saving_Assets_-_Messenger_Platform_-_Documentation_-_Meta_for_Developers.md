# Saving Assets - Messenger Platform - Documentation - Meta for Developers

Source: https://developers.facebook.com/docs/messenger-platform/send-messages/saving-assets

# Saving Assets

To optimize sending assets, you may optionally have the Messenger Platform save an asset when it is sent. This is useful if you plan on sending the same attachments repeatedly, since it eliminates the need to upload an asset with each request.

The Messenger Platform offers two APIs that allow you to save assets for later use: the [Send API](#send_api), and the [Attachment Upload API](#attachment_upload_api). Both APIs support saving assets from URL and from your local file system.

### Contents

* [Supported Asset Types](#asset_types)
* [Saving with the Send API](#send_api)
  + [Saving from URL](#send_api_url)
  + [Saving from File](#send_api_file)
  + [API Response](#send_api_response)
* [Saving with the Attachment Upload API](#attachment_upload_api)
  + [Saving from URL](#upload_api_url)
  + [Saving from File](#upload_api_file)
  + [API Response](#upload_api_response)
* [Sending Saved Assets](#using_attachment_id)

## Supported Asset Types

The Messenger Platform supports saving the following asset types, up to 25MB in size:

* image
* audio - `Content-Type` header must use type `audio`. For example, `audio/mp3`.
* video
* file

## Saving with the Send API

The Send API allows you to save an asset that is sent with a message, as an alternative to uploading it in advance with the [Attachment Upload API](#attachment_upload_api). To do this, send a `POST` request with `payload.is_reusable` set to `true` to the `/messages` endpoint.

### Saving from URL

To save an asset from a URL, specify the source URL in the `payload.url` property of the `attachment` object of your message:

```
{
  "recipient":{
    "id":"<PSID>"
  },
  "message":{
    "attachment":{
      "type":"<ASSET_TYPE>", 
      "payload":{
        "url":"<ASSET_URL>",
        "is_reusable": true
      }
    }
  }
}
```

For a complete list of API calls and request properties, see the [Send API Reference](/docs/messenger-platform/reference/send-api/).

### Saving from File

To save an asset from your local file system, submit your message request to the Send API as form data, and specify the file location in the `filedata` field of the request:

```
curl  \
  -F 'recipient={"id":"<PSID>"}' \
  -F 'message={"attachment":{"type":"<ASSET_TYPE>", "payload":{"is_reusable":true}}}' \
  -F 'filedata=@/tmp/shirt.png;type=image/png' \
  "https://graph.facebook.com/v25.0/me/messages?access_token=<PAGE_ACCESS_TOKEN>"
```

For a complete list of API calls and request properties, see the [Send API Reference](/docs/messenger-platform/reference/send-api/).

### API Response

The response will contain an `attachment_id` that can be [used to attach the asset to future messages](#using_attachment_id). Please note that this ID is private and only the page that originally sent the attachment can reuse it.

```
{
  "recipient_id": "1254444444682919",
  "message_id": "m_AG5Hz2Uq7tuwNEhXfYYKj8mJEM_QPpz5jdCK48PnKAjSdjfipqxqMvK8ma6AC8fplwlqLP_5cgXIbu7I3rBN0P",
  "attachment_id": "687799999980546"
}
```

## Saving with the Attachment Upload API

The Attachment Upload API allows you to upload assets in advance. This is useful if you know in advance that you will need to send particular assets repeatedly. To do this, send a `POST` request to the `/message_attachments` endpoint.

For a complete list of API calls and request properties, see the [Attachment Upload API Reference](/docs/messenger-platform/reference/attachment-upload-api/).

### Saving from URL

To save an asset from a URL, specify the source URL in the `payload.url` property of the `attachment` object of your message:

```
curl --location --request POST 'https://graph.facebook.com/v2.10/me/message_attachments?access_token=<PAGE_ACCESS_TOKEN>' \
--header 'Content-Type: application/json' \
--data-raw '{
  "message":{
    "attachment":{
      "type":"image", 
      "payload":{
        "url":"http://www.messenger-rocks.com/image.jpg",
        "is_reusable": true
      }
    }
  }
}'
```

For a complete list of API calls and request properties, see the [Attachment Upload API Reference](/docs/messenger-platform/reference/attachment-upload-api/).

### Saving from File

To save an asset from your local file system, submit your message request to the Attachment Upload API as form data, and specify the file location in the `filedata` field of the request:

```
curl  \
  -F 'recipient={"id":"<PSID>"}' \
  -F 'message={"attachment":{"type":"<ASSET_TYPE>", "payload":{"is_reusable":true}}}' \
  -F 'filedata=@/tmp/shirt.png;type=image/png' \
  "https://graph.facebook.com/v25.0/me/messages?access_token=<PAGE_ACCESS_TOKEN>"
```

### API Response

The response will contain an `attachment_id` that can be [used to attach the asset to future messages](#using_attachment_id). Please note that this ID is private and only the page that originally sent the attachment can reuse it.

```
{
  "attachment_id":"1857777774821032"
}
```

## Sending Saved Assets

Once you have an `attachment_id` for your saved asset, you can use it to attach the asset to a message. For more information, see [Sending Messages - Attaching Saved Assets](/docs/messenger-platform/send-messages#attachment_reuse).

### Developer Support

* Use the [Meta Status tool](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F&h=AT4g8QgXjWWEHYYzL0tyK36kHF1E9vQ-1zGTQLy7WjkYXUIT5uJWhv4SfQy5kVrgOuVh26YL8E5m6zpUgZb-8go2gAR5VgM22mNOlFyOSruKRUbuy49KpJGKDSfD8RQYfKkGyXV0ryxh4uBs) to check for the status and outages of Meta business products.
* Use the [Meta Developer Support tool](/support) to report bugs and view reported bugs, get help with Ads or Business Manager, and more.

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)