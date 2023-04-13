ТОКЕН  =  "5745766103:AAEvS84tPxYEAINRMGCYa1DDuJcv7biz-Sk"

ключи  = {
    'евро' : 'EUR' ,
    'доллар' : 'доллар США' ,
    'рубль' : 'руб'
} запросы на импорт
импортировать  json
из  ключей импорта конфигурации

класс  APIException ( Исключение ):
    проходить

класс  криптоконвертера :
    @ статический метод
    def  get_price ( база : ул , котировка : ул , сумма : ул ):
        если  цитата  ==  база :
            поднять  APIException ( f'Невозможно перевести получение валюты { base } .' )

        попробуй :
            quote_ticker  =  ключи [ цитата ]
        кроме  KeyError :
            поднять  APIException ( f'Не удалось обработать валюту { quote } ' )

        попробуй :
            base_ticker  =  ключи [ база ]
        кроме  KeyError :
            поднять  APIException ( f'Не удалось обработать валюту { base } ' )

        попробуй :
            сумма  =  плавающая ( сумма )
        кроме  ValueError :
            поднять  APIException ( f'Не удалось обработать количество валюты { количество } ' )

        если  сумма  <=  0 :
            поднять  APIException ( f'Невозможно конверсировать количество валюты меньше или равное 0' )

        р  =  запросы . получить ( f'https://min-api.cryptocompare.com/data/price?fsym= { base_ticker } &tsyms= { quote_ticker } ' )
        общая_база  =  json . загружает ( r . содержание )[ ключи [ цитата ]]

        вернуть  total_base
импортировать  телебота
из  ключей импорта конфигурации  , TOKEN
из  расширений  импортировать  APIException , CryptoConverter

бот  =  телебот . ТелеБот ( ЖЕТОН )

@ бот . message_handler ( команды = [ 'start' , 'help' ])
def  help ( сообщение : телебот . типы . Сообщение ):
    text  =  'Чтобы начать работу, принять команду боту в следующнм формат: \n <имя валютной цены, которую он хочет узнать> \
<имя валюты, в которой необходимо узнать цену первой валюты> \
<количество первой валюты> \n Увидеть список доступных валют: /values'
    бот . answer_to ( сообщение , текст )

@ бот . message_handler ( команды = [ 'значения' ])
 значения def ( сообщение : телебот . типы . сообщение ):
    text  =  'Доступные валюты:'
    для  ключей  в  ключах . ключи ():
        текст  =  ' \n ' . присоединиться (( текст , ключ , ))
    бот . answer_to ( сообщение , текст )

@ бот . message_handler ( content_types = [ 'текст' ,])
def  convert ( сообщение : телебот . типы . Сообщение ):
    попробуй :
        значения  =  сообщение . текст . разделить ( '' )

        если  len ( значения ) >  3 :
            поднять  APIException ( "Слишком много параметров." )
        elif  len ( значения ) <  3 :
            поднять  APIException ( "Мало параметров." )

        база , цитата , сумма  =  значения
        total_base  =  криптоконвертер . get_price ( база , котировка , сумма )
    кроме  APIException  как  e :
        бот . answer_to ( сообщение , f'Ошибка пользователя \n { e } ' )
    кроме  Исключения  как  e :
        бот . answer_to ( сообщение , f'Не удалось обработать команду \n { e } ' )
    еще :
        text  =  f'Цена { сумма }  { база } в { цитата } - { общая_база } '
        бот . send_message ( сообщение . чат . идентификатор , текст )

бот . опрос ()