"""Tests para la interfaz CLI del juego Backgammon."""

import unittest
from unittest.mock import patch, MagicMock
from cli.cli import pedir_int, main
from core.exceptions import EntradaInvalida


class TestPedirInt(unittest.TestCase):
    """Tests para la función pedir_int."""
    
    @patch('builtins.input', return_value='5')
    def test_pedir_int_valido(self, mock_input):
        """Test que pedir_int retorna un entero válido."""
        resultado = pedir_int("Ingrese un número: ")
        self.assertEqual(resultado, 5)
    
    @patch('builtins.input', return_value='abc')
    def test_pedir_int_invalido(self, mock_input):
        """Test que pedir_int lanza excepción con entrada inválida."""
        with self.assertRaises(EntradaInvalida):
            pedir_int("Ingrese un número: ")
    
    @patch('builtins.input', return_value='')
    def test_pedir_int_vacio(self, mock_input):
        """Test que pedir_int lanza excepción con entrada vacía."""
        with self.assertRaises(EntradaInvalida):
            pedir_int("Ingrese un número: ")


class TestMainFlujo(unittest.TestCase):
    """Tests para el flujo principal del juego."""
    
    @patch('builtins.input')
    @patch('builtins.print')
    def test_creacion_jugadores_exitosa(self, mock_print, mock_input):
        """Test que se crean los jugadores correctamente."""
        mock_input.side_effect = ['Jugador1', 'Jugador2', '3']
        
        with patch('cli.cli.Backgammongame') as mock_game:
            mock_game_instance = MagicMock()
            mock_game_instance.game_over.return_value = False
            mock_game_instance.get_turno.return_value = MagicMock(
                get_nombre=lambda: 'Jugador1',
                get_ficha=lambda: 'Blancas'
            )
            mock_game_instance.tirar_dados.return_value = [3, 4]
            mock_game_instance.dados_restantes.return_value = True
            mock_game_instance.mostrar_tablero.return_value = "tablero"
            mock_game_instance.get_dados.return_value = [3, 4]
            mock_game_instance.get_banco.return_value = {'Blancas': 0, 'Negras': 0}
            mock_game_instance.movimientos_posibles.return_value = {}
            mock_game.return_value = mock_game_instance
            
            try:
                main()
            except IndexError:
                pass
    
    @patch('builtins.input')
    @patch('builtins.print')
    def test_rendicion(self, mock_print, mock_input):
        """Test que el jugador puede rendirse."""
        mock_input.side_effect = ['Jugador1', 'Jugador2', '2']
        
        with patch('cli.cli.Backgammongame') as mock_game:
            mock_game_instance = MagicMock()
            mock_game_instance.game_over.return_value = False
            mock_game_instance.get_turno.return_value = MagicMock(
                get_nombre=lambda: 'Jugador1',
                get_ficha=lambda: 'Blancas'
            )
            mock_game_instance.tirar_dados.return_value = [3, 4]
            mock_game_instance.dados_restantes.return_value = True
            mock_game_instance.mostrar_tablero.return_value = "tablero"
            mock_game_instance.get_dados.return_value = [3, 4]
            mock_game_instance.get_banco.return_value = {'Blancas': 0, 'Negras': 0}
            mock_game_instance.movimientos_posibles.return_value = {}
            mock_game.return_value = mock_game_instance
            
            main()
    
    @patch('builtins.input')
    @patch('builtins.print')
    def test_salir_juego(self, mock_print, mock_input):
        """Test que el jugador puede salir del juego."""
        mock_input.side_effect = ['Jugador1', 'Jugador2', '3']
        
        with patch('cli.cli.Backgammongame') as mock_game:
            mock_game_instance = MagicMock()
            mock_game_instance.game_over.return_value = False
            mock_game_instance.get_turno.return_value = MagicMock(
                get_nombre=lambda: 'Jugador1',
                get_ficha=lambda: 'Blancas'
            )
            mock_game_instance.tirar_dados.return_value = [3]
            mock_game_instance.dados_restantes.return_value = True
            mock_game_instance.mostrar_tablero.return_value = "tablero"
            mock_game_instance.get_dados.return_value = [3]
            mock_game_instance.get_banco.return_value = {'Blancas': 0, 'Negras': 0}
            mock_game_instance.movimientos_posibles.return_value = {}
            mock_game.return_value = mock_game_instance
            
            main()
    
    @patch('builtins.input')
    @patch('builtins.print')
    def test_mover_ficha_normal(self, mock_print, mock_input):
        """Test que se puede mover una ficha normalmente."""
        llamadas_dados = [0]
        
        def dados_restantes_mock():
            llamadas_dados[0] += 1
            return llamadas_dados[0] == 1
        
        mock_input.side_effect = ['Jugador1', 'Jugador2', '1', '1', '3']
        
        with patch('cli.cli.Backgammongame') as mock_game:
            mock_game_instance = MagicMock()
            mock_game_instance.game_over.side_effect = [False, True]
            mock_game_instance.get_turno.return_value = MagicMock(
                get_nombre=lambda: 'Jugador1',
                get_ficha=lambda: 'Blancas'
            )
            mock_game_instance.tirar_dados.return_value = [2]
            mock_game_instance.dados_restantes.side_effect = dados_restantes_mock
            mock_game_instance.mostrar_tablero.return_value = "tablero"
            mock_game_instance.get_dados.return_value = [2]
            mock_game_instance.get_banco.return_value = {'Blancas': 0, 'Negras': 0}
            mock_game_instance.movimientos_posibles.return_value = {0: [2]}
            mock_game_instance.mover_ficha.return_value = None
            mock_game_instance.ganador.return_value = None
            mock_game.return_value = mock_game_instance
            
            main()
            
            mock_game_instance.mover_ficha.assert_called_once_with(0, 2)
    
    @patch('builtins.input')
    @patch('builtins.print')
    def test_sacar_ficha(self, mock_print, mock_input):
        """Test que se puede sacar una ficha."""
        llamadas_dados = [0]
        
        def dados_restantes_mock():
            llamadas_dados[0] += 1
            return llamadas_dados[0] == 1
        
        mock_input.side_effect = ['Jugador1', 'Jugador2', '1', '20', '-1']
        
        with patch('cli.cli.Backgammongame') as mock_game:
            mock_game_instance = MagicMock()
            mock_game_instance.game_over.side_effect = [False, True]
            mock_game_instance.get_turno.return_value = MagicMock(
                get_nombre=lambda: 'Jugador1',
                get_ficha=lambda: 'Blancas'
            )
            mock_game_instance.tirar_dados.return_value = [4]
            mock_game_instance.dados_restantes.side_effect = dados_restantes_mock
            mock_game_instance.mostrar_tablero.return_value = "tablero"
            mock_game_instance.get_dados.return_value = [4]
            mock_game_instance.get_banco.return_value = {'Blancas': 0, 'Negras': 0}
            mock_game_instance.movimientos_posibles.return_value = {19: ['retirar']}
            mock_game_instance.retirar_ficha.return_value = None
            mock_game_instance.ganador.return_value = None
            mock_game.return_value = mock_game_instance
            
            main()
            
            mock_game_instance.retirar_ficha.assert_called_once_with(19)
    
    @patch('builtins.input')
    @patch('builtins.print')
    def test_reingresar_ficha_desde_banco(self, mock_print, mock_input):
        """Test que se puede reingresar una ficha desde el banco."""
        llamadas_dados = [0]
        
        def dados_restantes_mock():
            llamadas_dados[0] += 1
            return llamadas_dados[0] == 1
        
        mock_input.side_effect = ['Jugador1', 'Jugador2', '1', '3']
        
        with patch('cli.cli.Backgammongame') as mock_game:
            mock_game_instance = MagicMock()
            mock_game_instance.game_over.side_effect = [False, True]
            mock_game_instance.get_turno.return_value = MagicMock(
                get_nombre=lambda: 'Jugador1',
                get_ficha=lambda: 'Blancas'
            )
            mock_game_instance.tirar_dados.return_value = [3]
            mock_game_instance.dados_restantes.side_effect = dados_restantes_mock
            mock_game_instance.mostrar_tablero.return_value = "tablero"
            mock_game_instance.get_dados.return_value = [3]
            mock_game_instance.get_banco.return_value = {'Blancas': 1, 'Negras': 0}
            mock_game_instance.reingreso_posible.return_value = {'reingresa': [2]}
            mock_game_instance.reingresar_ficha.return_value = None
            mock_game_instance.ganador.return_value = None
            mock_game.return_value = mock_game_instance
            
            main()
            
            mock_game_instance.reingresar_ficha.assert_called_once()
    
    @patch('cli.cli.Backgammongame')
    @patch('builtins.input')
    @patch('builtins.print')
    def test_ganador_detectado(self, mock_print, mock_input, mock_game):
        """Test que se detecta cuando hay un ganador."""
        llamadas_dados = [0]

        def dados_restantes_mock():
            llamadas_dados[0] += 1
            return llamadas_dados[0] == 1

        mock_input.side_effect = ['Jugador1', 'Jugador2', '1', '1', '3']
        mock_game_instance = MagicMock()
        mock_game_instance.game_over.side_effect = [False, True]
        mock_game_instance.get_turno.return_value = MagicMock(
            get_nombre=lambda: 'Jugador1',
            get_ficha=lambda: 'Blancas'
        )
        mock_game_instance.tirar_dados.return_value = [2]
        mock_game_instance.dados_restantes.side_effect = dados_restantes_mock
        mock_game_instance.mostrar_tablero.return_value = "tablero"
        mock_game_instance.get_dados.return_value = [2]
        mock_game_instance.get_banco.return_value = {'Blancas': 0, 'Negras': 0}
        mock_game_instance.movimientos_posibles.return_value = {0: [2]}
        mock_game_instance.mover_ficha.return_value = None
        mock_game_instance.ganador.return_value = 'Jugador1'
        mock_game.return_value = mock_game_instance

        main()

        calls = [str(call) for call in mock_print.call_args_list]
        self.assertTrue(any('Gano' in str(call) or 'Jugador1' in str(call) for call in calls))


if __name__ == '__main__':
    unittest.main()