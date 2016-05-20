# encoding=utf8
import qrcode
import easygui
import webbrowser
import os
import hashlib

from wox import Wox, WoxAPI

PKG_DIR = os.path.dirname(os.path.realpath(__file__))
DEFAULT_RESULT = {
    'Title': '输入需要转换成二维码的内容，然后回车！',
    'SubTitle': 'Powered by ousui',
    'IcoPath': 'images/ico.png',
    'JsonRPCAction': {
        'method': '_openUrl',
        'parameters': ['http://github.com/ousui']
    }
}


class Qrcode(Wox):
    def _openUrl(self, url):
        webbrowser.open(url)

    def _openDialog(self, content, path):
        easygui.msgbox(content, '二维码', '确定', image=path)

    def _genBarcode(self, content):
        md5 = hashlib.md5(bytes(content, 'utf-8')).hexdigest()
        path = os.path.join(PKG_DIR, 'images', 'qrcodes', '{}.png'.format(md5))
        # 是否存在这个md5文件，如果有直接返回结果，如果没有则生成
        if os.path.isfile(path):
            return path
        qrcode.make(content).save(path)
        return path

    def query(self, query):
        results = []
        if query.strip() == '':
            results.append(DEFAULT_RESULT)
        else:
            path = self._genBarcode(query.strip())
            results.append({
                'Title': query.strip(),
                'SubTitle': path,
                'IcoPath': path,
                'JsonRPCAction': {
                    'method': '_openDialog',
                    'parameters': [query.strip(), path],
                    'DontHideAfterAction': True
                }
            })

        return results


if __name__ == "__main__":
    # 启动时清理上次生成的 qrcode
    Qrcode()
