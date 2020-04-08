# -*- coding: utf-8 -*-
import re

from alphabet_detector import AlphabetDetector
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle, Image


# 初期設定
def make(filename="resume"):  # ファイル名
    pdf_canvas = set_info(filename)  # キャンバス名
    print_string(pdf_canvas)
    pdf_canvas.save()  # 保存


def set_info(filename):
    pdf_canvas = canvas.Canvas("./{0}.pdf".format(filename))  # 保存先
    pdf_canvas.setAuthor("")  # 作者
    pdf_canvas.setTitle("")  # 表題
    pdf_canvas.setSubject("")  # 件名
    return pdf_canvas


def cut_text(text, lenth):
    textArr = re.findall('.{' + str(lenth) + '}', text)
    body_text = text[(len(textArr) * lenth):]

    textArr.append(body_text)
    return textArr


# 履歴書フォーマット作成
def print_string(pdf_canvas):
    pdfmetrics.registerFont(UnicodeCIDFont('HeiseiKakuGo-W5'))  # フォント
    width, height = A4  # 用紙サイズ

    # (1)履歴書 タイトル
    font_size = 24  # フォントサイズ
    pdf_canvas.setFont('HeiseiKakuGo-W5', font_size)
    pdf_canvas.drawString(90, 770, '履  歴  書')  # 書き出し(横位置, 縦位置, 文字)

    # (2)作成日
    year = '2020'
    month = '12'
    day = '16'
    font_size = 10
    pdf_canvas.setFont('HeiseiKakuGo-W5', font_size)
    pdf_canvas.drawString(285, 770, f'{year}年   {month}月   {day}日現在')

    # (3)証明写真
    # tableを作成
    a = Image(f'/Users/stevenzhang/PycharmProjects/python-study/WechatIMG2344.jpeg')
    a.drawHeight = 32 * mm
    a.drawWidth = 25 * mm

    data = [
        [a],
    ]
    table = Table(data, colWidths=30 * mm, rowHeights=40 * mm)  # tableの大きさ
    table.setStyle(TableStyle([  # tableの装飾
        ('FONT', (0, 0), (0, 0), 'HeiseiKakuGo-W5', 12),  # フォントサイズ
        ('BOX', (0, 0), (0, 0), 1, colors.black),  # 罫線
        ('VALIGN', (0, 0), (0, 0), 'MIDDLE'),  # フォント位置
    ]))
    table.wrapOn(pdf_canvas, 145 * mm, 235 * mm)  # table位置
    table.drawOn(pdf_canvas, 145 * mm, 235 * mm)

    # (4) プロフィール
    data = [
        ['ふりがな　　'
         'チョウ　リョウヒ', '   男  ・  女'],
        ['氏名 Steven　張りょうひ', ''],
        ['生年月日　　　　　　　　　　　　　1980　　年　12　　月　16　　日生　（満　40歳）', ''],
    ]
    table = Table(data, colWidths=(100 * mm, 20 * mm), rowHeights=(7 * mm, 20 * mm, 7 * mm))
    table.setStyle(TableStyle([
        ('FONT', (0, 0), (1, 2), 'HeiseiKakuGo-W5', 8),
        ('BOX', (0, 0), (1, 2), 1, colors.black),
        ('INNERGRID', (0, 0), (1, 2), 1, colors.black),
        ('SPAN', (0, 2), (1, 2)),
        ('SPAN', (1, 0), (1, 1)),
        ('VALIGN', (0, 0), (1, 2), 'MIDDLE'),
        ('VALIGN', (0, 1), (0, 1), 'TOP'),
    ]))
    table.wrapOn(pdf_canvas, 20 * mm, 232 * mm)
    table.drawOn(pdf_canvas, 20 * mm, 232 * mm)

    # (5)住所
    data = [
        ['ふりがな', '電話'],
        ['連絡先（〒120ー0021　）   \n銀河系連邦皇帝大街\nSteven Zhang壹号院\n香山御景台官邸', 'E-mail \nzhanglingfei@google.com'],
        ['ふりがな', '電話'],
        ['連絡先（〒　　　ー　　　　）', 'E-mail'],
    ]
    table = Table(data, colWidths=(100 * mm, 60 * mm), rowHeights=(7 * mm, 20 * mm, 7 * mm, 20 * mm))
    table.setStyle(TableStyle([
        ('FONT', (0, 0), (1, 3), 'HeiseiKakuGo-W5', 9),
        ('BOX', (0, 0), (1, 3), 1, colors.black),
        ('INNERGRID', (0, 0), (1, 3), 1, colors.black),
        ('VALIGN', (0, 0), (1, 2), 'MIDDLE'),
        ('VALIGN', (0, 1), (1, 1), 'TOP'),
        ('VALIGN', (0, 3), (1, 3), 'TOP'),
    ]))
    table.wrapOn(pdf_canvas, 20 * mm, 178 * mm)
    table.drawOn(pdf_canvas, 20 * mm, 178 * mm)

    # (6)学歴・職歴
    data = [
        ['        年', '   月', '                                            学歴・職歴'],
        ['2002 ', '12 ', '木星戦争学院 文学物理系 '],
        ['1992 ', '12 ', '冥王星げい術学院 ピアノ化学系 '],
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]
    table = Table(data, colWidths=(25 * mm, 14 * mm, 121 * mm), rowHeights=7.5 * mm)
    table.setStyle(TableStyle([
        ('FONT', (0, 0), (-1, -1), 'HeiseiKakuGo-W5', 11),
        ('BOX', (0, 0), (-1, -1), 1, colors.black),
        ('INNERGRID', (0, 0), (-1, -1), 1, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    table.wrapOn(pdf_canvas, 20 * mm, 20 * mm)
    table.drawOn(pdf_canvas, 20 * mm, 20 * mm)

    # 1枚目終了
    pdf_canvas.showPage()

    # (7)学歴・職歴、免許・資格
    data = [
        ['        年', '   月', '                                            学歴・職歴'],
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        ['        年', '   月', '                                            免許・資格'],
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' '],
    ]
    table = Table(data, colWidths=(25 * mm, 14 * mm, 121 * mm), rowHeights=7.5 * mm)
    table.setStyle(TableStyle([
        ('FONT', (0, 0), (-1, -1), 'HeiseiKakuGo-W5', 11),
        ('BOX', (0, 0), (-1, -1), 1, colors.black),
        ('INNERGRID', (0, 0), (-1, -1), 1, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    table.wrapOn(pdf_canvas, 20 * mm, 132 * mm)
    table.drawOn(pdf_canvas, 20 * mm, 132 * mm)

    # (8)そのほか

    # orig_sentence = 'NHKは、放送法に基づく特殊法人として1950年に設立された。設立目的は、放送法により「公共の福祉のために、あまねく日本全国で受信できるように豊かで、' \
    #                 '且つ良い放送番組による国内基幹放送を行うと同時に放送およびその受信の進歩発達に必要な業務を行い、' \
    #                 '合わせて国際放送および協会国際衛星放送を行うこと」となっている（法15条、定款3条）。また、同法の規定により1926年に設立された社団法人日本放送協会の業務' \
    #                 'を継承している（法附則第13項）。なお、社団法人日本放送協会は、1925年に日本で初めて放送業務を開始した社団法人東京放送局、社団法人名古屋放送局、社団法人大阪放送局（' \
    #                 '現：NHK放送センター、NHK名古屋放送局、NHK大阪放送局）の業務を統合して設立されたものである'
    orig_sentence = '所属事務所によると、速水さんは3日に発熱症状がみられ、その後も咽頭痛や咳、痰、体の痛み等の症状が続いたことから、6日に医療機関を受診。胸部レントゲンでは所' \
                    '見なしの診断だったものの、PCR検査を受けることになり、7日午後に陽性が確認されたという。速水さんは現在、' \
                    '所属事務所によると、速水さんは3日に発熱症状がみられ、その後も咽頭痛や咳、痰、体の痛み'\
                    '症状は安定しているものの自宅待機をしており、受け入れ先の病院が手配でき次第入院する予定だということだ。なお、3月17日以降はスタッフやキ' \
                    'ャストとの濃厚接触はなかったという。速水さんは所属事務所を通じ、「この度はご心配、ご迷惑をおかけして誠に申し訳ありません。今は、症状も快方に向かってきており、' \
                    'このまま完全復活できるよう快復に努めます。そしてまた元気になって歌う姿を必ずお見せしたいと思います」とコメントしている。'

    print(len(orig_sentence))

    final_text = return_split_text_by_characterencode(orig_sentence)

    data = [
        ['志望の動機、自己PR、趣味、特技など \n'
         'For accurate long-term ephemerides, please instead\n '
         'use our Horizons system. This orbit viewer was\n'
         'implemented using two-body and hence should not \n'
         'used for determining accurate long-term \n'
         'trajectories (over several years or decades) \n'
         'or planetary encounter circumstances.', '通勤時間', ''],
        ['', '                        約　　2時間　　23分', ''],
        ['', '扶養家族（配偶者を除く）', ''],
        ['', '                              　　　　    　　　　人', ''],
        ['', '配偶者', '配偶者の扶養義務'],
        ['', '       有    ・    無', '       有    ・    無'],
        ['本人希望記入欄（特に待遇・職種・勤務時間・その他についての希望などがあれば記入）', '', ''],
        [final_text]

    ]
    print(len('and hence should not be used for determining accurate long-term trajectories trajectories \n '))
    table = Table(data, colWidths=(90 * mm, 35 * mm, 35 * mm),
                  rowHeights=(8 * mm, 10 * mm, 8 * mm, 10 * mm, 8 * mm, 10 * mm, 8 * mm, 50 * mm))
    table.setStyle(TableStyle([
        ('FONT', (0, 0), (2, 7), 'HeiseiKakuGo-W5', 10),
        ('BOX', (0, 0), (2, 7), 1, colors.black),
        ('LINEBEFORE', (1, 0), (1, 5), 1, colors.black),
        ('LINEBEFORE', (2, 4), (2, 5), 1, colors.black),
        ('LINEABOVE', (1, 2), (2, 2), 1, colors.black),
        ('LINEABOVE', (1, 4), (2, 4), 1, colors.black),
        ('LINEABOVE', (0, 6), (2, 6), 1, colors.black),
        ('LINEABOVE', (0, 7), (2, 7), 1, colors.black),
        ('VALIGN', (0, 0), (2, 5), 'TOP'),
        ('VALIGN', (0, 6), (2, 6), 'MIDDLE'),
    ]))
    table.wrapOn(pdf_canvas, 20 * mm, 20 * mm)
    table.drawOn(pdf_canvas, 20 * mm, 20 * mm)

    # 2枚目終了
    pdf_canvas.showPage()


def return_split_text_by_characterencode(orig_sentence):
    ad = AlphabetDetector()
    character_coding_list = ad.detect_alphabet(orig_sentence)
    for character_coding in character_coding_list:
        print(character_coding)
        if 'HIRAGANA' in character_coding or 'KATAKANA' in character_coding or 'CJK' in character_coding:
            text_list = cut_text(f'{orig_sentence}', 43)
            final_text = ''
            for text in text_list:
                final_text += f'{text}\n'
        else:
            text_list = cut_text(f'{orig_sentence}', 88)
            final_text = ''
            for text in text_list:
                final_text += f'{text}\n'
    return final_text


# 作成
if __name__ == '__main__':
    make()
