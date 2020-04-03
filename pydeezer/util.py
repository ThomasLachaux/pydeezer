import re
import hashlib


def clean_query(query):
    # A pure copy-paste of regex patterns from DeezloaderRemix
    # I dont know regex

    query = re.sub(r"/ feat[\.]? /g", " ", query)
    query = re.sub(r"/ ft[\.]? /g", " ", query)
    query = re.sub(r"/\(feat[\.]? /g", " ", query)
    query = re.sub(r"/\(ft[\.]? /g", " ", query)
    query = re.sub(r"/\&/g", "", query)
    query = re.sub(r"/–/g", "-", query)
    query = re.sub(r"/–/g", "-", query)

    return query


def save_lyrics(lyric_data, save_path):
    try:
        if not str(save_path).endswith(".lrc"):
            save_path += ".lrc"

        with open(save_path, "w") as f:
            sync_data = lyric_data["LYRICS_SYNC_JSON"]

            for line in sync_data:
                if str(line["line"]):
                    f.write("{0}{1}".format(
                        line["lrc_timestamp"], line["line"]))
                f.write("\n")

        return True
    except Exception as err:
        print("Error", err)
        return False


def get_text_md5(text, encoding="UTF-8"):
    return hashlib.md5(str(text).encode(encoding)).hexdigest()


def get_blowfish_key(track_id):
    secret = 'g4el58wc0zvf9na1'

    m = hashlib.md5()
    m.update(bytes([ord(x) for x in track_id]))
    id_md5 = m.hexdigest()

    blowfish_key = bytes(([(ord(id_md5[i]) ^ ord(id_md5[i+16]) ^ ord(secret[i]))
                           for i in range(16)]))

    return blowfish_key
