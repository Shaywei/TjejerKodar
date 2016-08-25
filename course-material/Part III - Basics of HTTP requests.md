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



