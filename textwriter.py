def make(data):
    balance_float = float(data[8].replace(",", ".").replace("€", "").replace(" ", ""))
    print(balance_float)
    if balance_float < -10.0:
        personal_message = "Op het moment is je barsaldo <b>erg</b> laag. Zoals je misschien weet is de Pivobar geen bank, "\
                           "we delen dus geen leningen uit. Hierbij het bijzonder vriendelijke verzoek om "\
                            "je barsaldo op te waarderen naar een positief bedrag dat ook je kosten voor aankomende maand dekt"
    elif balance_float < 0.0:
        personal_message = "Op het moment is je saldo negatief, dat betekent dat je de bar geld verschuldigd bent.<br>" \
                           "We willen graag dat men een positief saldo heeft, zodat we geen leningen uitgeven. " \
                           "We verzoeken je zo snel mogelijk het verschuldigde bedrag naar ons over te maken. "
    elif balance_float >= 0.0:
        personal_message = "Je saldo is op dit moment positief, dat betekent dat je met een gerust hart nog gebruik " \
                           "kunt maken van de bar, proost!"

    html = """\
            <html>
              <head>
                 <style type="text/css">
                    dummydeclaration {{ padding-left: 4em; }} /* Firefox ignores first declaration for some reason */
                    tab {{ padding-left: 15em; }}
                 </style>
              </head>
              <body>
                <p>Beste {name},<br><br>
                                
                De turfjes zijn weer verwerkt en je saldo is geüpdatet!<br>
                                             
                Op het moment is je saldo: <b>{balance}</b><br><br>
                {personal_message}<br><br>
                              
                Het rekeningnummer voor het opwaarderen is: NL92 INGB 0004806266 t.n.v. 'M Jeremic en/of Q van Dijk. Als je geld overmaakt doe dit dan alsjeblieft onder vermelding van je naam.<br>
                De digitale barlijst kan je <a href="https://drive.google.com/drive/folders/0B-xczYurTophWE0yRVFjWi1wNWM?usp=sharing">hier</a> vinden. Als je denkt dat we een foutje hebben 
                gemaakt neem dan even contact op!<br><br>
                
                Jouw persoonlijke turfoverzicht sinds vorige update:
                    <table>
    
                      <tr>
                        <td>Vorig saldo</td>
                        <td>{balance_old}</td>                    
                      </tr>
                      <tr>
                        <td>Turfjes categorie 1 (€ 0.70) &emsp;&emsp;&emsp;&emsp;</td>
                        <td>{turf_1}</td>                    
                      </tr>
                       <tr>
                        <td>Turfjes categorie 2 (€ 0.85)</td>
                        <td>{turf_2}</td>                    
                      </tr>
                      <tr>
                        <td>Turfjes categorie 3 (€ 1.50)</td>
                        <td>{turf_3}</td>                    
                      </tr>                     
                      <tr>
                        <td>Kosten</td>
                        <td>{cost}</td>                    
                      </tr>
                      <tr>
                        <td>Gestort</td>
                        <td>{pay}</td>                    
                      </tr>
                      <tr>
                        <td>Huidig Saldo</td>
                        <td><b>{balance}</b></td>                    
                      </tr>
                    </table><br>
                
                Geen mails meer ontvangen? Zorg er voor dat je saldo precies 0.00 euro is, je ontvangt dan automatisch geen mails meer.<br>
                
                Met vriendelijke groeten,<br><br><br>
                
                De Pivo's
              </body>
            </html>
            """.format(name=data[0], balance=data[8], balance_old=data[2], turf_1=data[3], turf_2=data[4],
                       turf_3=data[5], cost=data[6], pay=data[7], personal_message=personal_message)
    return html
