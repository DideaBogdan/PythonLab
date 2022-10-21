def validate_dict(rules, dictionary):
    for rule in rules:
        key, prefix, middle, suffix = rule
        text = dictionary.get(key)
        if text is None:
            return False
        if text.startswith(prefix) is False:
            return False
        if text.endswith(suffix) is False:
            return False
        if text.find(middle) < 0 or text.find(middle) > len(text) - len(middle)-1:
            return False
    return True


s = {("key1", "", "inside", ""), ("key2", "start", "middle", " ")}
d = {"key1": "come inside, it's too cold out", "key2": "start middle "}
print(validate_dict(s, d))
