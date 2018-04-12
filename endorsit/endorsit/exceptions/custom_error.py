from logzero import logger

from .code import Code


class ServiceError(Exception):
    status = False

    # 自己定义了一个 return_code，作为更细颗粒度的错误代码
    def __init__(self, error_code=None, payload=None):
        Exception.__init__(self)
        if error_code is not None:
            self.error_code = error_code
        else:
            self.error_code = 100000
        self.payload = payload

    # 构造要返回的错误代码和错误信息的 dict
    def to_dict(self):
        rv = dict(self.payload or ())
        rv['status'] = self.status
        rv['error_code'] = self.error_code
        rv['error_msg'] = Code.msg[self.error_code]
        # 日志打印
        logger.warning(Code.msg[self.error_code])

        return rv
