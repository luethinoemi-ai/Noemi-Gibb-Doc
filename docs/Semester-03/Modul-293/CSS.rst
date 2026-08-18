CSS
====

Lernziele
~~~~~~~~~~~

.. important::

   - Ich kann erläutern, wozu ein CSS-Styling dient.
   - Ich kann erklären, wie CSS in ein HTML-Dokument eingebunden werden kann.
   - Ich kann die wichtigsten Style-Tags für die Textformatierung nennen.
   - Ich kann Margin und Padding richtig anwenden.
   - Ich kenne das Box-Model und kann es anwenden.
   - Ich kann für meine Webseite einen Background definieren.


Was ist CSS?
~~~~~~~~~~~~~

CSS wird verwendet, um Webseiten zu gestalten.

Während HTML den Inhalt und die Struktur definiert, bestimmt CSS das Aussehen.

.. note::

   HTML beschreibt WAS auf einer Webseite angezeigt wird.

   CSS bestimmt WIE die Webseite aussieht.


Warum CSS?
~~~~~~~~~~~~

Eine Webseite kann mit verschiedenen Stylesheets völlig unterschiedlich aussehen.

.. important::

   Derselbe HTML-Code kann mit verschiedenen CSS-Dateien komplett unterschiedlich dargestellt werden.


HTML und CSS
~~~~~~~~~~~~~~~

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

      =

   Fertige Webseite


CSS einbinden
~~~~~~~~~~~~~~~

Ein Stylesheet wird im Header einer HTML-Datei eingebunden.

.. code-block:: html

   <link rel="stylesheet" href="main.css">


CSS-Datei
~~~~~~~~~~~~

Die Formatierungen werden in einer separaten Datei gespeichert.

Beispiel:

.. code-block:: text

   main.css



CSS Syntax
~~~~~~~~~~~~~~

Ein CSS-Eintrag besteht aus:

- Selektor
- Eigenschaft
- Wert

Beispiel:

.. code-block:: css

   body {
       color: #444;
   }


Selektoren
~~~~~~~~~~~~~~

Selektoren bestimmen, auf welche Elemente ein Stil angewendet wird.

Beispiele:

.. code-block:: css

   body
   #header
   footer



Layout einer Webseite
~~~~~~~~~~~~~~~~~~~~~~~~

Im Smartlearn-Beispiel wird die Webseite in verschiedene Bereiche aufgeteilt:

.. code-block:: text

   Header
   Navigation
   Content
   Sidebar
   Footer


Width
~~~~~~~~

Die Eigenschaft width definiert die Breite eines Elements.

Beispiel:

.. code-block:: css

   width: 800px;


Margin
~~~~~~~~~

Margin beschreibt den Aussenabstand eines Elements.

Beispiel:

.. code-block:: css

   margin: 10px;


Padding
~~~~~~~~~~~

Padding beschreibt den Innenabstand eines Elements.

Beispiel:

.. code-block:: css

   padding: 10px;


Margin und Padding
~~~~~~~~~~~~~~~~~~~~~~

.. important::

   Margin = Abstand ausserhalb

   Padding = Abstand innerhalb


Box Model
~~~~~~~~~~~

Das Box Model beschreibt den Aufbau eines HTML-Elements.

.. code-block:: text

   +----------------------+
   |        Margin        |
   |  +----------------+  |
   |  |    Border      |  |
   |  | +-----------+  |  |
   |  | | Padding   |  |  |
   |  | | Content   |  |  |
   |  | +-----------+  |  |
   |  +----------------+  |
   +----------------------+


Height
~~~~~~~~~

Height definiert die Höhe eines Elements.

.. code-block:: css

   height: 100px;


Background
~~~~~~~~~~~~~

Mit Background wird der Hintergrund eines Elements definiert.

Beispiel:

.. code-block:: css

   background: #333;


Textformatierung
~~~~~~~~~~~~~~~~~~

Wichtige Eigenschaften:

- color
- text-align
- text-decoration


Display
~~~~~~~~

Display bestimmt, wie ein Element dargestellt wird.

.. code-block:: css

   display: block;
   display: inline;
   display: flex;
   display: grid;


Weitere CSS-Themen
~~~~~~~~~~~~~~~~~~~

Folgende Themen werden zusätzlich erwähnt:

- Text
- Fonts
- Links
- Listen
- Tabellen
- Border
- Outline
- Display
- Positioning
- Navigation Bar
- Image Gallery
- Image Transparency
- Image Sprites
- Attribute Selectors


Prüfungswissen
~~~~~~~~~~~~~~~

.. dropdown:: Was macht margin: 10px?

   Der Aussenabstand des Elements wird auf allen Seiten um 10 Pixel erhöht.

.. dropdown:: Was definiert width?

   Die Breite eines Elements.

.. dropdown:: Was passiert, wenn für ein Blockelement keine width definiert wird?

   Es nimmt automatisch die Breite des Elternelements an.

.. dropdown:: Welche Eigenschaft steuert die horizontale Textausrichtung?

   text-align

.. dropdown:: Welche Werte gibt es bei text-align?

   left, right, center, justify

.. dropdown:: Was bedeutet display: inline?

   Das Element verhält sich wie ein Inline-Element.

.. dropdown:: Wofür wird display: flex verwendet?

   Für flexible Containerlayouts.

.. dropdown:: Wofür wird display: grid verwendet?

   Für Rasterlayouts mit Zeilen und Spalten.


Zusammenfassung
~~~~~~~~~~~~~~~~

.. important::

   Die wichtigsten Themen dieses Kapitels:

   - CSS einbinden
   - CSS Syntax
   - CSS Selektoren
   - Width
   - Height
   - Margin
   - Padding
   - Box Model
   - Background
   - Display

.. tip::

   Für Prüfungen besonders wichtig:

   - Margin
   - Padding
   - Box Model
   - Width
   - Display
