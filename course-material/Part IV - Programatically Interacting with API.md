# Part IV - Programatically Interacting with API

So we've seen how we can use `curl` to talk to APIs, but how do we achieve similar results with Python code?  

## Introducing the `requests` library - "HTTP for Humans"

Comes with very good and easy to read [docs](http://docs.python-requests.org/en/master/)!

### [Mob Programming](https://en.wikipedia.org/wiki/Mob_programming) Exercise

Let's write, as a group (!) a Python script that does the following:

* Queries the `silly server` for a list of thigns
* Deletes all items in the list that start with `T`:
  * If the item is two words or less, it will use the `DELETE` method
  * If the item is three to four words, it will use the `POST` method with `item_name` parameter
  * If the item is five words or more, it will use the `POST` method with the `item_index` parameter
* For each remaining item, add a counter-item to the list which is the **reverse** of the item ("Pandas" --> "sadnaP"):
  * If the item starts with the letter Q or a letter that appears before it on the Alphabet, it uses the `PUT` method
  * Otherwise, it uses the `POST` method
  
Don't worry - we'll switch "driver" every few minutes :)


### Mini Project / Excersice

It's time to jump in to the water and learn how to swim (or suffer a terrible death by drowning)!

Let's create a service that you can query for an address and it will give you:

* The current [forecast](https://developer.forecast.io/docs/v2) for that location in the address
* A bunch of public [Instagram](https://www.instagram.com/developer/endpoints/media/) photos for the address
* A [static google map](https://developers.google.com/maps/documentation/static-maps/intro) of the address
* A [google maps streetview](https://developers.google.com/maps/documentation/streetview/intro) picture of the address

Since we are not doing a webdevelopment course, I will supply the code and a general explanation of the server part.  
But the hard part (which is up to you) is to add the functionality for interaction with the different APIs and manipulating the data to fit into the provided template.

#### Before we start

##### Authorization is a headache

In this part we'll:

* Intoduce the concept of authorization, access tokens and API keys
* Give examples of how to generate keys/tokens for the services we want to interact with:
  * [Forecast.io](https://developer.forecast.io/docs/v2)
  * [Googlemaps - static](https://developers.google.com/maps/documentation/static-maps/intro)
  * [Googlemaps - streetview](https://developers.google.com/maps/documentation/streetview/intro)
  * [Instagram](https://www.instagram.com/developer/endpoints/media/) - Is a real pain. After much headache though, I found [this](http://services.chrisriversdesign.com/instagram-token) which made life easy again.


##### Human readable address to `lat` `lon` pair

We want the users for the service to be able to just put in a simple address (for example: Barcelona, Spain).  
However, all the APIs above use `{lat,lon}` pairs...  
Personally, I have no idea how to translate one to other!  
Fortunately though.... [I don't have to!](http://lmgtfy.com/?q=python+address+to+lat+lon#)

##### Rundown for the server code

Let's go through the files / code we have to start with in the address_describe project folder in scripts.

* [The server](../scripts/address_describe/simple_flask_server.py)
* [The template](../scripts/address_describe/templates/address.html) (Not in the scope of the course)

##### Some possible hints for when you're stuck

* Are you running the server?  (Check in terminal)
* Are you running the server from the same code that you are editing?  (Maybe add a print statement and see if you actually see it when you run the server)
* Environment issues? (Are you getting `ImportError`s? Are you running within a `virtualenv`? What sort of modules do you have installed there?)

##### Get to work! ^_^
