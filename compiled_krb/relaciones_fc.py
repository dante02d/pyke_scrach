# relaciones_fc.py

from __future__ import with_statement
from pyke import contexts, pattern, fc_rule, knowledge_base

pyke_version = '1.1.1'
compiler_version = 1

def novios(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('parejas', 'novios', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('parejas', 'relacion',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),
                        rule.pattern(2).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def amantes(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('parejas', 'amantes', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('parejas', 'relacion',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),
                        rule.pattern(2).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def populate(engine):
  This_rule_base = engine.get_create('relaciones')
  
  fc_rule.fc_rule('novios', This_rule_base, novios,
    (('parejas', 'novios',
      (contexts.variable('novio'),
       contexts.variable('novia'),),
      False),),
    (contexts.variable('novio'),
     contexts.variable('novia'),
     pattern.pattern_literal('novios'),))
  
  fc_rule.fc_rule('amantes', This_rule_base, amantes,
    (('parejas', 'amantes',
      (contexts.variable('novio'),
       contexts.variable('novia'),),
      False),),
    (contexts.variable('novio'),
     contexts.variable('novia'),
     pattern.pattern_literal('amantes'),))


Krb_filename = '../relaciones.krb'
Krb_lineno_map = (
    ((13, 17), (3, 3)),
    ((18, 21), (5, 5)),
    ((30, 34), (9, 9)),
    ((35, 38), (11, 11)),
)
