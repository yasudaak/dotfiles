Vim�UnDo� ,d�9\��ZRF%���/��߄��qtb��u   y                 +       +   +   +    ]��    _�                            ����                                                                                                                                                                                                                                                                                                                                                             ]��5    �         �      dldir_name = 'download'5�_�                       <    ����                                                                                                                                                                                                                                                                                                                               <          D       v   7    ]��Y    �         �      Fdldir_name = '/smb/大学/授業教材/ポータルサイト/download'5�_�                   ^       ����                                                                                                                                                                                                                                                                                                                            {   +       {   +       V   +    ]�?    �   ]   _   �              _sub = i.get_text()5�_�                    �        ����                                                                                                                                                                                                                                                                                                                                                             ]�i    �   �   �   �       �   �   �   �    5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ]�K�     �                # 絶対パス5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ]�K�    �         �    �         �    5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ]�K�     �                # 絶対パス5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ]�K�     �         �    �         �    5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ]�K�     �                @# 存在していてもOKとする（エラーで止めない）5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ]�K�    �         �    5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ]�K�     �                # 保存先フォルダ名5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ]�K�     �                2# 絶対パスを簡単に取得できるように5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ]�K�     �                from pathlib import Path5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ]�K�    �         �    �         �    5�_�                    L        ����                                                                                                                                                                                                                                                                                                                            9           9           V        ]�L    �   K   L              # print(link, sub)5�_�                    Q        ����                                                                                                                                                                                                                                                                                                                            9           9           V        ]�L    �   P   R   �      print(subject)5�_�                    |        ����                                                                                                                                                                                                                                                                                                                            �           |           V        ]�L    �   {   |          # 参加しているコース   "#<ul class="courseTree courseList"   #<table class="ContentsMenu"   #の   #target="_top"   #のhrefを見つけて実行   #<hrefを実行   k#<a href="do_contents.php?set_contents_id=f55349184359b88741508f5f8d11742e&reset_status=true&acs_=373fa389"   %#target="download"のhrefを探して      �# href="/webclass/download.php/3講目講義資料_アニメーション.ppt?file=08adc37910addfad98ed6ac08c75fe3e&target_type=attach&time=1571730861&group_id=d25f18c109410e3b755e6679da81fd85&contents_id=5d2cdd58d109a6c26a248b16fe690b55&uid=2a9f81c3687d9e13a9aed54672f098ad&username=180973367&realname=%E5%AE%89%E7%94%B0%E3%80%80%E6%85%A7&acs_=9af26ef4&file_name=3%E8%AC%9B%E7%9B%AE%E8%AC%9B%E7%BE%A9%E8%B3%87%E6%96%99_%E3%82%A2%E3%83%8B%E3%83%A1%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3.ppt"   # hrefを探してwget5�_�                    X        ����                                                                                                                                                                                                                                                                                                                            |           |           V        ]�LB     �   W   X              print(_html)5�_�                    _       ����                                                                                                                                                                                                                                                                                                                            {           {           V        ]�Ld    �   ^   _          G            # print('https://rpwebcls.meijo-u.ac.jp/webclass/' + _link)5�_�                    d       ����                                                                                                                                                                                                                                                                                                                            z           z           V        ]�Lh    �   c   d                      print(_html)5�_�                   e       ����                                                                                                                                                                                                                                                                                                                            y           y           V        ]�L�    �   d   e          �            # frame src="/webclass/text/d2/d25f18c109410e3b755e6679da81fd85/9ac09ad225b8381ea99913def2c116a5/a99913def2c116a5.pdf" noresize="" />5�_�                     d       ����                                                                                                                                                                                                                                                                                                                            x           x           V        ]�L�    �   d   f   y    5�_�      "               a        ����                                                                                                                                                                                                                                                                                                                            y           y           V        ]�L�    �   `   a           5�_�       #   !       "            ����                                                                                                                                                                                                                                                                                                                                                             ]��>     �       "   y    5�_�   "   $           #   !        ����                                                                                                                                                                                                                                                                                                                                                             ]��D     �       +   z       5�_�   #   %           $   (       ����                                                                                                                                                                                                                                                                                                                            (          (   )       v       ]��Q     �   '   )   �      ,# 画像を読み込まないで軽くする5�_�   $   &           %   '        ����                                                                                                                                                                                                                                                                                                                            (          (   )       v       ]��R     �   &   '          !options.add_argument('--lang=ja')5�_�   %   '           &   &        ����                                                                                                                                                                                                                                                                                                                            '          '   )       v       ]��S     �   %   &          # 言語5�_�   &   (           '   %        ����                                                                                                                                                                                                                                                                                                                            &          &   )       v       ]��T     �   $   %          -options.add_argument('--user-agent=hogehoge')5�_�   '   )           (   $        ����                                                                                                                                                                                                                                                                                                                            %          %   )       v       ]��U    �   #   $          # UA5�_�   (   *           )   $        ����                                                                                                                                                                                                                                                                                                                            %           $           V        ]���    �   #   $          # 画像を読み込まない   <options.add_argument('--blink-settings=imagesEnabled=false')5�_�   )   +           *   !        ����                                                                                                                                                                                                                                                                                                                            #           !           V        ]���    �       !          %# headlessでは不要そうな機能   7options.add_argument('--disable-desktop-notifications')   ,options.add_argument("--disable-extensions")5�_�   *               +   !        ����                                                                                                                                                                                                                                                                                                                                                             ]��    �       !           5�_�               "   !   t       ����                                                                                                                                                                                                                                                                                                                            w           w           V        ]�L�     �   s   u        5�_�                    e       ����                                                                                                                                                                                                                                                                                                                            x           x           V        ]�L|     �   d   f        5�_�                   {       ����                                                                                                                                                                                                                                                                                                                                                             ]��     �   z   |   �      $                     print(filename)5�_�                   {       ����                                                                                                                                                                                                                                                                                                                                                             ]��    �   z   |   �      #                    print(filename)5�_�                    z       ����                                                                                                                                                                                                                                                                                                                                                             ]�3    �   z   {   �                          �   z   |   �      ,                    print('^^^^^^^^^^^^^^^')5�_�      
              |        ����                                                                                                                                                                                                                                                                                                                            {   +       {   +       V   +    ]�A     �   |   }   �    �   |   }   �      ,                    print('^^^^^^^^^^^^^^^')5�_�                 
   }       ����                                                                                                                                                                                                                                                                                                                            {   +       {   +       V   +    ]�-     �   }   ~   �    5�_�      	       
      }       ����                                                                                                                                                                                                                                                                                                                            {   +       {   +       V   +    ]�B    �   }   ~   �                          �   }      �      X                    print(filename.replace('»', '').replace(' ', '').replace('　', '')5�_�                  	   ~   X    ����                                                                                                                                                                                                                                                                                                                                                             ]�k   	 �   }      �      Y                    print(filename.replace('»', '').replace(' ', '').replace('　', ''))5�_�                    {       ����                                                                                                                                                                                                                                                                                                                                                             ]��     �   z   |   �      #                     rint(filename)5��