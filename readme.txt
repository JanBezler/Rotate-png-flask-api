1.  Program korzysta z bibliotek Pillow, NumPy oraz Flask.
    Aby zadziałał, należy dodać je do swojego śdodowiska.
    Można to zrobić za pomocą komendy:

    'pip install pillow numpy flask'

2.  Wszystko, co trzeba zrobić, by usługa działa, to uruchomić skrypt "run.py", np:

    'python run.py'

    (wersja Pythona: python=3.9.2)

3.  Aby skorzystać usługi, należy wysłać zdjęcie w formacie PNG używając metody POST, jak poniżej:

    'curl -F "image=@<input filename>" --output "<output filename>" -X POST <IP hosta>:<port>/rotate'

    gdzie:
        <input filename> - ściażka wraz z nazwą pliku, który chcemy wysłać (np. 'zdjecia/zdjecie123.png')
        <output filename> - nazwa (ścieżka) pliku, do którego ma być zapisany otrzymany plik (np. 'otrzymane.png')
        <IP hosta> - IP urządzenia, na którym działa usługa (domyślnie '127.0.0.1')
        <IP hosta> - numer portu, na którym działa usługa (domyślnie '5000')

    Domyślnie można użyć polecenia:

    'curl -F "image=@zdjecie.png" --output "otrzymane.png" -X POST 127.0.0.1:5000/rotate'