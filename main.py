### 1. Shifrlangan matndan o‘rtacha ASCII
# matn = 'adrjenqafwfads'
#
# yigindi = 0
# for i in matn:
#     yigindi += ord(i)
# ortacha = yigindi / len(matn)
# print(ortacha)
from colorsys import yiq_to_rgb

### 2.. ASCII oralig‘i bo‘yicha filtr
# a = input("Matn kiriting: ")
#
# natija = ''
# for i in a:
#     if 65 <= ord(i) <= 122:
#         natija += i
# print(natija)

### 3.. So‘zlar bo‘yicha eng “yukori ASCII” so‘zni toping
# matn = input("Matn kiriting: ")
#
# sozlar = matn.split()
# max_yigindi = 0
# eng_katta_soz = ''
#
#
# for i in sozlar:
#     yigindi = sum(ord(j) for j in i )
#     print(yigindi)
#     if yigindi > max_yigindi:
#         max_yigindi = yigindi
#         eng_katta_soz = i
#
# print(f"Eng katta soz: {eng_katta_soz}" )
# print(f"Max yigindi: {max_yigindi}")

### 4. Belgilarni juft/toq ASCII kodi bo‘yicha guruhlash
# matn = input("Belgilarni kiriting: ")
#
# juft_belgilar = ''
# toq_belgilar = ''
# for i in matn:
#     if ord(i) % 2 == 0:
#         juft_belgilar += i
#     else:
#         toq_belgilar += i
#
# print(f"Juft belgilar {juft_belgilar}")
# print(f"Toq belgilar {toq_belgilar}")

### 5
# matn = input("Matn kiriting: ")
# n = int(input("Siljitish miqdori (n): "))
#
# natija = ''
#
# for belgi in matn:
#     if 'A' <= belgi <= 'Z':
#         kod = (ord(belgi) - ord('A') + n) % 26 + ord('A')
#         natija += chr(kod)
#     elif 'a' <= belgi <= 'z':
#         kod = (ord(belgi) - ord('a') + n) % 26 + ord('a')
#         natija += chr(kod)
#     else:
#         natija += belgi
# print("Shifrlangan matn:", natija)

### 6
# matn = input("Matn kiriting: ")
#
# farqlar = []
#
# for i in range(1, len(matn)):
#     farq = ord(matn[i]) - ord(matn[i - 1])
#     farqlar.append(farq)
#
# print("ASCII farqlar ro'yxati:", farqlar)


### 7
# ism = input("Ismingizni kiriting: ")
# familiya = input("Familiyangizni kiriting: ")
#
# ism_ascii = [str(ord(harf)) for harf in ism]
# familiya_ascii = [str(ord(harf)) for harf in familiya]
#
# aralash = []
# for i in range(max(len(ism_ascii), len(familiya_ascii))):
#     if i < len(ism_ascii):
#         aralash.append(ism_ascii[i])
#     if i < len(familiya_ascii):
#         aralash.append(familiya_ascii[i])
#
# parol_rakamlar = ''.join(aralash)
#
#
# parol = parol_rakamlar[:8]
#
# print("Yaratilgan parol:", parol)
