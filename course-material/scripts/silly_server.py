import json

import flask


app = flask.Flask(__name__)


silly_things = [
    "Sardine Ice-Cream", "The Patriarchy", "Pandas",
    "Violence", "The phrase: 'Goddag yxskaft'"]


@app.route('/')
def index():
    return "I am a silly server. I hold to silly things!"


@app.route('/silly', methods=['GET'])
def list_silly_thing():
    return json.dumps(
        {i: silly_things[i] for i in range(len(silly_things))},
        indent=4)


@app.route('/silly/<new_item>', methods=['PUT'])
def put_add_silly_thing(new_item):
    silly_things.append(new_item)
    return "I've added {} to the list of silly things!".format(new_item)


@app.route('/silly/add', methods=['POST'])
def post_add_silly_thing():
    data = flask.request.get_data()
    data_as_dict = json.loads(data)
    new_item = data_as_dict['new_item']
    silly_things.append(new_item)
    return "I've added {} to the list of silly things!".format(new_item)


@app.route('/silly/delete', methods=['POST'])
def post_delete_silly_thing():
    args = flask.request.args
    item_to_delete = None
    if args.get('item_name'):
        print 'blas'
        item_to_delete = args['item_name']
        silly_things.remove(item_to_delete)
    elif args.get('item_index'):
        item_to_delete = silly_things.pop(int(args['item_index']))
    else:
        raise Exception(
            'Please specify either "item_name" or "item_index" as '
            'a URL Parameter!')
    return "I've deleted {} from the list of silly things!".format(
        item_to_delete)


if __name__ == "__main__":
    app.run(port=8080, debug=True)
