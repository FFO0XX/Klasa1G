import uuid  



ksiazka1 = {
    'nazwa': 'Pan Tadeusz',
    'ilość stron': '375',
    'autor': 'Adam Mickiewicz',
    'id': uuid.uuid4()
}

ksiazka2 = {
    'nazwa': 'Balladyna',
    'ilość stron': '170',
    'autor': 'Juliusz Słowacki',
    'id': uuid.uuid4()
}
ksiazka3 = {
    'nazwa': 'Upiorny pociąg. Wiggott przedstawia fantastyczny woskowy świat',
    'ilość stron': '384',
    'autor': 'Terry Deary',
    'id': uuid.uuid4()
}

biblioteka = [ksiazka1,ksiazka2,ksiazka3]