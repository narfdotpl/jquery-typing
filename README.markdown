jQuery-typing
=============

Assign callbacks for started/stopped typing events.


Usage
-----

    $(':text').first().typing({
        start: function () {$('body').css('color', 'red');},
        stop: function () {$('body').css('color', 'blue');},
        delay: 400
    });

`typing` command takes key-value object with `start`, `stop` and
`delay` keys. They are all optional, so you can either pass only
`start` callback, `stop` callback, `stop` callback and `delay` time,
or everything.

`delay` is amount of time the plugin waits for another keypress before
judging that typing has stopped; it is expressed in milliseconds and
defaults to 400.


Demo
----

Visit <http://narf.pl/jquery-typing/>


Download
--------

Get production version from
<http://narf.pl/jquery-typing/jquery.typing.min.js>

For development version visit [GitHub][].

  [GitHub]: http://github.com/narfdotpl/jquery-typing
