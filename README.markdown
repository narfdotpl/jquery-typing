jQuery-typing
=============

Assign callbacks for started/stopped typing events.


Usage
-----

    $(':text').typing({
        start: function (event, $elem) {
            $elem.css('background', '#fa0');
        },
        stop: function (event, $elem) {
            $elem.css('background', '#f00');
        },
        delay: 400
    });

`typing` command takes key-value object with `start`, `stop` and
`delay` keys. They are all optional, so you can either pass only
`start` callback, `stop` callback, `stop` callback and `delay` time,
or everything.

`delay` is amount of time the plugin waits for another keypress before
judging that typing has stopped; it is expressed in milliseconds and
defaults to 400. Regardless of `delay`'s value, the `stop` callback is
called immediately when blur event occurs.

Callbacks are passed two arguments: event that caused callback execution
and jQuery object for matched element. Possible events are `keypress`
or `keydown` for `start` callbacks and `keyup` or `blur` for `stop`
callbacks.


Demo
----

Visit <http://narf.pl/jquery-typing/>


Download
--------

Get production version from
<http://narf.pl/jquery-typing/jquery.typing-0.2.0dev.min.js>

For development version visit [GitHub][].

  [GitHub]: http://github.com/narfdotpl/jquery-typing


Meta
----

jQuery-typing is written by [Maciej Konieczny][] and uses
[semantic versioning][] for release numbering.  Everything in `plugin/`
directory is released into the [public domain][].

  [Maciej Konieczny]: http://narf.pl/
  [semantic versioning]: http://semver.org/
  [public domain]: http://unlicense.org/
