from parsimonious import Grammar

knit_grammar = Grammar(r"""
    pattern = cast_on? (row "\n")*
    cast_on = "CO" count "\n"
    row = "Row " count ":" stitch_list
    stitch_list = stitch_group ("," stitch_group)*
    stitch_group = simple_stitch / repeat_stitch
    simple_stitch = stitch_kind count stitch_scope?
    repeat_stitch = "(" stitch_list ")" repeat_count
    repeat_count = count / "twice"
    stitch_kind = "p" / "k" / "sl" / "yo" / "ssk" / "sk2p"
    stitch_scope = "tog" / "psso" / "pnso"
    count = ~"[0-9]"+
""")

def human_readable__pattern(pattern):
    knit_grammar.parse(example)
    return "foo"

example = open('example.k').read()

assert human_readable__pattern(example) == (
    """
    Row 1: knit 10, purl 10
    Row 2: kint 15, purl 5
    """)

# http://zderadicka.eu/writing-simple-parser-in-python/
