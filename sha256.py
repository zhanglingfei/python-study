import hashlib
import hmac


def stringtomd5(originstr):
    signaturemd5 = hashlib.sha256().encode("utf-8")
    signaturemd5.update(originstr)
    return signaturemd5.hexdigest()

def jm_sha256(key, value):
    """
    sha256加密
    :param key:
    :param value: 加密字符串
    :return: 加密结果转换为16进制字符串，并大写
    """
    hsobj = hashlib.sha256(key.encode("utf-8"))
    hsobj.update(value.encode("utf-8"))
    return hsobj.hexdigest().upper()


def jm_sha256_single(value):
    """
    sha256加密
    :param value: 加密字符串
    :return: 加密结果转换为16进制字符串，并大写
    """
    hsobj = hashlib.sha256()
    hsobj.update(value.encode("utf-8"))
    return hsobj.hexdigest().upper()


def jm_md5(key, value):
    """
    md5加密
    :param key:
    :param value: 加密字符串
    :return: 加密结果转换为16进制字符串，并大写
    """
    hsobj = hashlib.md5(key.encode("utf-8"))
    hsobj.update(value.encode("utf-8"))
    return hsobj.hexdigest().upper()


def jm_md5_singlt(value):
    """
    md5加密
    :param value: 加密字符串
    :return: 加密结果转换为16进制字符串，并大写
    """
    hsobj = hashlib.md5()
    hsobj.update(value.encode("utf-8"))
    return hsobj.hexdigest().upper()


def hmac_sha256(key, value):
    """
    hmacsha256加密
    :param key:
    :param value: 加密字符串
    :return: 加密结果转换为16进制字符串，并大写
    """
    message = value.encode("utf-8")
    return hmac.new(key.encode("utf-8"), message, digestmod=hashlib.sha256).hexdigest().upper()


def hmac_sha256_single(value):
    """
    hmacsha256加密
    :param value: 加密字符串
    :return: 加密结果转换为16进制字符串，并大写
    """
    message = value.encode("utf-8")
    return hmac.new(message, digestmod=hashlib.sha256).hexdigest().upper()


def hmac_md5(key, value):
    """
    hmacmd5加密
    :param key:
    :param value: 加密字符串
    :return: 加密结果转换为16进制字符串，并大写
    """
    message = value.encode("utf-8")
    return hmac.new(key.encode("utf-8"), message, digestmod=hashlib.md5).hexdigest().upper()


def hmac_md5_single(value):
    """
    hmacmd5加密
    :param value: 加密字符串
    :return: 加密结果转换为16进制字符串，并大写
    """
    message = value.encode("utf-8")
    return hmac.new(message, digestmod=hashlib.md5).hexdigest().upper()


if __name__ == '__main__':

    print("sha256加密：", jm_sha256_single("zhan.gsan"))

