# -*- coding:utf-8 -*-
# Made by Kei Choi(hanul93@gmail.com)

import os # ���� ������ ���� import
import hashlib # MD5 �ؽø� ���� import

#---------------------------------------------------------------------
# KavMain Ŭ����
# Ű�޹�� ���� ������� ��Ÿ���� Ŭ�����̴�.
# �� Ŭ������ ������ ��� ���� Ŀ�� ��⿡�� �ε����� �ʴ´�.
#---------------------------------------------------------------------
class KavMain :
    #-----------------------------------------------------------------
    # scan(self, filehandle, filename)
    # �Ǽ��ڵ带 �˻��Ѵ�.
    # ���ڰ� : filehandle - ���� �ڵ�
    #        : filename   - ���� �̸�
    # ���ϰ� : (�Ǽ��ڵ� �߰� ����, �Ǽ��ڵ� �̸�, �Ǽ��ڵ� ID)
    #-----------------------------------------------------------------
    def scan(self, filehandle, filename) :
        try : # ��� ������ ������ �����ϱ� ���� ���� ó���� ���� 
            fp = filehandle # ���� �ڵ��� fp�� ����

            fp.seek(0) # ���� �����͸� ���� ������ �̵�
            buf = fp.read(68) # 68 Byte�� ����
            if len(buf) == 68 : # buf�� 68 Byte�� ������?
                md5 = hashlib.md5() # MD5 �ؽø� ����
                md5.update(buf)
                f_md5 = md5.hexdigest()

                eicar_pattern = '44d88612fea8a8f36de82e1278abb02f'

                if f_md5 == eicar_pattern :  # ������ �������� ��
                    return True, 'EICAR Test', 0 # �´ٸ� �˻� ����� �̸�, ID�� ����
        except : # ��� ���ܻ����� ó��
            pass
        
        return False, '', -1

    #-----------------------------------------------------------------
    # disinfect(self, filename, malwareID)
    # �Ǽ��ڵ带 ġ���Ѵ�.
    # ���ڰ� : filename   - ���� �̸�
    #        : malwareID  - ġ���� �Ǽ��ڵ� ID
    # ���ϰ� : �Ǽ��ڵ� ġ�� ����
    #-----------------------------------------------------------------
    def disinfect(self, filename, malwareID) : # �Ǽ��ڵ� ġ��
        try :
            # �Ǽ��ڵ� ���� ������� ���� ID ���� 0�ΰ�?
            if malwareID == 0 : 
                os.remove(filename) # ���� ����
                return True # ġ�� �Ϸ� ����
        except :
            pass

        return False # ġ�� ���� ����

    #-----------------------------------------------------------------
    # listvirus(self)
    # ����/ġ�� ������ �Ǽ��ڵ��� ����� �˷��ش�.
    #-----------------------------------------------------------------
    def listvirus(self) :
        vlist = [] # ����Ʈ�� ���� ����
        vlist.append('EICAR Test') # �����ϴ� �Ǽ��ڵ� �̸� ���
        return vlist

    #-----------------------------------------------------------------
    # getinfo(self)
    # ��� ���� ����� �ֿ� ������ �˷��ش�. (����, ������...)
    #-----------------------------------------------------------------
    def getinfo(self) :
        info = {} # ������ ���� ����
        info['author'] = 'Kei Choi' # ������
        info['version'] = '1.0'     # ����
        info['title'] = 'EICAR Test Engine' # ���� ����
        return info