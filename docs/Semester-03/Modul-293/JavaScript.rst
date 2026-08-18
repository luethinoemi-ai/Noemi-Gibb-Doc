JavaScript
==========

Lernziele
~~~~~~~~~

.. important::

   - Ich weiss, was JavaScript ist und wie es eingesetzt werden kann.
   - Ich kenne das HTML DOM und kann Objekte ändern.
   - Ich kann weitere Elemente mit JavaScript erstellen, z. B. eine Formularvalidierung oder eine Bildergalerie.

Einführung
~~~~~~~~~~

JavaScript bringt Leben in eine Webseite.

Während HTML den Inhalt einer Webseite definiert und CSS das Aussehen gestaltet, sorgt JavaScript für Funktionen und Interaktivität.

.. note::

   Wer interaktive Webseiten oder Webanwendungen entwickeln möchte, kommt an JavaScript kaum vorbei.

JavaScript im Überblick
~~~~~~~~~~~~~~~~~~~~~~~

Die Möglichkeiten von JavaScript sind sehr vielfältig.

Dieser Kurs vermittelt nur einen kurzen Einblick in die wichtigsten Grundlagen.

.. code-block:: text

   HTML
      │
      ▼
   Inhalt

      +

   CSS
      │
      ▼
   Gestaltung

      +

   JavaScript
      │
      ▼
   Interaktivität

      =

   Moderne Webseite

HTML DOM
~~~~~~~~

Eine der wichtigsten Eigenschaften von JavaScript ist die Bearbeitung des HTML DOM.

DOM steht für:

.. code-block:: text

   Document Object Model

Das DOM stellt die Elemente einer Webseite als Objekte dar.

Dadurch kann JavaScript Elemente finden, verändern oder neue Elemente erstellen.

.. important::

   Mit JavaScript kann der Inhalt einer Webseite während der Laufzeit verändert werden.

DOM vereinfacht erklärt
~~~~~~~~~~~~~~~~~~~~~~~

Man kann sich das DOM als Struktur aller HTML-Elemente einer Webseite vorstellen.

.. code-block:: text

   Webseite
      │
      ▼
   HTML DOM
      │
      ├── Überschrift
      ├── Absatz
      ├── Bild
      └── Formular

JavaScript kann auf diese Elemente zugreifen und sie verändern.

Beispiel: Text anzeigen
~~~~~~~~~~~~~~~~~~~~~~~

Ein leerer Paragraph kann erstellt werden.

Wenn ein Ereignis auftritt, kann JavaScript Text in diesem Paragraphen anzeigen.

Beispiel:

.. code-block:: text

   Ereignis
      │
      ▼
   JavaScript
      │
      ▼
   Text wird angezeigt

.. note::

   Ereignisse können beispielsweise Benutzereingaben oder Fehler sein.

DOM bearbeiten
~~~~~~~~~~~~~~

JavaScript bietet Methoden, um Elemente zu finden.

Beispiel:

.. code-block:: javascript

   document.getElementById()

Mit dieser Methode kann auf ein bestimmtes HTML-Element zugegriffen werden.

Beispiel:

.. code-block:: javascript

   const name = document.getElementById('name')

.. important::

   Das Element wird über seine ID gesucht.

Beispiel: Formularvalidierung
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ein häufiges Einsatzgebiet von JavaScript ist die Formularvalidierung.

Dabei werden Eingaben überprüft.

Beispiele:

- Name muss ausgefüllt sein
- Passwort darf nicht zu kurz sein
- Passwort darf nicht zu lang sein

Ablauf:

.. code-block:: text

   Benutzer füllt Formular aus
             │
             ▼
      JavaScript prüft Eingaben
             │
             ▼
        Fehler gefunden?
          │         │
         Ja        Nein
          │         │
          ▼         ▼
    Fehlermeldung  Formular senden

.. note::

   Im Beispiel werden Fehlermeldungen gesammelt und angezeigt.

Wichtige Bestandteile des Beispiels
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Elemente aus dem Formular:

.. code-block:: javascript

   const name = document.getElementById('name')

   const password = document.getElementById('password')

   const form = document.getElementById('form')

JavaScript reagiert auf das Absenden des Formulars:

.. code-block:: javascript

   form.addEventListener()

Dadurch wird beim Abschicken automatisch eine Prüfung durchgeführt.

HTML5 und Formularvalidierung
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. tip::

   Seit HTML5 können viele Formularvalidierungen direkt mit HTML durchgeführt werden.

Beispiele:

- Mindestlänge
- Maximallänge
- Pflichtfelder

Zusätzlich kann CSS verwendet werden, um Felder optisch hervorzuheben.

Beispiel:

- Grün bei korrekter Eingabe
- Rot bei fehlerhafter Eingabe

Bildkarussell
~~~~~~~~~~~~~

Ein weiteres Beispiel für JavaScript ist ein Bildkarussell.

Dabei werden mehrere Bilder angezeigt und gewechselt.

Ablauf:

.. code-block:: text

   Bild 1
      │
      ▼
   Bild 2
      │
      ▼
   Bild 3
      │
      ▼
   Bild 1

.. note::

   Das Bildkarussell zeigt, wie JavaScript dynamische Inhalte erzeugen kann.

Typische Einsatzgebiete
~~~~~~~~~~~~~~~~~~~~~~~

JavaScript wird in diesem Kapitel verwendet für:

- Bearbeitung des DOM
- Formularvalidierung
- Bildkarusselle
- Anzeige von Inhalten nach Ereignissen

Zusammenfassung
~~~~~~~~~~~~~~~

.. important::

   JavaScript bringt Interaktivität in Webseiten.

   Wichtige Themen:

   - DOM
   - DOM bearbeiten
   - getElementById()
   - Event Listener
   - Formularvalidierung
   - Bildkarussell

.. tip::

   Für die Prüfung besonders wichtig:

   - Bedeutung von JavaScript
   - DOM
   - getElementById()
   - Event Listener
   - Formularvalidierung

Prüfungswissen
~~~~~~~~~~~~~~

.. dropdown:: Was ist das DOM?

   Eine Struktur, die HTML- und XML-Dokumente als Baum von Objekten darstellt.

.. dropdown:: Wofür steht DOM?

   Document Object Model.

.. dropdown:: Wie kann auf ein Element im DOM zugegriffen werden?

   Mit JavaScript-Methoden wie:

   document.getElementById()

.. dropdown:: Was kann JavaScript mit DOM-Elementen machen?

   Elemente finden, ändern oder neue Elemente erstellen.

.. dropdown:: Wofür wird JavaScript in diesem Kapitel verwendet?

   Für DOM-Bearbeitung, Formularvalidierung und Bildkarusselle.
