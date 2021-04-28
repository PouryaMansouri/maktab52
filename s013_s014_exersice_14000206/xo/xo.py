from typing import Literal, Union, Optional


class _Player:
    def __init__(self, name: str, sign: Literal['x', 'o']) -> None:
        self.name = name
        self.sign = sign


class _XOTable:
    xo_map = {k: None for k in range(1, 10)}  # {1:x, 2: None, 3: o, ...}

    def __str__(self):
        map = self.xo_map
        return """
 -----------------
|  {}  |  {}  |  {}  |
 -----------------
|  {}  |  {}  |  {}  |
 -----------------
|  {}  |  {}  |  {}  |
 -----------------
""".format(*[map[i] if map[i] else i for i in map])

    def mark(self, cell_no, sign: str):
        assert isinstance(cell_no, int) and 1 <= cell_no <= 9, "Enter a valid cell no [1, 9]"
        assert not self.xo_map[cell_no], "Cell is filled"
        sign = str(sign).lower()
        assert sign in 'xo', 'Invalid sign' + sign
        self.xo_map[cell_no] = sign


class _XOGame(_XOTable):
    class UnFinishedGameError(Exception):
        "winner: zamani raise mishe k, bazi tamoom nashode bahe, vali winner() ..."
        pass

    class FinishedGameError(Exception):
        "mark: dar zamin k bazi tamoom shde ..."
        pass

    class InvalidCellError(Exception):
        "mark: Che por bashe, che addesh eshtabah bashe va ..."
        pass

    class InvalidPlayer(Exception):
        "mark: palyere voroodi eshtebah bashad!!!"
        pass

    def __init__(self, player1: _Player, player2: _Player) -> None:
        pass

    def _calculate_result(self):
        map = self.xo_map
        for _ in range( 3, 9):
            print(map[0 + _] == map[1 + _] == map[2 + _])

    def mark(self, cell_no, player: Union[_Player, Literal['x', 'o'], int]):
        if isinstance(player, _Player):
            signe = player.sign
        else:
            signe = player
        super().mark(cell_no, signe)
        self._calculate_result()

    def winner(self) -> Optional[_Player]:
        pass


player1 = _Player("Pourya", 'x')
player2 = _Player("Mohammad", 'o')
q = _XOTable()
print(q.xo_map)
q.mark(3, 'x')
print(q.xo_map)
game = _XOGame(player1, player2)
