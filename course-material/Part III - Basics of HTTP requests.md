# HTTP

```
HTTP is the protocol that allows for sending documents back and forth on the web.
```

`HTTP` is the protocol that allows for sending documents back and forth on the web. A protocol is a set of rules that determines which messages can be exchanged, and which messages are appropriate replies to others. Another common protocol is POP3, which you might use to fetch email on your hard disk.

In HTTP, there are two different roles: server and client. In general, the client always initiates the conversation; the server replies. HTTP is text based; that is, messages are essentially bits of text, although the message body can also contain other media. Text usage makes it easy to monitor an HTTP exchange.

HTTP messages are made of a header (or headers) and a body. The body can often remain empty; it contains data that you want to transmit over the network, in order to use it according to the instructions in the header. The header contains metadata, such as encoding information; but, in the case of a request, it also contains the important HTTP methods.


## HTTP Verbs

Each request specifies a certain `HTTP` method in the request header. This is the first all caps word in the request header. For instance,

`GET / HTTP/1.1`  

means the `GET` method is being used, while  

`DELETE /clients/anne HTTP/1.1`  

means the `DELETE` method is being used.  


`HTTP` methods tell the server what to do with the data identified by the URL.

`HTTP` methods tell the server what to do with the data identified by the URL. The request can optionally contain additional information in its body, which might be required to perform the operation - for instance, data you want to store with the resource.

If you've ever created HTML forms, you'll be familiar with two of the most important `HTTP` methods: `GET` and `POST`. But there are far more `HTTP` methods available. The most important ones for interacting with RESTful APIs are `GET`, `POST`, `PUT` and `DELETE`.

Other methods are available, such as `HEAD` and `OPTIONS`, but they are more rare.

### `GET`

`GET` is the simplest type of `HTTP` request method; the one that browsers use each time you click a link or type a URL into the address bar.

It instructs the server to transmit the data identified by the URL to the client. For example:

`GET /clients`  

Might give us a list of clients while:

`GET /clients/robin`  

Might give us details about the client 'robin'


Data should never be modified on the server side as a result of a `GET` request (`GET` request is "read-only").

### `PUT`

A `PUT` request is used when you wish to create or update the resource identified by the URL. For example:

`PUT /clients/robin`  

might create a client, called Robin on the server.  
`PUT` requests contain the data to use in updating or creating the resource in the body.

### `DELETE`

`DELETE` should perform the contrary of `PUT`; it should be used when you want to delete the resource identified by the URL of the request.

`DELETE /clients/anne`

This will delete all data associated with the resource, identified by `/clients/anne`.

### `POST`

`POST` is used when the processing you wish to happen on the server should be repeated, if the `POST` request is repeated.  

In addition, `POST` requests should cause processing of the request body as a subordinate of the URL you are posting to.

Often, `POST` requests are used to trigger operations on the server, which do not fit into the Create/Update/Delete paradigm;

## URL Parameters ([Query String](https://en.wikipedia.org/wiki/Query_string))

A typical URL containing a query string is as follows:

`http://example.com/over/there?name=ferret`

* The query string is composed of a series of field-value pairs.
* Within each pair, the field name and value are separated by an equals sign, `=`.
* The series of pairs is separated by the ampersand, `&`.

#### URL Encoding

Some characters cannot be part of a `URL` (for example, the SPACE) and some other characters have a special meaning in a URL: for example, the characters `?`, `&` and `=`

The URI generic syntax uses URL encoding to deal with this problem, while `HTML` forms make some additional substitutions rather than applying percent encoding for all such characters.

For example, SPACE is encoded as `+` or `%20`.

You can see more examples [here](https://en.wikipedia.org/wiki/Percent-encoding).

## `HTTP` client - `cURL`

`cURL` (or just `curl` if you're lazy) is a nifty, easy-to-use tool for making `HTTP` requests from the command prompt 
If you're using Mac / Linux - you have it installed already :)
If you're using Windows, you'll have to download `cURL`.
You can download it [here](https://curl.haxx.se/download.html) (Scroll to the bottom of the list).

* Verify that you can `curl www.example.com` and get a boring `html` doc:

```
shayweiss@ ~/git/ $ curl www.example.com
<!doctype html>
<html>
<head>
    <title>Example Domain</title>

    <meta charset="utf-8" />
    <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <style type="text/css">
    body {
        background-color: #f0f0f2;
        margin: 0;
        padding: 0;
        font-family: "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;
        
    }
    div {
        width: 600px;
        margin: 5em auto;
        padding: 50px;
        background-color: #fff;
        border-radius: 1em;
    }
    a:link, a:visited {
        color: #38488f;
        text-decoration: none;
    }
    @media (max-width: 700px) {
        body {
            background-color: #fff;
        }
        div {
            width: auto;
            margin: 0 auto;
            border-radius: 0;
            padding: 1em;
        }
    }
    </style>    
</head>

<body>
<div>
    <h1>Example Domain</h1>
    <p>This domain is established to be used for illustrative examples in documents. You may use this
    domain in examples without prior coordination or asking for permission.</p>
    <p><a href="http://www.iana.org/domains/example">More information...</a></p>
</div>
</body>
</html>
```

* Super short [curl tutorial](https://gist.github.com/joyrexus/85bf6b02979d8a7b0308)

### Excercise: Let's play with making simple API calls

#### Deploy a silly local server

1. Download this [silly server](../scripts/silly_server.py)
2. Make sure you have all the dependency to run it in an activated `virtualenv`
3. Open a command-prompt  and run it `python silly_server.py` (You need to `cd` to the directory first)

#### "Documentation" for the `silly server` API

The server is holding a list of silly things.  
When you deploy the server (step 3 above) it will run in [`localhost`](https://en.wikipedia.org/wiki/Localhost) on port `8080`.  

Here is how you interact with it:

1. You can list all the silly things with a `GET` request to `/silly` endpoint. Open a browser and put `http://localhost:8080/silly` in the address bar or alternatively run `curl http://localhost:8080/silly` from the command prompt
2. You can add things to the list. The server offers two different ways to do this (try them both!):
  * You can do a `PUT` request to `/silly/<new_item>`  
  **Bonus:** To experience URL encoding, try to add an item with a space in the name this way)
  * You can do a `POST` request to `/silly/add` - you'll need to send a request body with a `json` (dictionary). The json should have a key called `new_item` and the value for that key is the new item you wish to add.  
  **Q:** What happens if what you send is not a dictionary or a dictionary without the `new_item` key?

  After adding new items, list all the items again to verify that the items have been added.
3. You can delete things from the list. The server offers two different ways to do this (try them both!):
  * You can do a `DELETE` request to `/silly/<item_to_delete>`
  * You can delete with a `POST` request to `/silly/delete`. But this time, instead of a request body, the server expect a *URL parameter*. There are two different type of items you can supply:  
    * `item_name` and the name of the item.
    * `item_index` and the number of the item in the list

  **Q:** What happens if you give a wrong name, an index that doesn't exist, or doesn't supply a parameter?
