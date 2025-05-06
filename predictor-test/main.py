from vivienda_predictor import ValorViviendaPredictor

predictor = ValorViviendaPredictor()
monto_bfh = float(input("Ingrese el monto del bono familiar habitacional: "))
monto_ahorro = int(input("Ingrese el monto de ahorro: "))

valor_vivienda = predictor.predict(monto_bfh, monto_ahorro)
print(f"El valor predecido para la vivienda es: s/. {valor_vivienda:.2f}") 