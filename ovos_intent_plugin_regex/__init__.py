import re

from ovos_plugin_manager.templates.intents import IntentExtractor


class RegexExtractor(IntentExtractor):
    keyword_based = False
    regex_entity_support = True

    def calc_intent(self, utterance, min_conf=0.0):
        utterance = utterance.strip().lower()
        for name, patterns in self.patterns.items():
            for pattern in patterns:
                match = pattern.match(utterance)
                if match:
                    return {'conf': 1.0,
                            'intent_type': name,
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
