HTTP-Protokoll
==============

Lernziele
---------

.. important::

   - Ich kenne den Aufbau einer URL.
   - Ich kann erklären, wie ein HTTP-Aufruf funktioniert.
   - Ich weiss, was die Statuscodes bedeuten.

Einführung
----------

HTTP steht für:

.. code-block:: text

   Hypertext Transfer Protocol

HTTP und HTML wurden gemeinsam entwickelt.

Dabei gilt:

- HTTP definiert das Protokoll.
- HTML definiert den Inhalt eines Dokuments.

.. note::

   HTTP beschreibt also, wie Informationen übertragen werden, während HTML beschreibt, wie eine Webseite aufgebaut ist.

Aufbau einer URL
----------------

.. important::

   URL steht für:

   Uniform Resource Locator

   Eine URL ist die Adresse einer Ressource im Internet.


Eine URL dient dazu, eine Ressource eindeutig zu kennzeichnen und zu adressieren.

Beispiel:

.. code-block:: text

   https://www.beispiel.ch:80/pfad/zur/datei.html?key1=value1&key2=value2#anker

Die URL besteht aus mehreren Bestandteilen.

Schema
~~~~~~

Das Schema beschreibt das verwendete Protokoll.

Beispiele:

- http
- https
- ftp
- mailto

Nach dem Protokoll folgt:

.. code-block:: text

   ://

.. tip::

   Browser ergänzen häufig automatisch das Standardprotokoll.

Domäne
~~~~~~

Die Domäne ist der Name einer Website.

Beispiel:

.. code-block:: text

   www.beispiel.ch

Menschen verwenden Domänen, da sie einfacher zu merken sind als IP-Adressen.

Bevor eine Verbindung hergestellt werden kann, übersetzt ein DNS-Server die Domäne in eine IP-Adresse.

Beispiel:

.. code-block:: text

   www.beispiel.ch
   ↓
   192.168.1.1

Fachbegriffe:

- First-Level-Domain
- Second-Level-Domain
- Sub-Domain

.. note::

   Computer kommunizieren über IP-Adressen. Der DNS-Server sorgt dafür, dass der Name einer Website in die passende IP-Adresse übersetzt wird.

.. important::

   Domäne = Name einer Website

   DNS = Übersetzer

   IP-Adresse = Adresse des Servers


Port
~~~~

Der Port bestimmt, über welchen Netzwerkanschluss kommuniziert wird.

Standardwerte:

.. code-block:: text

   HTTP  -> 80
   HTTPS -> 443

Manchmal werden andere Ports verwendet.

Beispiel:

.. code-block:: text

   8080

Dann muss der Port in der URL angegeben werden.

Pfad
~~~~

Der Pfad beschreibt den Speicherort einer Datei auf dem Webserver.

Beispiel:

.. code-block:: text

   /pfad/zur/datei.html

Wenn kein Dateiname angegeben wird, liefert der Server automatisch:

.. code-block:: text

   index.html

Argumente
~~~~~~~~~

Argumente dienen dazu, Daten an den Server zu übermitteln.

Die Übertragung erfolgt als Schlüssel-Wert-Paare.

Beispiel:

.. code-block:: text

   ?key1=value1&key2=value2

Wichtig:

- Das Fragezeichen startet die Argumente.
- Das kaufmännische UND (&) trennt die Werte.

Anker
~~~~~

Der Anker wird mit dem Zeichen:

.. code-block:: text

   #

eingeleitet.

Existiert dieser Anker auf der Seite, springt der Browser direkt zu diesem Abschnitt.

Zusammenfassung URL
-------------------

.. important::

   Eine URL besteht aus:

   - Schema
   - Domäne
   - Port
   - Pfad
   - Argumenten
   - Anker

Geschichte von HTTP
-------------------

1989
~~~~

- Entwicklung von HTTP
- Entwicklung von HTML
- Entwicklung des URL-Konzepts

1996 - HTTP/1.0
~~~~~~~~~~~~~~~

- Veröffentlichung von HTTP/1.0
- Jedes Objekt benötigt eine neue Verbindung
- Auch Bilder benötigen eigene Verbindungen

1999 - HTTP/1.1
~~~~~~~~~~~~~~~

- Einführung zusammen mit HTML 4.01
- Problem der vielen Verbindungen wird verbessert
- Daten können nun auch an den Server gesendet werden

2015 - HTTP/2
~~~~~~~~~~~~~

- Mehrere Anfragen können zusammengefasst werden
- Kürzere Antwortzeiten
- Datenkompression
- Push-Verfahren

2022 - HTTP/3
~~~~~~~~~~~~~

- Aktuellste Version
- Verwendet QUIC statt TCP
- TLS 1.3 ist integriert
- Schnellere Ladezeiten
- Höhere Sicherheit

Wie funktioniert HTTP?
----------------------

HTTP arbeitet nach dem Client-Server-Modell.

Beteiligte:

.. code-block:: text

   Client (Browser)
          |
       Request
          |
          v
        Server
          |
      Response
          |
          v
   Client (Browser)

Ablauf:

1. Der Browser sendet eine Anfrage (Request).
2. Der Server verarbeitet die Anfrage.
3. Der Server sendet eine Antwort (Response).

.. note::

   Jede Anfrage und jede Antwort enthält einen Header und einen Body.

Request und Response
--------------------

Eine Anfrage (Request) enthält:

- Header
- Body

Eine Antwort (Response) enthält:

- Header
- Body

Der Header enthält Informationen über die Kommunikation.

Status Codes
------------

Jede Response enthält einen Statuscode.

Wichtige Statuscodes:

.. code-block:: text

   200 OK
   404 Not Found
   500 Internal Server Error

200 OK
~~~~~~

Die Anfrage war erfolgreich.

404 Not Found
~~~~~~~~~~~~~

Die angeforderte Ressource wurde nicht gefunden.

Mögliche Ursache:

- Falscher Pfad

500 Internal Server Error
~~~~~~~~~~~~~~~~~~~~~~~~~

Der Server hat einen Fehler festgestellt.

Dies tritt häufig bei dynamischen Anwendungen auf.

.. warning::

   Statuscodes sind prüfungsrelevant.

Request-Methoden
----------------

HTTP definiert verschiedene Methoden.

Diese werden auch als Verbs bezeichnet.

GET
~~~

Mit GET werden Daten abgefragt.

Eigenschaften:

- Daten werden über die URL übertragen.
- Der Request-Body bleibt leer.

POST
~~~~

Mit POST werden Daten an den Server geschickt.

Eigenschaften:

- Daten befinden sich im Request-Body.
- Daten sind nicht sichtbar in der URL.

.. tip::

   Formulare werden in der Regel mit POST gesendet.

PUT
~~~

PUT wird verwendet, um Objekte zu erstellen oder zu aktualisieren.

Bei mehrfacher Ausführung mit denselben Daten entsteht nicht mehrfach dieselbe Ressource.

DELETE
~~~~~~

DELETE dient zum Löschen einer Ressource.

OPTIONS
~~~~~~~

OPTIONS zeigt, welche Methoden von einer URL unterstützt werden.

HEAD
~~~~

HEAD liefert nur die Header-Informationen.

Wichtige Regel
--------------

.. important::

   Bei statischen Webseiten werden hauptsächlich GET und POST verwendet.

   - GET für Anfragen
   - POST für Formulare

Zusammenfassung
---------------

- Eine URL besteht aus mehreren Bestandteilen.
- HTTP verwendet Requests und Responses.
- Jede Response besitzt einen Statuscode.
- Die wichtigsten Statuscodes sind 200, 404 und 500.
- Die wichtigsten Methoden sind GET und POST.
- HTTP basiert auf einem Client-Server-Modell.


Prüfungswissen
--------------

.. dropdown:: Wofür steht URL?

   Uniform Resource Locator

.. dropdown:: Aus welchen Bestandteilen besteht eine URL?

   - Schema
   - Domäne
   - Port
   - Pfad
   - Argumente
   - Anker

.. dropdown:: Welcher Standard-Port wird für HTTP verwendet?

   80

.. dropdown:: Welcher Standard-Port wird für HTTPS verwendet?
   443

