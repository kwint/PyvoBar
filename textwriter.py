def make(name, balance):

    balance_float = float(balance.replace(",",".").replace("€", "").replace(" ", ""))
    print(balance_float)
    if balance_float < 0.0:
        personal_message = "Op het moment is je saldo negatief, dat betekend dat je de bar geld verschuildigd bent.<br>" \
                           "We willen graag dat men een positief saldo heeft, zodat we geen lening uitgeven" \
                           "We verzoeken je zo snel mogelijk het verschuildigde bedrag naar ons over te maken."
    elif balance_float > 0.0:
        personal_message = "Je saldo is op dit moment positief, dat betekend dat je met een gerust hart nog gebruik " \
                           "kunt maken van de bar, proost!"

    html = """\
            <html>
              <head></head>
              <body>
                <p>Beste {name},<br><br>
                Turfjes zijn weer verwerkt en je saldo is geupdate!<br>
                Op het moment is je saldo: <mark style="background-color:blue"><b>{balance}</b></mark><br><br>
                {personal_message}<br><br>
                
                Het rekeningnummer voor het opwaarderen is: NL92 INGB 0004806266 t.n.v. 'M Jeremic en/of Q van Dijk<br>
                De digitale barlijst kan je <a href="https://drive.google.com/drive/folders/0B-xczYurTophWE0yRVFjWi1wNWM?usp=sharing">hier</a> vinden. Als je denkt dat we een foutje hebben 
                gemaakt neem dan even contact op!<br><br>
                
                Met vriendelijke groeten,<br><br><br>
                
                De Pivo's
              </body>
            </html>
            """.format(name=name, balance=balance, personal_message=personal_message)
    return html
