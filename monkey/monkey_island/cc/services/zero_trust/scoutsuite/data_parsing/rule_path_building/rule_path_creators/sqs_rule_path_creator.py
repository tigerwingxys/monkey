from monkey_island.cc.services.zero_trust.scoutsuite.consts.rule_names.sqs_rules import SQSRules
from monkey_island.cc.services.zero_trust.scoutsuite.consts.service_consts import SERVICE_TYPES
from monkey_island.cc.services.zero_trust.scoutsuite.data_parsing.rule_path_building.abstract_rule_path_creator import \
    AbstractRulePathCreator


class SQSRulePathCreator(AbstractRulePathCreator):

    service_type = SERVICE_TYPES.SQS
    supported_rules = SQSRules
