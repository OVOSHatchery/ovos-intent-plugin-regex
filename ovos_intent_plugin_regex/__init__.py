from ovos_plugin_manager.templates.pipeline import IntentPipelinePlugin, RegexIntentDefinition, IntentMatch
from ovos_utils import classproperty


class RegexPipelinePlugin(IntentPipelinePlugin):

    # plugin api
    @classproperty
    def matcher_id(self):
        return "regex"

    def match(self, utterances, lang, message):
        return self.calc_intent(utterances, lang=lang)

    def train(self):
        # no training step needed
        return True

    # implementation
    def calc_intent(self, utterance, min_conf=0.0, lang=None):
        lang = lang or self.lang
        utterance = utterance.strip().lower()
        for intent in (e for e in self.registered_intents
                       if e.lang == lang and isinstance(e, RegexIntentDefinition)):
            for pattern in intent.patterns:
                match = pattern.match(utterance)
                if match:
                    data = {'conf': 1.0,
                            'intent_type': intent.name,
                            'entities': match.groupdict(),
                            'utterance': utterance,
                            'utterance_remainder': "",
                            'intent_engine': 'regex'}

                    return IntentMatch(intent_service=self.matcher_id,
                                       intent_type=intent.name,
                                       intent_data=data,
                                       confidence=1.0,
                                       utterance=utterance,
                                       skill_id=intent.skill_id)
        return None
