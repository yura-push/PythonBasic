def hash_tag_creator2(string_var: str) -> str:
    if len(string_var) <= 0:
        raise ValueError("empty string")

    return "#" + (string_var.title()).replace(" ", "") if len(string_var) < 140 else False


print(hash_tag_creator2(""))
