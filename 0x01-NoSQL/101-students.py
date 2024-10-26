#!/usr/bin/env python3

""" Returns all students sorted by average score """


def top_students(mongo_collection):
    """ Returns all students sorted by average score """
    pipeline = [ { '$unwind': '$topics'},
                 { '$group': {'id': {'_id': '$_id',
                                     'name': '$name'},
                              'averageScore': {'$avg': '$topics.score'}
                              }
                   }
                 { '$project': {'_id': '$_id._id',
                                'name': '$_id.name',
                                'averageScore': '$averageScore'}
                   },
                 { '$sort': {'averageScore': -1}}
                 ]
    return list(mongo_collection.aggregate(pipeline))
