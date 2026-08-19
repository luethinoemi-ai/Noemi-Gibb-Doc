Website veröffentlichen
=======================

Lernziele
---------

.. important::

   - Ich kann meine Webseite veröffentlichen.
   - Ich kann meine veröffentlichte Webseite vor unerlaubtem Zugriff schützen.

Einleitung
----------

Eine Webseite, die nur lokal auf dem eigenen Computer gespeichert ist, kann von anderen Personen nicht besucht werden.

.. note::

   Im Modul wird dies mit einer Pizza im Tiefkühlfach verglichen.

   Die Pizza ist vorhanden, erfüllt aber ihren eigentlichen Zweck noch nicht.

Eine Webseite sollte öffentlich oder für einen bestimmten Benutzerkreis erreichbar sein.

Webspace und Hosting
--------------------

Damit eine Webseite im Internet erreichbar ist, wird ein Webserver benötigt.

Aufgabe im Modul:

- Anbieter von Webspaces vergleichen
- Preise vergleichen
- Funktionsumfang vergleichen
- Eigene Entscheidung begründen

Zusätzlich soll festgehalten werden:

- Kosten einer eigenen Domain pro Jahr
- Begründung für die Wahl eines Anbieters

.. tip::

   Diese Informationen werden als Portfolioeintrag dokumentiert.

Wichtige rechtliche Aspekte
---------------------------

Beim Veröffentlichen einer Webseite müssen verschiedene Punkte beachtet werden.

.. warning::

   Das Internet ist kein rechtsfreier Raum.

Folgende Themen sind wichtig:

- Impressum
- Urheberrecht
- Standort des Webservers
- Persönlichkeitsschutz

Urheberrecht
~~~~~~~~~~~~

Bilder und Texte dürfen nicht einfach übernommen werden.

.. danger::

   Urheberrechtlich geschützte Bilder dürfen nicht ohne Erlaubnis öffentlich verwendet werden.

Dies gilt auch für:

- Webseiten
- Präsentationen
- öffentlich zugängliche Dokumente

Auch veränderte Bilder können weiterhin erkannt werden.

.. note::

   Smartlearn weist darauf hin, dass spezielle Server urheberrechtliche Verstösse erkennen können.

Persönlichkeitsschutz
~~~~~~~~~~~~~~~~~~~~~

Beim Veröffentlichen von Inhalten müssen die Rechte anderer Personen respektiert werden.

Wichtige Punkte:

- Persönliche Daten schützen
- Rechte anderer Personen respektieren

Impressum
~~~~~~~~~

Beim Veröffentlichen von Webseiten müssen die Anforderungen bezüglich Impressum beachtet werden.

.. important::

   Auch die Webseiten dieses Moduls müssen diese Anforderungen erfüllen.

Portfolioeintrag
----------------

Zu folgenden Punkten soll ein Portfolioeintrag erstellt werden:

- Impressum
- Urheberrecht
- Standort des Webservers
- Persönlichkeitsschutz

Für jeden Punkt soll festgehalten werden:

- Worauf geachtet werden muss
- Welche Anforderungen erfüllt werden müssen

Webseite auf dem Webserver veröffentlichen
------------------------------------------

Für dieses Modul wird ein bereitgestellter Webspace verwendet.

Anmeldung
~~~~~~~~~

Im Lema kann unter:

.. code-block:: text

   sh-web

auf die persönlichen Zugangsdaten zugegriffen werden.

Falls keine Zugangsdaten vorhanden sind:

- Lehrperson kontaktieren

Dateien hochladen
-----------------

Für die Verbindung zum Webserver wird ein SFTP-Programm verwendet.

Beispiel:

.. code-block:: text

   FileZilla

Vorgehen:

1. Datei
2. Servermanager
3. Neuer Server
4. SSH/SFTP-Zugangsdaten eintragen
5. Verbinden

.. note::

   Nach erfolgreicher Verbindung befindet man sich auf dem eigenen Webserver.

Datei ersetzen
--------------

Im Verzeichnis

.. code-block:: text

   /httpdocs

kann die vorhandene

.. code-block:: text

   index.html

durch die eigene Webseite ersetzt werden.

Danach sollte die Webseite über die persönliche Domain erreichbar sein.

Verzeichnis schützen
--------------------

Da die Webseite bewertet wird, soll sie nicht für alle frei zugänglich sein.

Dazu wird ein Passwortschutz eingerichtet.

Datei .htaccess
---------------

Im Verzeichnis

.. code-block:: text

   /httpdocs

wird eine Datei mit folgendem Namen erstellt:

.. code-block:: text

   .htaccess

Beispiel:

.. code-block:: text

   AuthType Basic
   AuthName "Geschützter Bereich"
   AuthUserFile /srv/vhosts/.../tmp/.htpasswd
   Require valid-user

.. important::

   Die Angaben müssen an die eigenen Zugangsdaten angepasst werden.

Datei .htpasswd
---------------

Zusätzlich wird ein Ordner erstellt:

.. code-block:: text

   /tmp

Darin befindet sich eine Datei:

.. code-block:: text

   .htpasswd

Beispiel:

.. code-block:: text

   test:$2a$10$1mSXuMtjtNTl7XxHy/MYp.fl9RQh4ZQLYJtSlz5sVsKcpCtk2xL26

Aufbau:

- Vor dem Doppelpunkt steht der Benutzername.
- Nach dem Doppelpunkt steht der Passwort-Hash.

.. note::

   Der Hash ist nicht das Klartext-Passwort.

Passwortschutz
--------------

Zusammenspiel:

.. code-block:: text

   Besucher
      │
      ▼
   .htaccess
      │
      ▼
   .htpasswd
      │
      ▼
   Zugriff erlaubt

.. important::

   Nur gültige Benutzer erhalten Zugriff auf die Webseite.

Portfolio
---------

Für die Lehrperson sollen zusätzlich dokumentiert werden:

- Benutzername
- Passwort

Damit die Webseite überprüft werden kann.


Domain
~~~~~~

Name einer Website.

Beispiel:

.. code-block:: text

   google.ch

Webspace
~~~~~~~~

Speicherplatz auf einem Webserver.

Dort werden die Dateien einer Website gespeichert.

.htaccess
~~~~~~~~~

Datei für Regeln und Konfigurationen eines Verzeichnisses.

.htpasswd
~~~~~~~~~

Datei mit verschlüsselten Passwörtern.


Prüfungswissen
--------------

.. dropdown:: Was ist der Hauptzweck einer .htaccess-Datei?

   Konfiguration von Einstellungen auf dem Webserver auf Verzeichnisebene.

.. dropdown:: Wofür wird eine .htpasswd-Datei verwendet?

   Zum Speichern von verschlüsselten Passwörtern für die Authentifizierung.

.. dropdown:: Wo wird eine .htaccess-Datei typischerweise gespeichert?

   Im Verzeichnis, das geschützt oder konfiguriert werden soll.

Zusammenfassung
---------------

.. important::

   Für die Veröffentlichung einer Webseite benötigt man:

   - Einen Webserver
   - Einen Webspace
   - Eine Domain

   Für den Schutz der Webseite:

   - .htaccess
   - .htpasswd

Wichtige Themen beim Veröffentlichen:

- Impressum
- Urheberrecht
- Standort des Webservers
- Persönlichkeitsschutz
