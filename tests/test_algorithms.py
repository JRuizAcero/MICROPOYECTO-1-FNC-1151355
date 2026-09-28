"""
Pruebas completas de los algoritmos de transformación a FNC.
"""
import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.models.grammar import Grammar
from src.models.production import Production
from src.parser.grammar_parser import GrammarParser
from src.algorithms.null_productions import NullProductionsEliminator
from src.algorithms.unit_productions import UnitProductionsEliminator
from src.algorithms.useless_symbols import UselessSymbolsEliminator
from src.algorithms.chomsky_converter import ChomskyConverter
from src.algorithms.fnc_validator import FNCValidator


class TestAlgorithms(unittest.TestCase):

    def test_null_productions_elimination(self):
        # S -> ABaC
        # A -> BC | ε
        # B -> b | ε
        # C -> D
        # D -> d
        text = """
        Variables: S, A, B, C, D
        Terminales: a, b, d
        Inicial: S
        Producciones:
        S -> A B a C
        A -> B C | ε
        B -> b | ε
        C -> D
        D -> d
        """
        g = GrammarParser.from_text_definition(text)
        nullable = NullProductionsEliminator.find_nullable_variables(g)
        self.assertIn("A", nullable)
        self.assertIn("B", nullable)
        self.assertNotIn("C", nullable)
        self.assertNotIn("D", nullable)

        g_no_null, step = NullProductionsEliminator.eliminate(g)
        # Comprobar que no queda ninguna regla a epsilon
        self.assertFalse(any(p.is_epsilon() for p in g_no_null.productions))
        self.assertTrue(len(step.removed_productions) >= 2)

    def test_unit_productions_elimination(self):
        # S -> A | a
        # A -> B | b
        # B -> c
        text = """
        Variables: S, A, B
        Terminales: a, b, c
        Inicial: S
        Producciones:
        S -> A | a
        A -> B | b
        B -> c
        """
        g = GrammarParser.from_text_definition(text)
        g_no_unit, step = UnitProductionsEliminator.eliminate(g)
        
        # Ninguna regla debe ser unitaria
        self.assertFalse(any(p.is_unit(g_no_unit.variables) for p in g_no_unit.productions))
        # S debe poder derivar a, b, c
        s_rights = [p.right for p in g_no_unit.get_productions_for("S")]
        self.assertIn(("a",), s_rights)
        self.assertIn(("b",), s_rights)
        self.assertIn(("c",), s_rights)

    def test_useless_symbols_elimination(self):
        # S -> AB | a
        # A -> a
        # B -> BC (B no genera nada terminal)
        # C -> c
        # D -> d (D no es alcanzable desde S)
        text = """
        Variables: S, A, B, C, D
        Terminales: a, b, c, d
        Inicial: S
        Producciones:
        S -> A B | a
        A -> a
        B -> B C
        C -> c
        D -> d
        """
        g = GrammarParser.from_text_definition(text)
        
        # Paso 1: Eliminar no generadoras (B no es generadora, por ende S -> AB se cae)
        g_gen, step_gen = UselessSymbolsEliminator.eliminate_non_generating(g)
        self.assertNotIn("B", g_gen.variables)
        self.assertNotIn(Production.from_string("S", "AB"), g_gen.productions)

        # Paso 2: Eliminar inalcanzables
        g_reach, step_reach = UselessSymbolsEliminator.eliminate_unreachable(g_gen)
        # Como S -> AB fue eliminada al podar B (no generadora), desde S solo queda S -> a.
        # Por ende, A también resulta inalcanzable desde S.
        self.assertNotIn("D", g_reach.variables)
        self.assertNotIn("C", g_reach.variables)
        self.assertNotIn("A", g_reach.variables)
        self.assertIn("S", g_reach.variables)

    def test_full_chomsky_conversion(self):
        # Gramática clásica de libro:
        # S -> a B | b A
        # A -> a | a S | b A A
        # B -> b | b S | a B B
        text = """
        Variables: S, A, B
        Terminales: a, b
        Inicial: S
        Producciones:
        S -> a B | b A
        A -> a | a S | b A A
        B -> b | b S | a B B
        """
        g = GrammarParser.from_text_definition(text)
        
        # 1. Nulas (no hay)
        g1, _ = NullProductionsEliminator.eliminate(g)
        # 2. Unitarias (no hay)
        g2, _ = UnitProductionsEliminator.eliminate(g1)
        # 3. Inútiles
        g3, _ = UselessSymbolsEliminator.eliminate_non_generating(g2)
        g4, _ = UselessSymbolsEliminator.eliminate_unreachable(g3)
        # 4. Sustituir terminales
        g5, _ = ChomskyConverter.substitute_terminals(g4)
        # 5. Binarizar
        g6, _ = ChomskyConverter.reduce_long_productions(g5)

        # Validar con FNCValidator
        validation = FNCValidator.validate(g6)
        self.assertTrue(validation.is_fnc, msg=validation.get_report())


if __name__ == "__main__":
    unittest.main()
