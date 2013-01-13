from experimental.tools.settingtools.SingleContextSetting import SingleContextSetting


class SingleContextTimeSignatureSetting(SingleContextSetting):
    r'''Single-context time signature setting.
    '''

    ### INITIALIZER ###

    def __init__(self, request=None, anchor=None, context_name=None, fresh=True, persist=True):
        SingleContextSetting.__init__(self, attribute='time_signatures', request=request, 
            anchor=anchor, context_name=context_name, fresh=fresh, persist=persist)

    ### PUBLIC METHODS ###

    def to_command(self, score_specification, voice_name):
        '''Change single-context time signature setting to command.

        Return command.
        '''
        from experimental.tools import settingtools
        anchor_timespan = score_specification.get_anchor_timespan(self, voice_name)
        command = settingtools.TimeSignatureRegionCommand(
            self.request, self.context_name, anchor_timespan, fresh=self.fresh)
        return command

    def make_time_signatures(self, score_specification):
        time_signatures = self.request._get_payload(score_specification)
        if time_signatures:
            segment_specification = score_specification.get_start_segment_specification(self.anchor)
            segment_specification._time_signatures = time_signatures[:]
            return time_signatures
