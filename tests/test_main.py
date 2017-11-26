import logging
import logjson


def test_main():

    capture = []

    class FileLike(object):
        pass

    logging.info('hi %s %s!', 'you', 'there')

    try:
        1/0
    except:
        logging.exception('Something went %s wrong:', 'horribly')


    logging.info('blah', extra=dict(a=1, b=2))


    logger = logging.getLogger('blah')
    logger.warning('Just checking %s', 'hell yeah')

    log2 = logwrap(logger, aaa=1, bbb=2)
    log2.info('But does it work tho?')

    log3 = logwrap(log2, ccc=3, ddd=4)
    log3.info('And the wrapper?')
