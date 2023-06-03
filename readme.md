<h2>Aplikacja wyszukująca potencjalne duplikaty obiektów z danych geolokalizacyjnych</h2>
Krzysztof Jankowski - Czerwiec 2023
<br>
<h3>Opis Problemu</h3>
Zespół analitykow dostaje dane obiektów (fabryki, elektrownie, kopalnie, porty ..) z różnych źródel. Jak to bywa z różnymi źródłami nazwy mogą sie ciut lub nawet bardzo róznić. Np. "Gazoport w Świmoujściu" oraz "Świnoujscie LNG" to to samo. Wychwytywanie duplikatów sprawia sporo problemu i zajmuje dużo czasu. Rozwiazaniem może być porównywanie koordynatów na mapie i zawężenie listy potencjalnych duplikatów do tychy które znajdują się w tym samym miejscu (lub prawie w tym samym miejscu).

<h3>Wymagania</h3>
Aplikacja powinna:
<li> Zaladowac dwa pliki excela z danymi obiektów</li>
<li> Znaleść kolumny "name", "longitute" i "latitude"</li>
<li> Zaokrąglic koordynaty wg podanej przez użytkownika wartości</li>
<li> Porównać dane w obu plikach</li>
<li> Wygenerować plik excela z wynikiem</li>

<h3>Ograniczenia</h3>
Ze względu na brak mozliwości pracy na prawdziwych danych, do testowania został przygotowany generator plikow (plik generator.py).
Skrypt pozwala na wygenerowanie pliku Excel z losowymi nazwami obiektów i koordynatami tych obiektow.

<h3>Aplikacja</h3>
Interfejs aplikacji napisany z użyciem biblioteki TKInter posiada:
<li>przycisk zaladowania pierwszego pliku</li>
<li>przycisk zaladowania drugiego pliku</li>
<li>pole do wpisania ilości miejsc po przecinku do zaookrąglenia koordynatów</li>
<li>przycisk do wygenerowania wyniku koncowego</li>
<li>każdy krok potwierdzany jest komunikatem stanu 'OK' lub '!!!'</li>

Zczytywanie danych, normalizacja, porównywanie danych i generowanie koncowego pliku excela z danymi wynikowymi jest wykonywane z wykorzystaniem bibiloteki Pandas.

<h3>Użytkowanie</h3>
<li>Kliknij 'Open' i wybierz pierwszy plik Excel. Plik musi miec kolumny name, longitute i latitude. Jezeli nie bedzie bledow pojawi sie 'OK' w UI</li>
<li>Kliknij 'Open' i wybierz drugi plik Exce;. Plik musi miec kolumny name, longitute i latitude. Jezeli nie bedzie bledow pojawi sie 'OK' w UI</li>
<li>wpisz do ilu miejsc po przecinku zaokrąglić koordynaty i kliknij 'Update'</li>
<li>wygeneruj wynik klikając 'Generate'</li>

<br>


