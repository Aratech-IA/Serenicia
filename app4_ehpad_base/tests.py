import time
import unittest

from app4_ehpad_base.models import Photos


#ajouter décoration @timeit devant une fonction pour chronométrer le temps d'execution
def timeit(f):
    def timed(*args, **kw):
        ts = time.time()
        result = f(*args, **kw)
        te = time.time()

        print('func:%r args:[%r, %r] took: %2.4f sec' % \
              (f.__name__, args, kw, te - ts))
        return result

    return timed


class app4_ehpad_baseTests(unittest.TestCase):
    def test_photos_count(self):
        count = Photos.objects.count()
        self.assertLessEqual(count, 5, msg='Vérifier websocket multiple face reco')
