Vim�UnDo� P�V��uue�b��G�7|͢�?o�Y'ku           if not os.path.exists(path):                              ]��    _�                             ����                                                                                                                                                                                                                                                                                                                                                             ]�FK    �                   5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        ]�F�     �                 	import os5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        ]�F�     �                 import datetime5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        ]�F�     �                 import feedparser       url = ""    5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        ]�F�     �                   5�_�      	                     ����                                                                                                                                                                                                                                                                                                                                                  V        ]�F�     �                 9                                os.popen('mkdir ' + path)   T                                        os.popen('wget -nc ' + link + ' -P ' + path)       8                                        download(path_t)   8                                        download(path_p)5�_�      
           	           ����                                                                                                                                                                                                                                                                                                                                                V       ]�F�     �               (            if not os.path.exists(path):5�_�   	              
           ����                                                                                                                                                                                                                                                                                                                                                V       ]�F�     �               $        if not os.path.exists(path):5�_�   
                         ����                                                                                                                                                                                                                                                                                                                                                V       ]�F�     �                 )                os.popen('mkdir ' + path)   D                        os.popen('wget -nc ' + link + ' -P ' + path)       (                        download(path_t)   (                        download(path_p)5�_�                           ����                                                                                                                                                                                                                                                                                                                                                  V        ]�F�     �               os.popen('mkdir ' + path)5�_�                            ����                                                                                                                                                                                                                                                                                                                                                V       ]�F�     �                   os.popen('mkdir ' + path)   0    os.popen('wget -nc ' + link + ' -P ' + path)5�_�                            ����                                                                                                                                                                                                                                                                                                                                                V       ]�F�     �               %            os.popen('mkdir ' + path)   8            os.popen('wget -nc ' + link + ' -P ' + path)5�_�                            ����                                                                                                                                                                                                                                                                                                                                                V       ]�F�     �                     download(path_t)       download(path_p)5�_�                            ����                                                                                                                                                                                                                                                                                                                                                V       ]�F�    �                Apath_p = '/smb/nhk/previous/' + YYYY + '-' + MM + '-' + DD + '/' 5�_�                           ����                                                                                                                                                                                                                                                                                                                                                V       ]�G    �   
            path_t = '/smb/nhk/today/'5�_�                           ����                                                                                                                                                                                                                                                                                                                                                v       ]�G    �               @path_p = '/smb/nhk/previous/' + YYYY + '-' + MM + '-' + DD + '/'�             5�_�                           ����                                                                                                                                                                                                                                                                                                                                                v       ]�G    �   
            $path_t = '/smb/ラジオ/nhk/today/'5�_�                           ����                                                                                                                                                                                                                                                                                                                                         $       v   !    ]�G#    �               Jpath_p = '/smb/ラジオ/nhk/previous/' + YYYY + '-' + MM + '-' + DD + '/'5�_�                           ����                                                                                                                                                                                                                                                                                                                                         $       v   !    ]�G&    �               Bpath_p = '/smb/ラジオ/nhk//' + YYYY + '-' + MM + '-' + DD + '/'5�_�                           ����                                                                                                                                                                                                                                                                                                                                         "       v       ]�G4   	 �   
            %path_t = '/smb/ラジオ/nhk/.today/'5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        ]��     �             �             5�_�                           ����                                                                                                                                                                                                                                                                                                                                                v       ]��     �               4        os.popen('wget -nc ' + link + ' -P ' + path)5�_�                           ����                                                                                                                                                                                                                                                                                                                                                v       ]��   
 �               ,        ('wget -nc ' + link + ' -P ' + path)5�_�                           ����                                                                                                                                                                                                                                                                                                                                                v       ]��    �               2        print ('wget -nc ' + link + ' -P ' + path)5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        ]��    �               4        os.popen('wget -nc ' + link + ' -P ' + path)   1        print('wget -nc ' + link + ' -P ' + path)5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        ]��     �               if not os.path.exists(path):5�_�                            ����                                                                                                                                                                                                                                                                                                                                                V       ]�F�     �               Fos.popen('mkdir ' + path) os.popen('wget -nc ' + link + ' -P ' + path)5�_�                           ����                                                                                                                                                                                                                                                                                                                               9          9       V   9    ]�F�     �               f                                os.popen('mkdir ' + path) os.popen('wget -nc ' + link + ' -P ' + path)5�_�                             ����                                                                                                                                                                                                                                                                                                                               9          9       V   9    ]�F�     �               f                                os.popen('mkdir ' + path) os.popen('wget -nc ' + link + ' -p ' + path)5��