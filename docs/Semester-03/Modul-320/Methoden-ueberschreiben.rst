Methoden überschreiben
======================

Was bedeutet überschreiben?
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Eine vorhandene Methode wird angepasst.

Beispiel
~~~~~~~~

Java bietet bereits:

.. code-block:: java

   toString()

an.

Diese Methode kann überschrieben werden.

Beispiel:

.. code-block:: java

   @Override
   public String toString() {

   }

Warum überschreiben?
~~~~~~~~~~~~~~~~~~~~

Die Standardausgabe ist oft nicht sinnvoll.

Durch Überschreiben kann die Ausgabe angepasst werden.

Zusammenfassung
~~~~~~~~~~~~~~~

.. important::

   Überschreiben = vorhandene Methode anpassen

   Häufiges Beispiel:

   toString()
