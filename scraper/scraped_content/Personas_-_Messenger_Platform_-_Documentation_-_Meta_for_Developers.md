# Personas - Messenger Platform - Documentation - Meta for Developers

Source: https://developers.facebook.com/docs/messenger-platform/send-messages/personas

# Messenger Platform Business Personas

![](https://scontent.fdac31-2.fna.fbcdn.net/v/t39.8562-6/121089976_357625862251555_8378917411301979428_n.png?_nc_cat=104&ccb=1-7&_nc_sid=f537c7&_nc_ohc=7wjoHBLmwwMQ7kNvwFrWQ0y&_nc_oc=Adq9Juo71V8y_5_tyaNK1H4At4dlrXdvK1y6vgSga8P2cvysabrXaa2LvLxVmwIMrLQ&_nc_zt=14&_nc_ht=scontent.fdac31-2.fna&_nc_gid=afXqgTmqZt2fdoeLm5hgPA&_nc_ss=7a30f&oh=00_Af0CsHoDV_BrsyigJ6w3zNp0708HMUC9F27kno0jV0PnEA&oe=69EBEB75)

The Messenger Platform allows you to create and manage personas for your business messaging experience. The persona may be backed by a human agent or a bot. A persona allows conversations to be passed from bots to human agents seemlessly. When a persona is introduced into a conversation, the persona's profile picture will be shown and all messages sent by the persona will be accompanied by an annotation above the message that states the persona name and business it represents.

"Adam from Jasper's Market"

#### Best Practices

* The `name` of a persona is freeform, but a first name and last name or initial, such as "John Z.", is recommended
* The Page name is still shown at the top of the conversation when using a persona. It is not necessary to include the company name in the `name` field.
* The persona should not be overly generic.
* The persona should be clearly distinguished from the Page/bot itself
* The persona should not attempt to deceive the recipient
* A persona can be created quickly. It is not necessary to sync your entire database of agents in advance

### Before You Start

You will need the following:

* A Page access token requested by someone who can perform the `MESSAGING` task on the Page
* The Page ID
* The `pages_messaging` permission
* A profile picture for your persona uploaded to the Meta servers. The image size may not exceed 8MB

## Create a Persona

To create a persona, send a `POST` request to the `/PAGE-ID/personas` endpoint with the `name` and `profile_picture_url` parameters set for the persona.

#### Sample Request

*Formatted for readability.*

```
curl -i -X POST "https://graph.facebook.com/PAGE-ID/personas
    ?name=Adam 
    &profile_picture_url=https://www.facebook.com/photo.php/fbid/adam-image.jpg
    &access_token=PAGE-ACCESS-TOKEN"
```

#### Sample Response

Upon success, your app will receive the following JSON response:

```
{
    "id": "PERSONA-ID"
}
```

## Get a List of Personas

To get a list of a Page's personas, including the name and profile picture for each, send a `GET` request to the `PAGE-ID/PERSONA-ID` endpoint:

#### Sample Request

*Formatted for readability.*

```
curl -i -X GET "https://graph.facebook.com/LATEST-API-VERSION/PAGE-ID/personas?access_token=PAGE-ACCESS-TOKEN"
```

#### Sample Response

Upon success, your app will receive the following JSON response:

```
{
  "data": [
    {
      "name": "Adam",
      "profile_picture_url": "https://facebook.com/adam-image.jpg",
      "id": "PERSONA-A-ID"
    },
    {
      "name": "David Mark",
      "profile_picture_url": "https://facebook.com/david-image.jpg",
      "id": "PERSONA-B-ID"
    },
  ],
  "paging": {
    "cursors": {
      "before": "QVFIUlMtR2ZATQlRtVUZALUlloV1",
      "after": "QVFIUkpnMGx0aTNvUjJNVmJUT0Yw"
    }
  }
}
```

### Get a Specific Persona

To retrieve all the personas associated with a Page, send a `GET` request to the `/PAGE-ID/personas` endpoint:

#### Sample Request

*Formatted for readability.*

```
curl -i -X GET "https://graph.facebook.com/LATEST-API-VERSION/PERSONA-ID
    ?access_token=PAGE-ACCESS-TOKEN"
```

#### Sample Response

Upon success, your app will receive the following JSON response:

```
{
     "name": "Adam",
     "profile_picture_url": "https://facebook.com/adam-image.jpg",
     "id": "PERSONA-ID"
}
```

## Send a Message as a Personas

To send a message as a Persona, send a `POST` request to the `PAGE-ID/messages` endpoint with the `persona_id` parameter with the `recipient` and `message` parameters.

#### Sample Request

*Formatted for readability.*

```
curl -i -X POST https://graph.facebook.com/LATEST-API-VERSION/PAGE-ID/messages
  ?recipient={ "id":"PSID" }
  &message={ "text":"Hello world!" }
  &persona_id=PERSONA-ID
  &access_token=PAGE-ACCESS-TOKEN"
```

If `persona_id` is not included, the message will be sent using the Page's ID.

### Sender Actions

You can add the typing indicator for the persona to show that actions are being taken by the persona. Only `typing_on` and `typing_off` sender actions are supported for personas.

To add the typing indicator as a Persona in the conversation, send a `POST` request to the `/PAGE-ID/messages` endpoint with the `persona_id` parameter.

#### Sample Request

*Formatted for readability.*

```
curl -i -X POST "https://graph.facebook.com/LATEST-API-VERSION/PAGE-ID/messages
  ?recipient={ 'id':'PSID' }
  &sender_action=typing_on
  &persona_id=PERSONA-ID
  &access_token=PAGE-ACCESS-TOKEN"
```

## Deleting a Persona

To delete a persona, send a `DELETE` request to the `/PERSONA-ID` endpoint.

#### Sample Request

*Formatted for readability.*

```
curl -X DELETE "https://graph.facebook.com/LATEST-API-VERSION/PERSONA-ID
    ?access_token=PAGE-ACCESS-TOKEN"
```

Messages previously sent by this persona will continue to appear in the chat history of the thread. Once deleted, a persona will no longer be able to send new messages.

#### Sample Response

Upon success, your app will receive the following JSON response:

```
{
    "success": true
}
```

## Learn More

### Developer Support

* Use the [Meta Status tool](https://l.facebook.com/l.php?u=https%3A%2F%2Fmetastatus.com%2F&h=AT7CzxwRFpBcY_PHPB0GAPvcsm0sH-hyZjNo_3yU3wLcWCmov1e--Q7tUOIYe35CtGLb-kLAQbaG0bmj9lb-VdfIb0ZlpN2DciKi9JOa7qOTd4xCKa0T5HjpT2bu18IrOo2HGku5wUkWkkVu) to check for the status and outages of Meta business products.
* Use the [Meta Developer Support tool](/support) to report bugs and view reported bugs, get help with Ads or Business Manager, and more.

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)