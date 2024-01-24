def presenteer(totaal, d = {}):
    for k,v in d.items():
        print(str(k)+ ' : '  + str(v))
    print("=" * 26)
    return f"totaal : {totaal} euro"