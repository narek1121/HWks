def safe_copy(src, dst):
    try:
        with open(src, encoding="utf-8") as f_in, open(dst, "w", encoding="utf-8") as f_out:
            f_out.write(f_in.read())
        return True
    except FileNotFoundError:
        return False
