from flask import (
    Blueprint, request, jsonify, json, abort
)

bp = Blueprint('api', __name__)

bp.OfferDB = [

    {

        'id': '1',

        'name': 'Jerzy Knapik',

        'title': 'Napiszę książkę',

        'dsc' : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam cursus, lectus ac maximus accumsan, nulla diam ultricies augue, nec efficitur erat enim at ipsum. Sed. '

    },

    {

        'id': '2',

        'name': 'Jerzy Olchowicz',

        'title': 'Zrobię naleśniki',

        'dsc': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam arcu nisl, dictum in cursus et, condimentum sit amet dui. Nulla commodo lacus vel nisl commodo. '

    }

]


@bp.route('/')
def index():
    return jsonify({'APP/API': "DPP-JMETER API"})


@bp.route('/timeBank-1.0/offers/save', methods=['POST'])
def saveDB():
    file = open("offers.txt", "w")
    json.dump(bp.OfferDB, file)
    file.close()
    return jsonify({'Result': "Saved"})


@bp.route('/timeBank-1.0/offers/load', methods=['POST'])
def loadDB():
    try:
        file = open("offers.txt", "r")
    except FileNotFoundError:
        return jsonify({'Result': "Error (No file found to load)"})
    bp.OfferDB = json.load(file)
    print(bp.OfferDB)
    file.close()
    return jsonify({'Result': "Loaded"})


@bp.route('/timeBank-1.0/offer', methods=['GET'])
def getAllOffer():
    return jsonify({'offers': bp.OfferDB})


@bp.route('/timeBank-1.0/offer/<offerID>', methods=['GET'])
def getOffer(offerID):
    off = [Offer for Offer in bp.OfferDB if (Offer['id'] == offerID)]

    return jsonify({'offer': off})


@bp.route('/timeBank-1.0/offer/<offerID>', methods=['PUT'])
def updateOffer(offerID):
    off = [Offer for Offer in bp.OfferDB if (Offer['id'] == offerID)]

    if 'name' in request.json:
        off[0]['name'] = request.json['name']

    if 'title' in request.json:
        off[0]['title'] = request.json['title']

    if 'dsc' in request.json:
        off[0]['dsc'] = request.json['dsc']

    return jsonify({'offer': off[0]})


@bp.route('/timeBank-1.0/offer', methods=['POST'])
def createOffer():

    off = [Offer for Offer in bp.OfferDB if (Offer['id'] == request.json['id'])]

    if len(off) != 0:
        return jsonify({'Error': 'User with this id exists'})

    dat = {

        'id': request.json['id'],

        'name': request.json['name'],

        'title': request.json['title'],

        'dsc': request.json['dsc']

    }

    bp.OfferDB.append(dat)

    return jsonify(dat)


@bp.route('/timeBank-1.0/offer/<offerID>', methods=['DELETE'])
def deleteOffer(offerID):
    off = [Offer for Offer in bp.OfferDB if (Offer['id'] == offerID)]

    if len(off) == 0:
        abort(404)

    bp.OfferDB.remove(off[0])

    return jsonify({'response': 'Success'})
