__all__ = ['stopwords']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers([])
@Js
def PyJs_anonymous_0_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers([])
    return Js([Js('a'), Js('about'), Js('above'), Js('after'), Js('again'), Js('against'), Js('all'), Js('am'), Js('an'), Js('and'), Js('any'), Js('are'), Js('as'), Js('at'), Js('be'), Js('because'), Js('been'), Js('before'), Js('being'), Js('below'), Js('between'), Js('both'), Js('but'), Js('by'), Js('could'), Js('did'), Js('do'), Js('does'), Js('doing'), Js('down'), Js('during'), Js('each'), Js('few'), Js('for'), Js('from'), Js('further'), Js('had'), Js('has'), Js('have'), Js('having'), Js('he'), Js("he'd"), Js("he'll"), Js("he's"), Js('her'), Js('here'), Js("here's"), Js('hers'), Js('herself'), Js('him'), Js('himself'), Js('his'), Js('how'), Js("how's"), Js('i'), Js("i'd"), Js("i'll"), Js("i'm"), Js("i've"), Js('if'), Js('in'), Js('into'), Js('is'), Js('it'), Js("it's"), Js('its'), Js('itself'), Js("let's"), Js('me'), Js('more'), Js('most'), Js('my'), Js('myself'), Js('nor'), Js('of'), Js('on'), Js('once'), Js('only'), Js('or'), Js('other'), Js('ought'), Js('our'), Js('ours'), Js('ourselves'), Js('out'), Js('over'), Js('own'), Js('same'), Js('she'), Js("she'd"), Js("she'll"), Js("she's"), Js('should'), Js('so'), Js('some'), Js('such'), Js('than'), Js('that'), Js("that's"), Js('the'), Js('their'), Js('theirs'), Js('them'), Js('themselves'), Js('then'), Js('there'), Js("there's"), Js('these'), Js('they'), Js("they'd"), Js("they'll"), Js("they're"), Js("they've"), Js('this'), Js('those'), Js('through'), Js('to'), Js('too'), Js('under'), Js('until'), Js('up'), Js('very'), Js('was'), Js('we'), Js("we'd"), Js("we'll"), Js("we're"), Js("we've"), Js('were'), Js('what'), Js("what's"), Js('when'), Js("when's"), Js('where'), Js("where's"), Js('which'), Js('while'), Js('who'), Js("who's"), Js('whom'), Js('why'), Js("why's"), Js('with'), Js('would'), Js('you'), Js("you'd"), Js("you'll"), Js("you're"), Js("you've"), Js('your'), Js('yours'), Js('yourself'), Js('yourselves')])
PyJs_anonymous_0_._set_name('anonymous')
PyJs_anonymous_0_
pass
pass


# Add lib to the module scope
stopwords = var.to_python()