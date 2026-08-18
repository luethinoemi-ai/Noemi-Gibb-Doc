Formulare
==========

Lernziele
~~~~~~~~~

.. important::

   - Ich kenne das form-Tag und Formular-Elemente.
   - Ich weiss, wie ich lokale Dateien auf den Server kopieren kann.
   - Ich kann versteckte Formular-Elemente übertragen.

Einführung
~~~~~~~~~~

Formulare werden verwendet, um Daten von Benutzern zu erfassen und zu übermitteln.

Jedes Formular wird durch das ``form``-Tag repräsentiert.

Formular-Elemente innerhalb dieses Tags werden automatisch übertragen, sobald das Formular abgeschickt wird.

Grundstruktur eines Formulars
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Grundsätzlich wird ein Formular mit folgendem Element erstellt:

.. code-block:: html

   <form action="" method="" autocomplete="">
      ...
   </form>

.. note::

   Alle Elemente innerhalb des form-Tags gehören zum Formular und werden beim Absenden berücksichtigt.

Aufbau eines Formulars
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: text

   Formular
       │
       ▼
   Eingabefelder
       │
       ▼
   Benutzer gibt Daten ein
       │
       ▼
   Formular absenden
       │
       ▼
   Daten werden übertragen

Formularelemente
~~~~~~~~~~~~~~~~

Ein Formular kann verschiedene Eingabefelder enthalten.

Beispiel:

.. code-block:: html

   <form method="get">
      Name:
      <input type="text" name="name" required />

      <br />

      Alter:
      <input type="number" name="alter" min="18" />

      <br />

      <input type="submit" />
   </form>

.. important::

   Das ``input``-Element wird verwendet, um Eingabefelder zu erstellen.

Validierung
~~~~~~~~~~~

HTML bietet eine clientseitige Validierung.

Diese überprüft Eingaben vor dem Absenden eines Formulars.

.. warning::

   Clientseitige Validierung ist nicht sicher.

   Die Attribute können mit den DevTools verändert werden.

Regeln für Live-Systeme
~~~~~~~~~~~~~~~~~~~~~~~

.. important::

   Clientseitige Validierung

   - Wichtig für die Benutzerfreundlichkeit

   Serverseitige Validierung

   - Wichtig für Integrität und Sicherheit

.. note::

   In diesem Modul wird nur die clientseitige Validierung verwendet.

Validierungsattribute
~~~~~~~~~~~~~~~~~~~~~

required
^^^^^^^^

Erzwingt eine Eingabe.

Beispiel:

.. code-block:: html

   <input type="text"
          name="name"
          required />

.. important::

   Das Feld muss ausgefüllt werden.

novalidate
^^^^^^^^^^

Deaktiviert die Validierung für das gesamte Formular.

Beispiel:

.. code-block:: html

   <form novalidate>
      ...
   </form>

type
^^^^

Die Validierung hängt vom gewählten Typ ab.

Beispiel:

.. code-block:: html

   <input type="email"
          name="email"
          required />

.. note::

   Hier muss eine gültige E-Mail-Adresse eingegeben werden.

min
^^^

Definiert den kleinsten erlaubten Wert.

Beispiel:

.. code-block:: html

   <input type="number"
          min="10" />

max
^^^

Definiert den grössten erlaubten Wert.

Beispiel:

.. code-block:: html

   <input type="number"
          max="99" />

pattern
^^^^^^^

Erwartet ein bestimmtes Eingabemuster.

Beispiel:

.. code-block:: html

   <input type="url"
          pattern="https?://.+" />

.. note::

   Das pattern-Attribut verwendet Regular Expressions.

   Dieses Thema wird in anderen Modulen vertieft.

GET und POST
~~~~~~~~~~~~

Formulare können Daten auf verschiedene Arten übertragen.

Die beiden wichtigsten Methoden sind:

- GET
- POST

Übersicht
^^^^^^^^^

.. code-block:: text

   Formular
      │
      ├── GET
      │      │
      │      └── Daten erscheinen in der URL
      │
      └── POST
             │
             └── Daten befinden sich im Body

Formular mit GET
^^^^^^^^^^^^^^^^

.. code-block:: html

   <form method="get">
      Name:
      <input type="text" name="name" value="Hans Muster" />

      <br />

      Alter:
      <input type="number" name="alter" value="31" />

      <br />

      <input type="submit" />
   </form>

.. note::

   Die übertragenen Daten erscheinen in der URL.

Formular mit POST
^^^^^^^^^^^^^^^^^

.. code-block:: html

   <form method="post">
      Name:
      <input type="text" name="name" value="Hans Muster" />

      <br />

      Alter:
      <input type="number" name="alter" value="31" />

      <br />

      <input type="submit" />
   </form>

.. note::

   Die Daten werden im Body der Anfrage übertragen.

Aufgabe mit DevTools
~~~~~~~~~~~~~~~~~~~~

Beim Abschicken eines Formulars sollen die DevTools geöffnet bleiben.

Beobachtet werden:

- Die URL
- Der Body der Anfrage

.. tip::

   Vergleiche die Unterschiede zwischen GET und POST.

Wichtiger Hinweis
~~~~~~~~~~~~~~~~~

.. warning::

   Werden zuerst Daten mit GET übertragen, bleiben diese in der URL sichtbar.

   Beim anschliessenden POST-Test können Daten dadurch doppelt erscheinen:

   - Einmal in der URL
   - Einmal im Body

   Deshalb sollten die URL-Parameter vor dem POST-Test entfernt werden.

Prüfungswissen
~~~~~~~~~~~~~~

.. dropdown:: Welches HTML-Element wird verwendet, um ein Formular zu erstellen?

   <form>

.. dropdown:: Welches Attribut markiert ein Feld als Pflichtfeld?

   required

.. dropdown:: Welches HTML-Element wird verwendet, um eine Dropdown-Liste zu erstellen?

   <select>

.. dropdown:: Wie wird die Art der Eingabe festgelegt?

   Mit dem type-Attribut des input-Elements.

Zusammenfassung
~~~~~~~~~~~~~~~

.. important::

   Die wichtigsten Elemente und Attribute:

   - form
   - input
   - required
   - novalidate
   - type
   - min
   - max
   - pattern

.. important::

   Die wichtigsten Übertragungsmethoden:

   - GET
   - POST

.. tip::

   Für die Prüfung besonders wichtig:

   - form-Tag
   - required
   - GET
   - POST
   - clientseitige Validierung
   - serverseitige Validierung
