Konstruktoren
=============

Was ist ein Konstruktor?
~~~~~~~~~~~~~~~~~~~~~~~~

Ein Konstruktor wird aufgerufen, wenn ein Objekt erstellt wird.

.. important::

   Konstruktor = Startwerte setzen

Beispiel
~~~~~~~~

.. code-block:: java

   BottleCylindrical bottle1 =
      new BottleCylindrical();

Konstruktor mit Parametern
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: java

   public BottleCylindrical(
      String liquidName,
      int height,
      int diameter,
      double density
   )

Dadurch können Startwerte direkt übergeben werden.

Warum Konstruktoren?
~~~~~~~~~~~~~~~~~~~~

Vorteile:

- Objekte erhalten Startwerte
- Attribute können geprüft werden
- Fehler werden früh erkannt

Beispiel mit Startwerten
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: java

   BottleCylindrical bottle1 =
      new BottleCylindrical(
         "Sandseife",
         20,
         15,
         0.5
      );

Beim Erstellen des Objekts werden die Werte direkt an den Konstruktor übergeben.

Dadurch besitzt das Objekt sofort gültige Startwerte.

.. note::

   Konstruktoren helfen dabei, Objekte direkt in einen definierten Anfangszustand zu bringen.

Zusammenfassung
~~~~~~~~~~~~~~~

.. important::

   Konstruktoren werden beim Erstellen eines Objekts aufgerufen.

   Sie setzen die Startwerte eines Objekts.
