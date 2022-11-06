import rsa
def generate_keys():
    pubKey, privKey = rsa.newkeys(1024)
    pubKey = pubKey.save_pkcs1('PEM')
    privKey = privKey.save_pkcs1('PEM')
    #print(pubKey,privKey)
    return pubKey,privKey

def load_keys(pubKey,prevKey):
    pubKey = rsa.PublicKey.load_pkcs1(pubKey)
    privKey = rsa.PrivateKey.load_pkcs1(privKey)
    return pubKey,privKey

#pubKey,privKey = generate_keys()
#load_keys(pubKey,privKey)

