from parsimonious import Grammar

knit_grammar = Grammar(r"""
    pattern = cast_on? (row "\n")*
    cast_on = "CO" count "\n"
    row = stitch_group ("," stitch_group)*
    stitch_group = stitch_kind count stitch_scope?
    stitch_kind = "p" / "k" / "sl st" / "yo"
    stitch_scope = "tog" / "psso" / "pnso"
    count = ~"[0-9]"+
""")

def human_readable__pattern(pattern):
    knit_grammar.parse(example)
    return "foo"

example = open('example.k').read()

assert human_readable__pattern(example) == (
    """
    knit 10, purl 10
    kint 15, purl 5
    """)

# http://zderadicka.eu/writing-simple-parser-in-python/
