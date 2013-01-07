import abc
from experimental.tools import timeexpressiontools
from experimental.tools.settingtools.PayloadCallbackMixin import PayloadCallbackMixin


class SettingLookupRequest(PayloadCallbackMixin):
    r'''Setting lookup request.

    Look up `attribute` setting active at `offset` in `voice_name`.

    Setting is assumed to resolve to a list or other iterable.

    Because of this setting lookup requests afford payload callbacks.

    Composers create concrete setting lookup request classes during specification.

    Composers create concrete setting lookup request classes with lookup methods.

    All lookup methods implement against ``OffsetExpression``.
    '''

    ### INITIALIZER ###

    __metaclass__ = abc.ABCMeta

    ### INITIALIZER ###

    @abc.abstractmethod
    def __init__(self, attribute, voice_name, offset, payload_callbacks=None):
        assert attribute in self.attributes, repr(attribute)
        assert isinstance(voice_name, str), repr(voice_name)
        assert isinstance(offset, timeexpressiontools.OffsetExpression)
        PayloadCallbackMixin.__init__(self, payload_callbacks=payload_callbacks)
        self._attribute = attribute
        self._voice_name = voice_name
        self._offset = offset

    ### READ-ONLY PUBLIC PROPERTIES ###

    @property
    def attribute(self):
        '''Setting lookup request attribute.

        Return string.
        '''
        return self._attribute

    @property
    def start_segment_identifier(self):
        '''Delegate to ``self.offset.start_segment_identifier``.

        Return string or none.
        '''
        return self.offset.start_segment_identifier

    @property
    def offset(self):
        '''Setting lookup request offset.

        Return offset expression.
        '''
        return self._offset

    @property
    def voice_name(self):
        '''Setting lookup request voice name.

        Return string.
        '''
        return self._voice_name

    ### PRIVATE METHODS ###
    
    @abc.abstractmethod
    def _get_payload(self, score_specification=None, voice_name=None):
        pass
