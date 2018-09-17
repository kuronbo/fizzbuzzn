===================
fizzbuzzn(practice)
===================
| 簡単なfizzbuzzプログラムからバージョンアップを繰り返すことで、
| pythonでのプログラムの作り方を学んでいく。

usage (v0.0.2)
--------------
apiはfizzbuzz(num)関数のみ

.. code-block::

    >>> from fizzbuzzn.app import fizzbuzz
    >>> fizzbuzz(1)
    1
    >>> fizzbuzz(15)
    FizzBuzz
    >>> fizzbuzz(0, zeroable=False)
    0
    >>> fizzbuzz(0, zeroable=True)
    FizzBuzz
