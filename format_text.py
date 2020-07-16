konec_radku = ['.', '?', '!', ";"]  # vycet znaku konce vety


# bool: zjisti zda se radku nachazi konec vety
def obsahuje_radek_konec_vety(radek):
    obs = False
    if radek != "":
        for i in konec_radku:
            if i in radek:
                obs = True
    return obs


# vrati znak ktery reprezentuje konec vety
def dej_rozdelovaci_znak(radek):
    rozdelovaci_znak = ""
    if obsahuje_radek_konec_vety(radek):
        for i in konec_radku:
            if i in radek:
                rozdelovaci_znak = i
    return rozdelovaci_znak


# vrati index znaku ktery reprezentuje konec vety
def dej_index_rozdel_znak(radek, rozdel_znak):
    t_index = 0
    for i in radek:
        t_index += 1
        if rozdel_znak == i:
            break
    return t_index


def sestav_vetu(radky):
    t_str = ""
    vety_list = []

    for radek in radky:
        if radek == None:
            radek = ""
        if radek.isupper():
            vety_list.append(radek.capitalize() + ".")
            radek = ""
            t_str = ""

        if obsahuje_radek_konec_vety(radek):
            while obsahuje_radek_konec_vety(radek):

                rozdel_str = dej_rozdelovaci_znak(radek)
                index_rozdel = dej_index_rozdel_znak(radek, rozdel_str)

                t_str += radek[:index_rozdel] + " "  # cast do tecky
                radek = radek[index_rozdel + 1:]  # smazani uz ulozene casti retezce
                vety_list.append(t_str)  # + " " pridat mezeru??
                t_str = ""
                if len(radek) > 0 & False == obsahuje_radek_konec_vety(radek):
                    t_str = radek + " "
        else:
            t_str += radek + " "

    return vety_list
