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


