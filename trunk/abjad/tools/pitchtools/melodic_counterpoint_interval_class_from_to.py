from abjad.tools.pitchtools.melodic_diatonic_interval_from_to import \
   melodic_diatonic_interval_from_to


def melodic_counterpoint_interval_class_from_to(pitch_carrier_1, pitch_carrier_2):
   '''.. versionadded:: 1.1.2

   Return melodic counterpoint interval class from `pitch_carrier_1` to
   `pitch_carrier_2`. ::

      abjad> pitchtools.melodic_counterpoint_interval_class_from_to(NamedPitch(-2), NamedPitch(12))
      MelodicCounterpointIntervalClass(+2)

   ::

      abjad> pitchtools.melodic_counterpoint_interval_class_from_to(NamedPitch(12), NamedPitch(-2))
      MelodicCounterpointInterval(-2)
   '''

   ## get melodic diatonic interval
   mdi = melodic_diatonic_interval_from_to(pitch_carrier_1, pitch_carrier_2)
  
   ## return melodic counterpoint interval class
   return mdi.melodic_counterpoint_interval.interval_class
