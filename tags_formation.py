def hash_tag_creator(string_var: str) -> str:
    try:
        hash_tag_var = "#" + (string_var.title()).replace(" ", "") if len(string_var) < 140 else False
        if len(string_var) == 0 or len(hash_tag_var) == 0:
            raise ValueError("empty string")
        else:
            return hash_tag_var
    except ValueError as exc:
        print(exc)


print(hash_tag_creator(" hash tag   creator  "))
