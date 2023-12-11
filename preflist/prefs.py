class Prefs:
    def __init__(self):
        self.__kanji = "北海道 青森県 岩手県 宮城県 秋田県 山形県 福島県 茨城県 栃木県 群馬県 埼玉県 千葉県 東京都 神奈川県 新潟県 富山県 石川県 福井県 山梨県 長野県 岐阜県 静岡県 愛知県 三重県 滋賀県 京都府 大阪府 兵庫県 奈良県 和歌山県 鳥取県 島根県 岡山県 広島県 山口県 徳島県 香川県 愛媛県 高知県 福岡県 佐賀県 長崎県 熊本県 大分県 宮崎県 鹿児島県 沖縄県"
        self.__kana = "ほっかいどう あおもり いわて みやぎ あきた やまがた ふくしま いばらき とちぎ ぐんま さいたま ちば とうきょう かながわ にいがた とやま いしかわ ふくい やまなし ながの ぎふ しずおか あいち みえ しが きょうと おおさか ひょうご なら わかやま とっとり しまね おかやま ひろしま やまぐち とくしま かがわ えひめ こうち ふくおか さが ながさき くまもと おおいた みやざき かごしま おきなわ "
        self.__en = "hokkaido aomori iwate miyagi akita yamagata fukushima ibaraki tochigi gunma saitama chiba tokyo kanagawa niigata toyama ishikawa fukui yamanashi nagano gifu shizuoka aichi mie shiga kyoto osaka hyogo nara wakayama tottori shimane okayama hiroshima yamaguchi tokushima kagawa ehime kochi fukuoka saga nagasaki kumamoto oita miyazaki kagoshima okinawa"
        self.__kata = "ホッカイドウ アオモリ イワテ ミヤギ アキタ ヤマガタ フクシマ イバラキ トチギ グンマ サイタマ チバ トウキョウ カナガワ ニイガタ トヤマ イシカワ フクイ ヤマナシ ナガノ ギフ シズオカ アイチ ミエ シガ キョウト オオサカ ヒョウゴ ナラ ワカヤマ トットリ シマネ オカヤマ ヒロシマ ヤマグチ トクシマ カガワ エヒメ コウチ フクオカ サガ ナガサキ クマモト オオイタ ミヤザキ カゴシマ オキナワ"

    def get(self, prop="kanji"):
        if prop == "en":
            return self.__en.split(" ")
        elif prop == "kata":
            return self.__kata.split(" ")
        elif prop == "kana":
            return self.__kana.split(" ")
        elif prop == "kanji":
            return self.__kanji.split(" ")

        
