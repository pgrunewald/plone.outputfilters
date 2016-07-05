import re
from zope.interface import implementer
from plone.outputfilters.interfaces import IFilter


@implementer(IFilter)
class EmDashAdder(object):
    order = 1000

    def __init__(self, context, request):
        pass

    def is_enabled(self):
        return True

    pattern = re.compile(r'--')

    def __call__(self, data):
        return self.pattern.sub('\xe2\x80\x94', data)
