from ovos_plugin_manager.intents import IntentExtractor, IntentPriority, RegexIntentDefinition, IntentDeterminationStrategy


class RegexExtractor(IntentExtractor):

    def __init__(self, config=None,
                 strategy=IntentDeterminationStrategy.SINGLE_INTENT,
                 priority=IntentPriority.REGEX_LOW,
                 segmenter=None):
        super().__init__(config, strategy=strategy,
                         priority=priority, segmenter=segmenter)
        self.patterns = {}  # lang: {name, patterns]

    def calc_intent(self, utterance, min_conf=0.0, lang=None, session=None):
        lang = lang or self.lang
        utterance = utterance.strip().lower()
        for intent in self.registered_intents:
            if intent.lang != lang:
                continue
            if not isinstance(intent, RegexIntentDefinition):
                continue
            for pattern in intent.patterns:
                match = pattern.match(utterance)
                if match:
                    return {'conf': 1.0,
                            'intent_type': intent.name,
                            'entities': match.groupdict(),
                            'utterance': utterance,
                            'utterance_remainder': "",
                            'intent_engine': 'regex'}
        return {'conf': 0,
                'intent_type': 'unknown',
                'entities': {},
                'utterance': utterance,
                'utterance_remainder': utterance,
                'intent_engine': 'regex'}
