import unicode.cnv as cnv


def split_convert_to_unicode(letters):
    a = ""
    for letter in letters:
        a = cnv.convert_data_to_unicode(letter) + " " + a
    return a
