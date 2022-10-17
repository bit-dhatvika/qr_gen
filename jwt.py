import python_jwt as jwt, jwcrypto.jwk as jwk
import datetime 


def get_jwt(lis):

    key = jwk.JWK.generate(kty='RSA', size=2048)
    payload = { 'sr': int(lis[0]), 'name':lis[1], 'pos': lis[2] };
    token = jwt.generate_jwt(payload, key, 'PS256', datetime.timedelta(days=5*365),jti_size=0)
    #header, claims = jwt.verify_jwt(token, key, ['PS256'])
    #for k in payload: assert claims[k] == payload[k]
    return token