HTML
====

Lernziele
---------

.. important::

   - Ich kenne einfache HTML-Elemente und kann diese anwenden.
   - Ich kenne die HTML-Seitenstruktur.
   - Ich kann erklären, wie eine HTML-Seite aufgebaut ist.
   - Ich kenne Elemente und Attribute.
   - Ich kann Überschriften, Paragrafen und Listen erstellen.

Aufgabe
-------

Im Verlauf dieses Kapitels wird eine einfache Webseite erstellt.

Die Webseite enthält:

- Überschriften
- Absätze
- Tabellen
- Sortierte Listen
- Unsortierte Listen
- Links

Zusätzlich können weitere Elemente ergänzt werden.


Was ist HTML?
-------------

HTML steht für:

.. code-block:: text

   HyperText Markup Language

HTML beschreibt den Aufbau und die Struktur einer Webseite.

.. note::

   HTML definiert den Inhalt einer Webseite.

   CSS gestaltet das Aussehen.

   JavaScript ergänzt Funktionen und Interaktivität.


HTML, CSS und JavaScript
------------------------

Die drei Technologien arbeiten zusammen:

.. code-block:: text

   HTML        -> Inhalt
   CSS         -> Gestaltung
   JavaScript  -> Funktionalität

Beispiel:

   HTML erstellt eine Überschrift.

   CSS bestimmt Farbe und Grösse.

   JavaScript reagiert auf Benutzeraktionen.


HTML-Grundgerüst
----------------

Ein minimales HTML-Dokument:

.. code-block:: html

   <!DOCTYPE html>
   <html lang="de">
     <head>
       <title>Page Title</title>
     </head>
     <body>
       <h1>This is a Heading</h1>
       <p>This is a paragraph.</p>
     </body>
   </html>


HTML-Elemente
-------------

HTML besteht aus Elementen.

Beispiele:

.. code-block:: html

   <h1>Überschrift</h1>

   <p>Absatz</p>

   <ul>
      <li>Element</li>
   </ul>

.. important::

   Ein Element wird normalerweise mit einem Start-Tag und einem End-Tag definiert.


HTML-Attribute
--------------

Attribute liefern zusätzliche Informationen zu einem Element.

Beispiel:

.. code-block:: html

   <a href="https://example.com">
      Link
   </a>

Hier ist:

.. code-block:: text

   href

das Attribut.


Überschriften
-------------

HTML bietet verschiedene Überschriften.

Beispiele:

.. code-block:: html

   <h1>Überschrift 1</h1>
   <h2>Überschrift 2</h2>
   <h3>Überschrift 3</h3>

.. tip::

   h1 ist die wichtigste Überschrift einer Seite.


Absätze
--------

Paragrafen werden mit folgendem Element erstellt:

.. code-block:: html

   <p>Dies ist ein Absatz.</p>


Listen
------

Unsortierte Liste:

.. code-block:: html

   <ul>
      <li>HTML</li>
      <li>CSS</li>
   </ul>

Sortierte Liste:

.. code-block:: html

   <ol>
      <li>Schritt 1</li>
      <li>Schritt 2</li>
   </ol>

.. important::

   <ul> = ungeordnete Liste

   <ol> = geordnete Liste

   <li> = Listeneintrag


Div
---

Das div-Tag gehört zu den meistverwendeten HTML-Tags.

Ein div besitzt keine eigene Bedeutung.

Es wird verwendet, um zusammengehörende Bereiche zu gruppieren.

Beispiel:

.. code-block:: html

   <div>
      <h1>Titel</h1>
      <p>Text</p>
   </div>



Semantische Elemente
--------------------

HTML bietet verschiedene Bereiche für die Struktur einer Webseite.

.. code-block:: text

   header
   nav
   section
   article
   aside
   footer
   details
   summary

- header: Einleitende Inhalte und Navigation
- nav: Navigationslinks
- section: Abschnitt eines Dokuments
- article: Eigenständiger Inhalt
- aside: Zusätzlicher Inhalt oder Seitenleiste
- footer: Fusszeile
- details: Zusätzliche Informationen
- summary: Überschrift für details



Class und ID
------------

Class
~~~~~

Eine Klasse kann mehreren Elementen zugewiesen werden.

Beispiel:

.. code-block:: html

   <p class="info">
      Text
   </p>

ID
~~

Eine ID identifiziert ein einzelnes Element.

Beispiel:

.. code-block:: html

   <div id="header">
      Inhalt
   </div>

.. important::

   Eine ID identifiziert ein einzelnes Element.

   Eine Klasse kann mehrfach verwendet werden.



Styles
------

Mit Styles können Elemente gestaltet werden.

Beispiel:

.. code-block:: html

   <p style="color:red;">
      Roter Text
   </p>



Links
-----

Links verbinden Webseiten miteinander.

Beispiel:

.. code-block:: html

   <a href="https://example.com">
      Website öffnen
   </a>

Wichtige Attribute:

- href
- target

.. note::

   href enthält die Zieladresse.



Bilder
------

Bilder werden mit dem img-Element eingebunden.

Beispiel:

.. code-block:: html

   <img
      src="bild.jpg"
      alt="Beschreibung">

.. important::

   Das alt-Attribut beschreibt das Bild.



Tabellen
--------

Tabelle erstellen:

.. code-block:: html

   <table>
      <tr>
         <th>Name</th>
      </tr>
      <tr>
         <td>Noemi</td>
      </tr>
   </table>

Wichtige Elemente:

- table
- tr
- th
- td



Leerzeilen und Leerschläge
--------------------------

Übung:

Zwischen zwei Paragrafen beliebig viele Leerzeilen und Leerzeichen einfügen.

Beobachtung:

Der Browser stellt den Text trotzdem normal dar.

.. warning::

   Mehrere Leerzeichen oder Leerzeilen werden vom Browser normalerweise zusammengefasst.




Prüfungsfragen
--------------

.. dropdown:: Wofür steht HTML?

   HyperText Markup Language

.. dropdown:: Welches Element definiert einen Absatz?

   <p>

.. dropdown:: Welches Attribut enthält die Zieladresse eines Links?

   href

.. dropdown:: Was ist der Unterschied zwischen Class und ID?

   Eine ID identifiziert ein einzelnes Element.

   Eine Klasse kann mehreren Elementen zugeordnet werden.


Zusammenfassung
---------------

.. important::

   Wichtige HTML-Elemente:

   - h1 bis h6
   - p
   - ul
   - ol
   - li
   - div
   - a
   - img
   - table

   Wichtige Attribute:

   - href
   - src
   - alt
   - class
   - id
   - style
