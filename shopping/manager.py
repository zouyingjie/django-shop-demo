# -*- coding: utf-8 -*-
import json
import pickle
from django.conf import settings
from django.core.cache import cache




def set_cache_commidty(all_commoditys):
    cache.set('all_commoditys', pickle.dumps(all_commoditys))


def get_cache_commodity():
    return  pickle.loads(cache.get('all_commoditys'), encoding='utf-8')
def has_cache_commodity():
    return cache.has_key('all_commoditys')