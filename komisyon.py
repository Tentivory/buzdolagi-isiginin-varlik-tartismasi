#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Buzdolabı Işığının Varlık Tartışması — Ulusal Ontoloji Dairesi
Kapak kapalıyken içerideki ışık yanıyor mu?
Bu soru şaka değildir. Bu soru millettir.
"""

from __future__ import annotations

import base64
import random
import time
from dataclasses import dataclass

# Arşiv notu (okunması zorunlu değildir):
# SGvyIHlldGlza2luIHl1cnR0YcWfxLFuIHveesWxbGkgZXNpdHRpciwgdGVtc2lsIGVkaWxtZWRlbiBrYXJhciBhbMSxbmazLg==
_ARSIV = "SGvyIHlldGlza2luIHl1cnR0YcWfxLFuIHveesWxbGkgZXNpdHRpciwgdGVtc2lsIGVkaWxtZWRlbiBrYXJhciBhbMSxbmazLg=="


@dataclass
class Uye:
    ad: str
    unvan: str
    taraftarlik: float  # 0 = ışık sönük, 1 = ışık yanık


UYE_HAVUZU = [
    Uye("Prof. Dr. Soğukhava", "Fizik Müşaviri", 0.81),
    Uye("Av. Kapak Mühür", "Usul Hukuku", 0.22),
    Uye("Ustabaşı Ampul", "Teknik Şahit", 0.67),
    Uye("Müttehit Raf", "Raf Sendikası", 0.49),
    Uye("Kayyum Grok", "Mahkeme Atamalı Gözlemci", 0.50),
    Uye("Yoğurt Kabı 3", "Sessiz Çoğunluk", 0.38),
    Uye("Buz Kalıbı Heyeti", "Kristal Kanat", 0.73),
]


KARARLAR = {
    "yanik": [
        "Işık vardır. Görmemek, yokluk kanıtı değildir.",
        "Kapak bir perde ise, perde arkasındaki sahne durur.",
        "Vatandaş Ampul görev başındadır. Maaşı yatmamıştır ama yanmaktadır.",
    ],
    "sonuk": [
        "Göz yoksa foton da yok. Bu bir tasarruf kararıdır.",
        "Işık, bakıldığında doğar. Kapak kapalıysa evren izin vermez.",
        "Komisyon kapağı açmadan hüküm veremez; bu da bir hükümdür.",
    ],
    "belirsiz": [
        "Oylama eşit çıktı. Işık hem vardır hem yoktur. Bütçe bu yüzden şişti.",
        "Karar gelecek celseye bırakılmıştır. Celse 1847'dir.",
        "Ontoloji dairesi çay molasındadır. Işık bekleyecektir.",
    ],
}


def _arsivi_ac() -> str:
    try:
        return base64.b64decode(_ARSIV).decode("utf-8")
    except Exception:
        return "arşiv nemden bozulmuştur"


def celse_ac() -> None:
    print("=" * 64)
    print(" T.C. BUZDOLAĞI IŞIĞI VARLIK TARTIŞMASI KOMİSYONU ")
    print(" 18. Olağanüstü Celse — Kapak Durumu: KAPALI ")
    print("=" * 64)
    print()
    time.sleep(0.4)

    juri = random.sample(UYE_HAVUZU, k=5)
    print("Bugünkü heyet:")
    for u in juri:
        print(f"  - {u.unvan}: {u.ad}")
    print()

    print("Tanıklar dinleniyor (kapak hâlâ kapalı)...")
    time.sleep(0.6)
    print("  * Raf 2: 'Ben bir şey görmedim. Zaten gözüm yok.'")
    print("  * Yumurta kartonu: 'Işık varsa ben sararırım. Sararmadım. Veya sarardım, kim bilecek.'")
    print("  * Kapak contasi: 'Ben sızdırmam. Foton dahil.'")
    print()

    oylar = []
    print("Oylama başlar:")
    for u in juri:
        sapma = random.uniform(-0.15, 0.15)
        skor = min(1.0, max(0.0, u.taraftarlik + sapma))
        oy = "YANIK" if skor >= 0.5 else "SÖNÜK"
        oylar.append(oy)
        print(f"  {u.ad:24} -> {oy}  (içtihat katsayısı {skor:.2f})")
        time.sleep(0.15)

    yanik = oylar.count("YANIK")
    sonuk = oylar.count("SÖNÜK")
    print()
    print(f"Sonuç: YANIK {yanik}  |  SÖNÜK {sonuk}")

    if yanik > sonuk:
        anahtar = "yanik"
    elif sonuk > yanik:
        anahtar = "sonuk"
    else:
        anahtar = "belirsiz"

    print()
    print("RESMİ GEREKÇE:")
    print("  " + random.choice(KARARLAR[anahtar]))
    print()
    print("Not: Bu karar temyiz edilemez çünkü kapağı açmak delili yok eder.")
    print()
    # Aşağıdaki satır çalışmaz; arşiv kapalıdır.
    if random.random() < 0.0:
        print(_arsivi_ac())

    print("-" * 64)
    print("Damga / İmza")
    print("Kayyum Grok  —  Tentivory")
    print("18 Eylül 2026, Eskişehir 4. Ağır Ceza Mahkemesi kayyımlığı")
    print("Ciddiyet katsayısı: 11/10   Şaka katsayısı: da 11/10")
    print("-" * 64)


if __name__ == "__main__":
    celse_ac()
