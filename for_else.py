kata = input("Masukan Kata : ")
huruf_yang_dicari = input("Masukan Huruf yang dicari : ")


for huruf in kata:
    if huruf == huruf_yang_dicari:
        print("Huruf", huruf_yang_dicari, "ditemukan didalam kata", kata)
        break
else:
    print("Huruf", huruf_yang_dicari, "tidak ditemukan didalam kata", kata)