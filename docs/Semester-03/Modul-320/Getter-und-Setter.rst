Getter und Setter
=================

Getter
~~~~~~

Getter lesen Werte aus einem Objekt.

Beispiel:

.. code-block:: java

   getLiquidName()

Merksatz:

.. tip::

   Getter = Lesen

Setter
~~~~~~

Setter schreiben Werte in ein Objekt.

Beispiel:

.. code-block:: java

   setLiquidName("Seife")

Merksatz:

.. tip::

   Setter = Schreiben

Warum Getter und Setter?
~~~~~~~~~~~~~~~~~~~~~~~~

Vorteile:

- Eingaben können geprüft werden
- Daten bleiben geschützt
- Fehler können verhindert werden

Beispiel
~~~~~~~~

.. code-block:: java

   BottleCylindrical bottle1 =
      new BottleCylindrical();

   bottle1.setLiquidName("Sandseife");

   System.out.println(
      bottle1.getLiquidName()
   );

Ablauf:

1. Setter schreibt einen Wert.
2. Getter liest einen Wert.
3. Der Wert wird ausgegeben.

Zusammenfassung
~~~~~~~~~~~~~~~

.. important::

   Getter lesen Werte.

   Setter schreiben Werte.
