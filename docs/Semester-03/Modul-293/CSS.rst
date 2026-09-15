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


fr-Einheit
^^^^^^^^^^

Die Einheit ``fr`` verteilt den verfügbaren Platz.

.. code-block:: css

   grid-template-columns: 1fr 2fr 1fr;


Width
~~~~~

Legt die Breite eines Elements fest.

Beispiel:

.. code-block:: css

   width: 300px;

Height
~~~~~~

Legt die Höhe eines Elements fest.

Beispiel:

.. code-block:: css

   height: 150px;

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

Responsive Design
~~~~~~~~~~~~~~~~~~~

Responsive Design bedeutet, dass sich eine Webseite automatisch an verschiedene Bildschirmgrössen anpasst.

Vorteile:

* Smartphone
* Tablet
* Laptop
* Desktop


Viewport Meta Tag
~~~~~~~~~~~~~~~~~~

Damit Webseiten auf mobilen Geräten korrekt dargestellt werden, wird folgender Meta-Tag verwendet:

.. code-block:: html

   <meta name="viewport" content="width=device-width, initial-scale=1.0">

Dieser Tag gehört in den ``<head>`` Bereich einer HTML-Datei.


Media Queries
~~~~~~~~~~~~~~~

Mit Media Queries können verschiedene CSS-Regeln für unterschiedliche Bildschirmgrössen definiert werden.

.. code-block:: css

   @media (max-width: 768px) {
      body {
         background-color: lightgray;
      }
   }


Flexbox
~~~~~~~~

Flexbox wird verwendet, um Elemente flexibel anzuordnen.

.. code-block:: css

   .container {
      display: flex;
   }

Wichtige Eigenschaften:

* justify-content
* align-items
* flex-direction



CSS Grid
~~~~~~~~~

CSS Grid ermöglicht zweidimensionale Layouts.

.. code-block:: css

   .container {
      display: grid;
      grid-template-columns: 1fr 1fr 1fr;
      gap: 10px;
   }


Float
~~~~~~

Mit float können Elemente links oder rechts positioniert werden.

.. code-block:: css

   img {
      float: left;
   }

Heute wird Float häufig durch Flexbox oder Grid ersetzt.



height: 100% vs 100vh
~~~~~~~~~~~~~~~~~~~~~~~

100%
-----

Bezieht sich auf das Elternelement.

100vh
------

Bezieht sich auf die gesamte sichtbare Höhe des Browserfensters.



z-index
~~~~~~~~

Mit z-index wird bestimmt, welches Element im Vordergrund angezeigt wird.

.. code-block:: css

   .overlay {
      position: absolute;
      z-index: 999;
   }


Position
~~~~~~~~

Mit ``position`` können Elemente gezielt platziert werden.

Mögliche Werte:

- static
- relative
- absolute
- fixed
- sticky

.. code-block:: css

   .box {
      position: absolute;
      top: 10px;
      left: 10px;
   }



Border
~~~~~~

Border definiert einen Rahmen um ein Element.

.. code-block:: css

   border: 2px solid black;

Farben
~~~~~~

Farben können als Name, HEX-Wert oder RGB-Wert definiert werden.

.. code-block:: css

   color: red;

   color: #ff0000;

   color: rgb(255,0,0);


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

.. dropdown:: Unterschied zwischen Flexbox und Grid?

   Flexbox arbeitet in einer Dimension
   (Zeile oder Spalte).

   Grid arbeitet in zwei Dimensionen
   (Zeilen und Spalten).


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

   - Width
   - Height
   - Margin
   - Padding
   - Box Model
   - Display
