
{'date': 'Thu Mar 28 2019 11:30:04.143 GMt-0300 (Hora oficial do Brasil) -X- SuPyGirls -X-',
'error': '''
 module <string> line 7
  faca _ Elemento(FACA)
        ^
SyntaxError: invalid syntax
'''},
{'date': 'Thu Mar 28 2019 11:31:33.323 GMt-0300 (Hora oficial do Brasil) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 7
    faca_Elemento(FACA)
NameError: name 'faca_Elemento' is not defined
'''},