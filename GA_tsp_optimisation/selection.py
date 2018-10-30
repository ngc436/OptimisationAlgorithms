class Selector:
    def __init__(self, selection_type):
        assert selection_type in ['fitness_proportionate', 'tournament']
        self.selection_type = selection_type

    def selection(self, **kwargs):
        if self.selection_type == 'roulette':
            self._roulette(**kwargs)
        if self.selection_type == 'tournament':
            self._tournament(**kwargs)

    def _roulette(self, **kwargs):
        population = kwargs.get('population')

        raise NotImplementedError

    def _tournament(self, **kwargs):
        raise NotImplementedError
