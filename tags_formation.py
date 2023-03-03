def hash_tag_creator(string_val: str) -> str:
    return "#" + (string_val.title()).replace(" ", "") if len(string_val) < 140 else False


print(hash_tag_creator(" Hello there thanks for trying my Kata Hello there thanks for trying my Kata"))
