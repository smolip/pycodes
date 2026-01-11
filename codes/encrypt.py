
text_to_encrypt = (
    "Once upon a midnight dreary, while I pondered, weak and weary,"
    "Over many a quaint and curious volume of forgotten lore, While I nodded, nearly napping, "
    "suddenly there came a tapping, as of some one gently rapping, rapping at my chamber door. "
    "'This some visiter,' I muttered, 'tapping at my chamber door - Only this, and nothing more."
)

lzw_d = {i: chr(i) for i in range(256)}

reversed_lzw_d = {v: k for k, v in lzw_d.items()}

k = len(lzw_d)

w = ""

output_list = []

for c in text_to_encrypt:
    wc = w + c
    if wc in lzw_d:
        w = wc
    else:
        if w in reversed_lzw_d:
            output_list.append(reversed_lzw_d[w])
        lzw_d[k] = wc
        w = c

if len(w) > 0:
    output_list.append(reversed_lzw_d[w])

print(output_list)