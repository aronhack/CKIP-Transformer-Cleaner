import pandas as pd
import re
from ckip_transformers.nlp import CkipWordSegmenter, CkipPosTagger, CkipNerChunker


def str_remove_emoji(text):
    '''
    Remove emoji from text
    - This function will preserve traditional Chinese characters
    '''
    emoji_pattern = re.compile("["
                               u"\U0001F000-\U0001F9FF"  # Extended emoticons and symbols
                               u"\U0001FA00-\U0001FA6F"  # Extended-A
                               u"\U0001FA70-\U0001FAFF"  # Extended-B
                               u"\U00002600-\U000027BF"  # Miscellaneous Symbols and Dingbats
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               u"\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
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
    word_pos = word_pos[['word', 'pos']]
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
                .groupby(['word', 'pos'])
                .size()
                .reset_index(name='word_count'))

    return word_pos


def clean_word_ner(ner):
    '''
    Clean word ner
    '''
    ner = ner[['word', 'ner']]
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
           .groupby(['word', 'ner'])
           .size()
           .reset_index(name='word_count'))
    return ner


def run_ckip_transofomer():
    '''
    Duplicated and adjusted from official GitHub
    https://github.com/ckiplab/ckip-transformers/blob/master/example/example.py
    '''

    # Show version
    print(__version__)

    # Initialize drivers
    print("Initializing drivers ... WS")
    ws_driver = CkipWordSegmenter(model="bert-base")
    print("Initializing drivers ... POS")
    pos_driver = CkipPosTagger(model="bert-base")
    print("Initializing drivers ... NER")
    ner_driver = CkipNerChunker(model="bert-base")
    print("Initializing drivers ... done")
    print()

    # Input text
    text = [
        "傅達仁今將執行安樂死，卻突然爆出自己20年前遭緯來體育台封殺，他不懂自己哪裡得罪到電視台。",
        "美國參議院針對今天總統布什所提名的勞工部長趙小蘭展開認可聽證會，預料她將會很順利通過參議院支持，成為該國有史以來第一位的華裔女性內閣成員。",
        "空白 也是可以的～",
    ]

    # Run pipeline
    print("Running pipeline ... WS")
    ws = ws_driver(text)
    print("Running pipeline ... POS")
    pos = pos_driver(ws)
    print("Running pipeline ... NER")
    ner = ner_driver(text)
    print("Running pipeline ... done")
    print()

    # Flag each [word, pos, ner]
    word_pos_li = []
    word_ner_li = []
    for sentence_ws, sentence_pos, sentence_ner in zip(ws, pos, ner):
        # Concatenate word, pos
        for word_ws, word_pos in zip(sentence_ws, sentence_pos):
            word_pos_li.append([word_ws, word_pos])

        # Flag ner
        for entity in sentence_ner:
            word_ner_li.append([entity.word, entity.ner])

    return word_pos_li, word_ner_li


def main():
    word_pos_li, word_ner_li = run_ckip_transofomer()
    word_pos = clean_word_pos(word_pos_li)
    word_ner = clean_word_ner(word_ner_li)
    print(word_pos)
    print(word_ner)


if __name__ == "__main__":
    main()
