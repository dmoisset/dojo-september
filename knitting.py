from parsimonious import Grammar

knit_grammar = Grammar(r"""
    pattern = (row "\n")*
    row = stitch_group ("," stitch_group)*
    stitch_group = stitch_kind count
    stitch_kind = "p" / "k"
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