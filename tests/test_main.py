import logging
import logjson
import json


def test_main():

    capture = []

    class FileLike(object):
        def write(self, data):
            capture.append(data)

    logger = logging.getLogger('blah')
    logger.addHandler(logjson.JSONHandler(stream=FileLike()))

    logger.info('hi %s %s!', 'you', 'there')

    print(capture)
    assert capture

    d = json.loads(capture[0])

    assert d['message'] == "hi you there!"
    assert d['name'] == "blah"





    # try:
    #     1/0
    # except:
    #     logging.exception('Something went %s wrong:', 'horribly')
    #
    #
    # logging.info('blah', extra=dict(a=1, b=2))
    #
    #
    # logger = logging.getLogger('blah')
    # logger.warning('Just checking %s', 'hell yeah')
    #
    # log2 = logwrap(logger, aaa=1, bbb=2)
    # log2.info('But does it work tho?')
    #
    # log3 = logwrap(log2, ccc=3, ddd=4)
    # log3.info('And the wrapper?')
