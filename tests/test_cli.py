"""Test module for test_cli."""

import io
import unittest
from unittest.mock import MagicMock, patch
from cli.cli import main
from core.player import Player


class TestCLI(unittest.TestCase):
    """Tests para la interfaz CLI del juego."""

    def setUp(self):
        """Configuración común para los tests.

        Creamos mocks para los jugadores que serán devueltos por el juego.
        """
        self.mock_player1 = MagicMock(spec=Player)
        self.mock_player1.get_nombre.return_value = "Dana"
        self.mock_player1.get_ficha.return_value = "Blancas"

        self.mock_player2 = MagicMock(spec=Player)
        self.mock_player2.get_nombre.return_value = "Abi"
        self.mock_player2.get_ficha.return_value = "Negras"

    @patch("builtins.input")
    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("cli.cli.Backgammongame")
    def test_iniciar_juego_y_salir(self, mock_game_class, mock_stdout, mock_input):
        """Simula a un usuario que inicia el juego, introduce nombres y elige la opción 3 (Salir) en
        el primer turno."""
        mock_input.side_effect = [
            "Dana",
            "Abi",
            "3",
        ]

        mock_game_instance = MagicMock()
        mock_game_instance.game_over.side_effect = [False, True] 
        mock_game_instance.get_turno.return_value = self.mock_player1
        mock_game_instance.get_dados.side_effect = [[5, 3], [5, 3]]

        mock_game_instance.movimientos_posibles.return_value = {0: [3, 5]} 
        mock_game_instance.dados_restantes.return_value = True  
        mock_game_instance.get_board.return_value.mostrar_tablero.return_value = [None] * 24
        mock_game_instance.get_banco.return_value = {"Blancas": 0, "Negras": 0}

        mock_game_class.return_value = mock_game_instance

        main()

        output = mock_stdout.getvalue() 
        mock_game_class.assert_called_once()
        self.assertEqual(mock_game_class.call_args[0][0].get_nombre(), "Dana")
        self.assertEqual(mock_game_class.call_args[0][1].get_nombre(), "Abi")
        self.assertIn("Bienvenido al juego 'Backgammons'!", output)

        self.assertIn("Turno de Dana (Blancas)", output)

        self.assertIn("Dados: [5, 3]", output)
        self.assertIn("ESTADO DEL TABLERO", output)  
        self.assertIn("1. Mover ficha", output)
        self.assertIn("2. Rendirse", output)
        self.assertIn("3. Salir del juego", output)
        self.assertIn("Juego finalizado por el usuario", output)
        self.assertIn("¡Hasta luego!", output)

    @patch("builtins.input")
    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("cli.cli.Backgammongame")
    def test_jugar_movimiento_y_rendirse(self, mock_game_class, mock_stdout, mock_input):
        """
        Simula un flujo más largo:
        1. Iniciar juego con nombres.
        2. Turno de Dana, tira dados [5, 3].
        3. Elige Opción 1 (Mover).
        4. Mueve de 1 a 4 (usando el dado 3).
        5. En el mismo turno, elige Opción 2 (Rendirse).
        """
        mock_input.side_effect = [
            "Dana",
            "Abi",
            "1",
            "1",
            "4",
            "2",
        ]

        mock_game_instance = MagicMock()

        mock_game_instance.game_over.side_effect = [False, False, True]
        mock_game_instance.get_turno.return_value = self.mock_player1
        mock_game_instance.get_dados.side_effect = [
            [5, 3],
            [5, 3],
            [5],
        ]
        mock_game_instance.movimientos_posibles.return_value = {0: [3, 5], 1: [4]}

        mock_game_instance.dados_restantes.side_effect = [True, True]
        mock_game_instance.get_board.return_value.mostrar_tablero.return_value = [None] * 24
        mock_game_instance.get_banco.return_value = {"Blancas": 0, "Negras": 0}

        mock_game_class.return_value = mock_game_instance

        main()

        output = mock_stdout.getvalue()

        mock_game_instance.mover_ficha.assert_called_with(0, 3)
        self.assertIn("Turno de Dana (Blancas)", output)  

        self.assertIn("Dados: [5, 3]", output)
        self.assertIn("Movimientos posibles:", output)
        self.assertIn("Desde posicion 1: → [4, 6]", output)
        self.assertIn("Ficha movida de 1 a 4", output)
        self.assertIn("Dados disponibles: [5]", output)
        self.assertIn("Dana se ha rendido", output)
        self.assertIn("¡Gracias por jugar!", output)

    @patch("builtins.input")
    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("cli.cli.Backgammongame")
    def test_sin_movimientos_posibles_pasa_turno(self, mock_game_class, mock_stdout, mock_input):
        """Simula un turno donde el jugador tira dados, pero no hay movimientos posibles, forzando
        un cambio de turno."""
        mock_input.side_effect = [
            "Dana",
            "Abi",
            "3",
        ]

        mock_game_instance = MagicMock()

        mock_game_instance.game_over.side_effect = [False, False, True]
        mock_game_instance.get_turno.side_effect = [self.mock_player1, self.mock_player2]
        mock_game_instance.get_dados.side_effect = [[6, 6], [1, 2], [1, 2]]

        mock_game_instance.movimientos_posibles.side_effect = [{}, {10: [11]}]
        mock_game_instance.dados_restantes.return_value = True
        mock_game_instance.get_board.return_value.mostrar_tablero.return_value = [None] * 24
        mock_game_instance.get_banco.return_value = {"Blancas": 0, "Negras": 0}

        mock_game_class.return_value = mock_game_instance
        main()
        output = mock_stdout.getvalue()
        self.assertIn("Turno de Dana (Blancas)", output) 

        self.assertIn("Dados: [6, 6]", output)
        self.assertIn("No hay movimientos posibles con los dados actuales", output)
        self.assertIn("Turno de Abi (Negras)", output)
        self.assertIn("Dados: [1, 2]", output)
        self.assertIn("1. Mover ficha", output)
        self.assertIn("Juego finalizado por el usuario", output)


if __name__ == "__main__":
    unittest.main()
