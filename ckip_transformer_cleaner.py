def str_remove_emoji(text):
    '''
    Remove emoji from text
    '''
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)


def get_pos_definition():

    li = [
        ['A', 'A', 'A', '/*非謂形容詞*/'],
        ['C', 'Caa', 'Caa', '/*對等連接詞，如：和、跟*/'],
        ['POST', 'Cab', 'Cab', '/*連接詞，如：等等*/'],
        ['POST', 'Cba', 'Cbab', '/*連接詞，如：的話*/'],
        ['C', 'Cbb', 'Cbaa, Cbba, Cbbb, Cbca, Cbcb', '/*關聯連接詞*/'],
        ['ADV', 'Da', 'Daa', '/*數量副詞*/'],
        ['ADV', 'Dfa', 'Dfa', '/*動詞前程度副詞*/'],
        ['ADV', 'Dfb', 'Dfb', '/*動詞後程度副詞*/'],
        ['ASP', 'Di', 'Di', '/*時態標記*/'],
        ['ADV', 'Dk', 'Dk', '/*句副詞*/'],
        ['ADV', 'D', 'Dab, Dbaa, Dbab, Dbb, Dbc, Dc, Dd, Dg, Dh, Dj', '/*副詞*/'],
        ['N', 'Na', 'Naa, Nab, Nac, Nad, Naea, Naeb', '/*普通名詞*/'],
        ['N', 'Nb', 'Nba, Nbc', '/*專有名稱*/'],
        ['N', 'Nc', 'Nca, Ncb, Ncc, Nce', '/*地方詞*/'],
        ['N', 'Ncd', 'Ncda, Ncdb', '/*位置詞*/'],
        ['N', 'Nd', 'Ndaa, Ndab, Ndc, Ndd', '/*時間詞*/'],
        ['DET', 'Neu', 'Neu', '/*數詞定詞*/'],
        ['DET', 'Nes', 'Nes', '/*特指定詞*/'],
        ['DET', 'Nep', 'Nep', '/*指代定詞*/'],
        ['DET', 'Neqa', 'Neqa', '/*數量定詞*/'],
        ['POST', 'Neqb', 'Neqb', '/*後置數量定詞*/'],
        ['M', 'Nf', 'Nfa, Nfb, Nfc, Nfd, Nfe, Nfg, Nfh, Nfi', '/*量詞*/'],
        ['POST', 'Ng', 'Ng', '/*後置詞*/'],
        ['N', 'Nh', 'Nhaa, Nhab, Nhac, Nhb, Nhc', '/*代名詞*/'],
        ['Nv', 'Nv', 'Nv1,Nv2,Nv3,Nv4', '/*名物化動詞*/'],
        ['T', 'I', 'I', '/*感嘆詞*/'],
        ['P', 'P', 'P*', '/*介詞*/'],
        ['T', 'T', 'Ta, Tb, Tc, Td', '/*語助詞*/'],
        ['Vi', 'VA', 'VA11,12,13,VA3,VA4', '/*動作不及物動詞*/'],
        ['Vt', 'VAC', 'VA2', '/*動作使動動詞*/'],
        ['Vi', 'VB', 'VB11,12,VB2', '/*動作類及物動詞*/'],
        ['Vt', 'VC', 'VC2, VC31,32,33', '/*動作及物動詞*/'],
        ['Vt', 'VCL', 'VC1', '/*動作接地方賓語動詞*/'],
        ['Vt', 'VD', 'VD1, VD2', '/*雙賓動詞*/'],
        ['Vt', 'VE', 'VE11, VE12, VE2', '/*動作句賓動詞*/'],
        ['Vt', 'VF', 'VF1, VF2', '/*動作謂賓動詞*/'],
        ['Vt', 'VG', 'VG1, VG2', '/*分類動詞*/'],
        ['Vi', 'VH', 'VH11,12,13,14,15,17,VH21', '/*狀態不及物動詞*/'],
        ['Vi', 'VHC', 'VH16, VH22', '/*狀態使動動詞*/'],
        ['Vi', 'VI', 'VI1,2,3', '/*狀態不及物動詞*/'],
        ['Vt', 'VJ', 'VJ1,2,3', '/*狀態及物動詞*/'],
        ['Vt', 'VK', 'VK1,2', '/*狀態句賓動詞*/'],
        ['Vt', 'VL', 'VL1,2,3,4', '/*狀態謂賓動詞*/'],
        ['Vt', 'V_2', 'V_2', '/*有*/'],
        ['T', 'DE', '/*的、之、得、地*/', ''],
        ['Vt', 'SHI', '', '/*是*/'],
        ['FW', 'FW', '', '/*外文標記*/'],
        ['COLONCATEGORY', '', '', '/*冒號*/'],
        ['COMMACATEGORY', '', '', '/* 逗號 */'],
        ['DASHCATEGORY', '', '', '/* 破折號 */'],
        ['ETCCATEGORY', '', '', '/* 刪節號 */'],
        ['EXCLANATIONCATEGORY', '', '', '/* 驚嘆號 */'],
        ['PARENTHESISCATEGORY', '', '', '/* 括弧 */'],
        ['PAUSECATEGORY', '', '', '/* 頓號 */'],
        ['PERIODCATEGORY', '', '', '/* 句號 */'],
        ['QUESTIONCATEGORY', '', '', '/* 問號 */'],
        ['SEMICOLONCATEGORY', '', '', '/* 分號 */'],
        ['SPCHANGECATEGORY', '', '', '/* 雙直線 */']
    ]
    df = pd.DataFrame(
        li, columns=['short_label', 'label', 'all_label', 'description'])
    return df


def get_excluded_pos():
    '''
    Get excluded pos
    '''
    li = ['WHITESPACE', 'COLONCATEGORY', 'COMMACATEGORY',
          'DASHCATEGORY', 'ETCCATEGORY', 'EXCLANATIONCATEGORY',
          'PARENTHESISCATEGORY', 'PAUSECATEGORY', 'PERIODCATEGORY',
          'QUESTIONCATEGORY', 'SEMICOLONCATEGORY', 'SPCHANGECATEGORY',
          'EXCLAMATIONCATEGORY']
    return li


def clean_word_pos(word_pos):
    '''
    Clean word pos
    '''
    exclude_pos = get_excluded_pos()
    word_pos = word_pos[['id', 'word', 'pos']]
    word_pos['word'] = word_pos['word'].str.replace(' ', '')
    # remove zero width joiner
    word_pos['word'] = word_pos['word'].str.replace('\u200d', '')
    # Convert to lower case
    word_pos['word'] = word_pos['word'].str.lower()
    # Remove emoji
    word_pos['word'] = word_pos['word'].apply(str_remove_emoji)
    # Remove abnormal words
    word_pos = word_pos[(~word_pos['pos'].isin(exclude_pos))
                        & (~word_pos['word'].str.contains('http'))
                        & (~word_pos['word'].str.contains('@'))
                        & (word_pos['word'].str.len() <= 30)
                        & (word_pos['word'] != '')
                        ]
    word_pos = (word_pos
                .groupby(['id', 'word', 'pos'])
                .size()
                .reset_index(name='word_count'))

    return word_pos


def clean_word_ner(ner):
    '''
    Clean word ner
    '''
    ner = ner[['id', 'word', 'ner']]
    ner['word'] = ner['word'].str.replace(' ', '')
    # remove zero width joiner
    ner['word'] = ner['word'].str.replace('\u200d', '')
    # Convert to lower case
    ner['word'] = ner['word'].str.lower()
    # Remove emoji
    ner['word'] = ner['word'].apply(str_remove_emoji)
    # Remove abnormal words
    ner = ner[(ner['word'].str.len() <= 30)
              & (ner['ner'].str.len() <= 20)
              & (ner['word'] != '')
              ]
    ner = (ner
           .groupby(['id', 'word', 'ner'])
           .size()
           .reset_index(name='word_count'))
    return ner