from Blib import bk_translator
from Blib import format_text


source_lang = "Angličtina"          # zdrojovy jazyk [Angličtina:Angličtina]
target_lang = "Čeština"             # ciloveho jazyk [Angličtina:Čeština]
source_file = "source.txt"
target_file = "target.txt"
time_delay = 2                      # čekání na odezvu serveru v [ 3sec.]
blok_text = 900                     # blok pismen k prekladu [max. 1000]


# nacti soubor jako radky pole
def ziskej_radky_textu(source_file):
    return [line.rstrip('\n') for line in open(source_file)]


def uloz_do_souboru(content):
    if content != "":
        print(content)
        text_file = open(target_file, "a")
        n = text_file.write(content)
        text_file.close()


def prekladej(t_str, driver_form, driver_trans):
    content = ""
    if t_str != "":
        content = bk_translator.preloz_text(t_str, driver_form, time_delay)
        content = bk_translator.preloz_text(content, driver_trans, time_delay)
    uloz_do_souboru(content)


def priprava_prekladu(radky, driver_form, driver_trans):
    prekladana_veta: str = ""
    vety = format_text.sestav_vetu(radky)

    for veta in vety:
        if len(prekladana_veta) + len(veta) > blok_text:
            prekladej(prekladana_veta, driver_form, driver_trans)
            prekladana_veta = ""
            prekladana_veta += veta

        else:
            if veta != "":
                prekladana_veta += veta


def main():
    # ziskej text
    radky_list = ziskej_radky_textu(source_file)
    # Inicialazace driverů
    driver_form = bk_translator.prekladac_cz(source_lang, source_lang)
    driver_trans = bk_translator.prekladac_cz(source_lang, target_lang)
    # zpracovani textu
    priprava_prekladu(radky_list, driver_form, driver_trans)
    # uklid
    # driver_trans.close()
    # driver_form.close()
    print("KONEC!")


if __name__ == '__main__':
    main()
