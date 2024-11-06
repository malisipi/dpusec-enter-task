import hashlib;

def md5_hash_oluştur(obje:any) -> str:
    kodlanmış_obje = (str(obje).encode());
    return hashlib.md5(kodlanmış_obje).hexdigest();
