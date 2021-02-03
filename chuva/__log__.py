
{'date': 'Thu Oct 10 2019 10:07:19.196 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 70
    a_floresta = FlorestaChuva()
  module <module> line 62
    self.floresta_inicio.esquerda = self.floresta_inicio.meio = self.floresta_inicio.esquerda = Molhado(self.floresta_inicio) 
  module <module> line 49
    self.aqui
AttributeError: 'Molhado' object has no attribute 'aqui'
'''},