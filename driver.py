from pyke import knowledge_engine,goal
import time

engine = knowledge_engine.engine(__file__)
fc_goal = goal.compile('parejas.relacion($person1, $person2,$relationship)')

def test(pareja):
    engine.reset()
    engine.activate('relaciones')
    with fc_goal.prove(engine,person1=pareja) as gen:
        for vars,plan in gen:
            print "%s, %s son %s" % (pareja,vars['person2'],vars['relationship'])
    engine.print_stats()
