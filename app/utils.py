import hashlib, string

BASE62_ALPHABETS = string.digits + string.ascii_lowercase + string.ascii_uppercase

def base62_encode(num: int) -> str:
    """Convert a number to base62 string"""
    if num == 0:
        return BASE62_ALPHABETS[0]
    encoded = []
    base = len(BASE62_ALPHABETS)
    while num > 0:
        num, remainder = divmod(num, base)
        encoded.append(BASE62_ALPHABETS[remainder])
    return "".join(reversed(encoded))

def link_to_slug(link: str, length: int = 7) -> str:
    """Generate a slug usiing a URL"""
    digest = hashlib.md5(link.encode("utf8")).hexdigest()
    num = int(digest[:15], 16)
    encoded = base62_encode(num)

    return encoded[:length]

