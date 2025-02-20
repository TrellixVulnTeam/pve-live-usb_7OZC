��    v      �  �   |      �	     �	     	
     %
  #   >
     b
     w
     �
     �
     �
     �
     �
          (     D     b     t     �     �  H   �  	  �            0        O     b     t  /   �     �     �  $   �          !     3      N  ,   o  )   �     �     �     �  j        r  *   �      �  
   �     �     �     �     �               ,     C     T     k     ~     �     �     �     �  %   �               *     F     W     i     {     �     �     �     �     �     �               1     I     f     ~     �  	   �     �     �     �     �                    &  <   4  M   q     �     �     �     �     �  #   	  #   -     Q     j  
   y     �     �     �     �     �     �      �          0     C     K     ^     q     t  #   �     �  y  �  @   B  ,   �  1   �  B   �  1   %  N   W  L   �  #   �  !     !   9  !   [     }  (   �  *   �     �            #   7  �   [  �  �     �     �  Z   �  -   $     R     q  ]   �  !   �  @     b   R     �  #   �  /   �  J   '  _   r  W   �      *   !   K   ,   m   �   �   0   K!  V   |!  T   �!     ("     @"  !   Q"     s"     �"  (   �"  &   �"  0   �"  '   $#  ?   L#  0   �#  *   �#  *   �#  6   $  -   J$  #   x$  K   �$  -   �$     %  H   2%  .   {%  .   �%  .   �%  .   &  *   7&  8   b&  &   �&     �&  1   �&  F   '  3   ['  ?   �'  G   �'  4   (  E   L(  !   �(  K   �(  (    )  <   ))  <   f)  .   �)  .   �)     *  	   *  >   *  "   M*  d   p*  y   �*  0   O+  3   �+     �+     �+     �+  Q   �+  O   ;,  .   �,  *   �,     �,  7   -  5   9-  $   o-     �-  :   �-     �-  G   .  /   W.  F   �.     �.     �.     /     !/  F   $/  C   k/  '   �/     
   D          _                      ,       R      g   d       o   r              5   '           9   n      J   (   j   Z   O   i   `      H              m       u   :                       h              "      P   ?   I   =      *      W   +           a   V   &   \   7          ]              $       b   U   e         N   8   c   B   @   K   !      Q   >           Y      f       E   S   4   0   	   p           1   ;   F       k   t       C   .   /         [   q   ^   6   <             l   -       )           v   T           s      3   X              #   2   M          A   L   G   %    
Supported algorithms:
 %s makes no sense with %s!
 %s not allowed with %s!
 %s: failed to create hashtable: %s
 %s: keyring created
 %s:%d: invalid export options
 %s:%d: invalid import options
 --clearsign [filename] --decrypt [filename] --edit-key user-id [commands] --encrypt [filename] --lsign-key user-id --sign --encrypt [filename] --sign --symmetric [filename] --sign [filename] --sign-key user-id --store [filename] --symmetric [filename] @
(See the man page for a complete listing of all commands and options)
 @
Examples:

 -se -r Bob [file]          sign and encrypt for user Bob
 --clearsign [file]         make a clear text signature
 --detach-sign [file]       make a detached signature
 --list-keys [names]        show keys
 --fingerprint [names]      show fingerprints
 @
Options:
  @Commands:
  Answer "yes" if it is okay to overwrite the file Enter new filename Enter passphrase
 Enter passphrase:  Enter the new passphrase for this secret key.

 File `%s' exists.  Invalid command  (try "help")
 Invalid passphrase; please try again Key is protected.
 No help available No help available for `%s' Please enter name of data file:  Please report bugs to <gnupg-bugs@gnu.org>.
 Please select what kind of key you want:
 Repeat passphrase
 Repeat passphrase:  Secret key is available.
 Syntax: gpg [options] [files]
Sign, check, encrypt or decrypt
Default operation depends on the input data
 This key has expired! Usage: gpg [options] [files] (-h for help) WARNING: using insecure memory!
 [filename] bad MPI bad certificate bad key bad passphrase bad public key bad secret key be somewhat more quiet can't open `%s'
 can't open the keyring cancelled by user
 checksum error conflicting commands
 decrypt data (default) do not make any changes encrypt data encryption only with symmetric cipher error creating `%s': %s
 export keys export keys to a key server file close error file create error file delete error file open error file read error file rename error file write error general error generate a new key pair import keys from a key server import/merge keys invalid default preferences
 invalid export options
 invalid hash algorithm `%s'
 invalid import options
 invalid passphrase list key and user IDs list keys list keys and fingerprints list keys and signatures list secret keys make a detached signature nN no no such user id not supported operation is not possible without initialized secure memory
 please see http://www.gnupg.org/documentation/faqs.html for more information
 prompt before overwriting public key not found qQ quit reading stdin ...
 remove keys from the public keyring remove keys from the secret keyring secret key not available show this help sign a key sign a key locally sign or edit a key signing failed: %s
 unexpected data unknown compress algorithm unknown version update all keys from a keyserver usage: gpg [options]  use as output file verbose verify a signature writing to stdout
 yY |NAME|encrypt for NAME |[file]|make a clear text signature |[file]|make a signature Project-Id-Version: gnupg 1.2.2
Report-Msgid-Bugs-To: translations@gnupg.org
POT-Creation-Date: 2018-06-08 20:19+0000
PO-Revision-Date: 2012-08-24 17:19+0200
Last-Translator: Ales Nyakhaychyk <nab@mail.by>
Language-Team: Belarusian <i18n@mova.org>
Language: be
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit
X-Generator: KBabel 1.0.2
 
Альгарытмы, якія падтрымліваюцца:
 %s ня мае сэнсу разам з %s!
 %s не дазваляецца разам з %s!
 %s: немагчыма стварыць хэш-табліцу: %s
 %s: створаны зьвязак ключоў
 %s:%d: недапушчальныя выбары экспартаваньня
 %s:%d: недапушчальныя выбары імпартаваньня
 --clearsign [назва_файла] --decrypt [назва_файла] --edit-key user-id [загады] --encrypt [назва_файла] --lsign-key user-id --sign --encrypt [назва_файла] --sign --symmetric [назва_файла] --sign [назва_файла] --sign-key user-id --store [назва_файла] --symmetric [назва_файла] @
(Глядзіце man старонку, для больш поўнага апісаньня ўсіх загадаў і выбараў)
 @
Прыклады:

 -se -r Bob [файл]          падпісаць і зашыфраваць для карыстальніка Bob
 --clearsign [файл]         стварыць чысты тэкставы подпіс
 --detach-sign [файл]       стварыць адчэплены подпіс
 --list-keys [назвы]        паказаць ключы
 --fingerprint [назвы]      паказаць адбіткі пальцаў
 @
Выбары:
  @Загады:
  Адкажыце "так", калі Вы згодны з перазапісам файла Увядзіце новае ймя файла Увядзіце пароль
 Увядзіце пароль:  Увядзіце новы пароль для гэтага сакрэтнага ключа.

 Файл "%s" ужо йснуе.  Нерэчаісны загад (паспрабуйце "help")
 Недапушчальны пароль. Калі ласка, паспрабуйце шчэ раз Ключ абаронены.
 Даведка адсутнічае Для "%s" даведка адсутнічае Калі ласка, задайце назву файла даньняў:  Калі ласка, паведамляйце пра памылкі на <gnupg-bugs@gnu.org>.
 Калі ласка, абярыце від ключа, які Вам патрэбны:
 Паўтарыце пароль
 Паўтарыце пароль:  Даступны сакрэтны ключ.
 Сынтаксіс: gpg [выбары] [файлы]
sign, check, encrypt ці decrypt
Дапомнае дзеяньне залежыць ад уваходных даньняў
 Гэты ключ згубіў састарэў! Выкарыстаньне: gpg [выбары] [файлы] (-h для даведкі) УВАГА! Выкарыстоўваецца небясьпечная памяць!
 [назва_файла] дрэнны MPI дрэнны сэртыфікат дрэнны ключ дрэнны пароль дрэнны грамадскі ключ дрэнны сакрэтны ключ працаваць менш шматслоўна немагчыма адкрыць "%s"
 немагчыма адчыніць зьвязак ключоў скасавана карыстальнікам
 памылка праверчае сумы несумяшчальныя загады
 разшыфраваць даньні (дапомна) не рабіць ніякіх зьменаў зашыфраваць даньні шыфраваньне толькі сымэтрычнымі шыфрамі памылка стварэньня "%s": %s
 экспарт ключоў экспартаваць ключы на паслужнік ключоў памылка зачыненьня файла памылка стварэньня файла памылка выдаленьня файла памылка адчыненьня файла памылка чытаньня файла памылка перайменаваньня файла памылка запісу файла агульная памылка стварыць новую пару ключоў імпартаваць ключы з паслужніка ключоў імпартаваць/аб'яднаць ключы недапушчальныя дапомныя перавагі
 недапушчальныя выбары экспартаваньня
 нерэчаісны хэш-альгарытм "%s"
 недапушчальныя выбары імпартаваньня
 нерэчаісны пароль паказаць сьпіс ключоў і ID карыстальнікаў паказаць сьпіс ключоў паказаць ключы й адбіткі пальцаў паказаць сьпіс ключоў і подпісаў паказаць сакрэтныя ключы зрабіць адчэплены подпіс nN no [не] карыстальнік з такім ID адсутнічае непадтрымліваецца дзеяньне немагчымае без распачатае бясьпечнае памяці
 па больш падрабязныя зьвесткі шукайце на http://www.gnupg.org/documentation/faqs.html
 пытацца перад перазапісам грамадскі ключ ня знойдзены qQ quit [выйсьці] чытаецца stdin ...
 выдаліць ключы са зьвязку грамадскіх ключоў выдаліць ключы са зьвязку сакрэтных ключоў сакрэтны ключ недаступны паказаць гэтую даведку падпісаць ключ падпісаць ключ толькі мясцова падпісаць ці рэдагаваць ключ збой падпісаньня: %s
 нечаканыя даньні невядомы альгарытм сьцісканьня невядомая вэрсыя абнавіць усе ключы з паслужніка ключоў Выкарыстаньне: gpg [выбары]  выкарыстоўваць у якасьці файла вываду шматслоўнасьць праверыць подпіс запіс у stdout
 yY |ІМЯ|   зашыфраваць для вылучанай асобы |[файл]|зрабіць чысты тэкставы подпіс |[файл]|зрабіць подпіс 