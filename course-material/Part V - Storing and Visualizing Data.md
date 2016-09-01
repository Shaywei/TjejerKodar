# Part IV - Storking and Visualzing Data

Now that we know how to get data from APIs, let's see if we can learn something from it!

## Easy Storing / Visualizing Data - ElasticSearch + Kibana

* Introduce [ElasticSearch](http://www.elasticsearchtutorial.com/elasticsearch-in-5-minutes.html)
* [ElasticSearch Basics](http://www.elasticsearchtutorial.com/basic-elasticsearch-concepts.html)

### [Our own ElasticSearch + Kibana cluster](http://e96fa10a742c3940012549683e3eed67.us-east-1.aws.found.io:9200) (This will only exist until the 13th of September 2016)
* Credentials will be given in class
* Download the [Sense](https://chrome.google.com/webstore/detail/sense-beta/lhjgkmllcaadmopgmanpapmpjgmfcfig?hl=en) extension to your browser for easy `curl`-ing. Short demo in class

### Visualizing Data stored in ES - Kibana

* [Our `Kibana 4`](https://fb4013b216d5ff2a1abe9492768619e1.us-east-1.aws.found.io/app/kibana) frontend
* Useful to visualize data in the cluster (short demo)

### Basics of data storing

* [Indices](https://www.elastic.co/guide/en/elasticsearch/reference/current/indices.html)
  * Data in ES is **immutable**
* [Mapping](https://www.elastic.co/guide/en/elasticsearch/reference/current/mapping.html)
  * Show example with @timestamp and explain the importance of that for visualizing!
  * Explain about [Unix timestamp (Epoch)](https://en.wikipedia.org/wiki/Unix_time), a useful [converter](http://www.epochconverter.com/)
* [Queries](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl.html)

## Lets store and visualize some data!

* Walk through the [Tweeter Dump script](../scripts/twitter-es-dump/tweeter_es_dump.py)

?Maybe work with the Slack API and put each message that was sent to slack into ES with some fields. Then visualize how many messages each user had / how many words each user had etc'?
?Maybe something with FB API?
?Maybe try to see how "random" is the Python random() method?

TBD
