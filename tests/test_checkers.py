import unittest
from checkers import *

class TestCheckers(unittest.TestCase):
    # constructor function for the unittests
    ## create checkers board with tiles and pieces with the create_board function
    @classmethod
    def setUp(cls):
        #init board class
        game_board = GameBoard()
        #fill board with tiles and pieces
        game_board.fill_board()
        #filled board object
        cls.board = game_board.get_board()

#Tests
## check if location on the board has a white color as intended after fill_board()
    def test_tile_color_is_white_on_location_0_0(self):
        self.assertEqual(self.board[0][0].get_color(),TileColor.WHITE)

    def test_tile_color_is_white_on_location_0_2(self):
        self.assertEqual(self.board[0][2].get_color(),TileColor.WHITE)

    def test_tile_color_is_white_on_location_0_4(self):
        self.assertEqual(self.board[0][4].get_color(),TileColor.WHITE)

    def test_tile_color_is_white_on_location_0_6(self):
        self.assertEqual(self.board[0][6].get_color(),TileColor.WHITE)

    def test_tile_color_is_white_on_location_0_8(self):
        self.assertEqual(self.board[0][8].get_color(),TileColor.WHITE)

    def test_tile_color_is_white_on_location_1_1(self):
        self.assertEqual(self.board[1][1].get_color(),TileColor.WHITE)

    def test_tile_color_is_white_on_location_1_3(self):
        self.assertEqual(self.board[1][3].get_color(),TileColor.WHITE)

    def test_tile_color_is_white_on_location_1_5(self):
        self.assertEqual(self.board[1][5].get_color(),TileColor.WHITE)

    def test_tile_color_is_white_on_location_1_7(self):
        self.assertEqual(self.board[1][7].get_color(),TileColor.WHITE)

    def test_tile_color_is_white_on_location_1_9(self):
        self.assertEqual(self.board[1][9].get_color(),TileColor.WHITE)

    def test_tile_color_is_white_on_location_2_0(self):
        self.assertEqual(self.board[2][0].get_color(),TileColor.WHITE)

    def test_tile_color_is_white_on_location_2_2(self):
        self.assertEqual(self.board[2][2].get_color(),TileColor.WHITE)

    def test_tile_color_is_white_on_location_2_4(self):
        self.assertEqual(self.board[2][4].get_color(),TileColor.WHITE)

    def test_tile_color_is_white_on_location_2_6(self):
        self.assertEqual(self.board[2][6].get_color(),TileColor.WHITE)

    def test_tile_color_is_white_on_location_2_8(self):
        self.assertEqual(self.board[2][8].get_color(),TileColor.WHITE)

    def test_tile_color_is_white_on_location_3_1(self):
        self.assertEqual(self.board[3][1].get_color(),TileColor.WHITE)

    def test_tile_color_is_white_on_location_3_3(self):
        self.assertEqual(self.board[3][3].get_color(),TileColor.WHITE)

    def test_tile_color_is_white_on_location_3_5(self):
        self.assertEqual(self.board[3][5].get_color(),TileColor.WHITE)

    def test_tile_color_is_white_on_location_3_7(self):
        self.assertEqual(self.board[3][7].get_color(),TileColor.WHITE)

    def test_tile_color_is_white_on_location_3_9(self):
        self.assertEqual(self.board[3][9].get_color(),TileColor.WHITE)

    def test_tile_color_is_white_on_location_4_0(self):
        self.assertEqual(self.board[4][0].get_color(),TileColor.WHITE)

    def test_tile_color_is_white_on_location_4_2(self):
        self.assertEqual(self.board[4][2].get_color(),TileColor.WHITE)

    def test_tile_color_is_white_on_location_4_4(self):
        self.assertEqual(self.board[4][4].get_color(),TileColor.WHITE)

    def test_tile_color_is_white_on_location_4_6(self):
        self.assertEqual(self.board[4][6].get_color(),TileColor.WHITE)

    def test_tile_color_is_white_on_location_4_8(self):
        self.assertEqual(self.board[4][8].get_color(),TileColor.WHITE)

    def test_tile_color_is_white_on_location_5_1(self):
        self.assertEqual(self.board[5][1].get_color(),TileColor.WHITE)

    def test_tile_color_is_white_on_location_5_3(self):
        self.assertEqual(self.board[5][3].get_color(),TileColor.WHITE)

    def test_tile_color_is_white_on_location_5_5(self):
        self.assertEqual(self.board[5][5].get_color(),TileColor.WHITE)

    def test_tile_color_is_white_on_location_5_7(self):
        self.assertEqual(self.board[5][7].get_color(),TileColor.WHITE)

    def test_tile_color_is_white_on_location_5_9(self):
        self.assertEqual(self.board[5][9].get_color(),TileColor.WHITE)

    def test_tile_color_is_white_on_location_6_0(self):
        self.assertEqual(self.board[6][0].get_color(),TileColor.WHITE)

    def test_tile_color_is_white_on_location_6_2(self):
        self.assertEqual(self.board[6][2].get_color(),TileColor.WHITE)

    def test_tile_color_is_white_on_location_6_4(self):
        self.assertEqual(self.board[6][4].get_color(),TileColor.WHITE)

    def test_tile_color_is_white_on_location_6_6(self):
        self.assertEqual(self.board[6][6].get_color(),TileColor.WHITE)

    def test_tile_color_is_white_on_location_6_8(self):
        self.assertEqual(self.board[6][8].get_color(),TileColor.WHITE)

    def test_tile_color_is_white_on_location_7_1(self):
        self.assertEqual(self.board[7][1].get_color(),TileColor.WHITE)

    def test_tile_color_is_white_on_location_7_3(self):
        self.assertEqual(self.board[7][3].get_color(),TileColor.WHITE)

    def test_tile_color_is_white_on_location_7_5(self):
        self.assertEqual(self.board[7][5].get_color(),TileColor.WHITE)

    def test_tile_color_is_white_on_location_7_7(self):
        self.assertEqual(self.board[7][7].get_color(),TileColor.WHITE)

    def test_tile_color_is_white_on_location_7_9(self):
        self.assertEqual(self.board[7][9].get_color(),TileColor.WHITE)

    def test_tile_color_is_white_on_location_8_0(self):
        self.assertEqual(self.board[8][0].get_color(),TileColor.WHITE)

    def test_tile_color_is_white_on_location_8_2(self):
        self.assertEqual(self.board[8][2].get_color(),TileColor.WHITE)

    def test_tile_color_is_white_on_location_8_4(self):
        self.assertEqual(self.board[8][4].get_color(),TileColor.WHITE)

    def test_tile_color_is_white_on_location_8_6(self):
        self.assertEqual(self.board[8][6].get_color(),TileColor.WHITE)

    def test_tile_color_is_white_on_location_8_8(self):
        self.assertEqual(self.board[8][8].get_color(),TileColor.WHITE)

    def test_tile_color_is_white_on_location_9_1(self):
        self.assertEqual(self.board[9][1].get_color(),TileColor.WHITE)

    def test_tile_color_is_white_on_location_9_3(self):
        self.assertEqual(self.board[9][3].get_color(),TileColor.WHITE)

    def test_tile_color_is_white_on_location_9_5(self):
        self.assertEqual(self.board[9][5].get_color(),TileColor.WHITE)

    def test_tile_color_is_white_on_location_9_7(self):
        self.assertEqual(self.board[9][7].get_color(),TileColor.WHITE)

    def test_tile_color_is_white_on_location_9_9(self):
        self.assertEqual(self.board[9][9].get_color(),TileColor.WHITE)

## check if location on the board has a black color as intended after fill_board()

    def test_tile_color_is_black_on_location_0_1(self):
        self.assertEqual(self.board[0][1].get_color(),TileColor.BLACK)

    def test_tile_color_is_black_on_location_0_3(self):
        self.assertEqual(self.board[0][3].get_color(),TileColor.BLACK)

    def test_tile_color_is_black_on_location_0_5(self):
        self.assertEqual(self.board[0][5].get_color(),TileColor.BLACK)

    def test_tile_color_is_black_on_location_0_7(self):
        self.assertEqual(self.board[0][7].get_color(), TileColor.BLACK)

    def test_tile_color_is_black_on_location_0_9(self):
        self.assertEqual(self.board[0][9].get_color(),TileColor.BLACK)

    def test_tile_color_is_black_on_location_1_0(self):
        self.assertEqual(self.board[1][0].get_color(),TileColor.BLACK)

    def test_tile_color_is_black_on_location_1_2(self):
        self.assertEqual(self.board[1][2].get_color(),TileColor.BLACK)

    def test_tile_color_is_black_on_location_1_4(self):
        self.assertEqual(self.board[1][4].get_color(),TileColor.BLACK)

    def test_tile_color_is_black_on_location_1_6(self):
        self.assertEqual(self.board[1][6].get_color(),TileColor.BLACK)

    def test_tile_color_is_black_on_location_1_8(self):
        self.assertEqual(self.board[1][8].get_color(),TileColor.BLACK)

    def test_tile_color_is_black_on_location_2_1(self):
        self.assertEqual(self.board[2][1].get_color(),TileColor.BLACK)

    def test_tile_color_is_black_on_location_2_3(self):
        self.assertEqual(self.board[2][3].get_color(),TileColor.BLACK)

    def test_tile_color_is_black_on_location_2_5(self):
        self.assertEqual(self.board[2][5].get_color(),TileColor.BLACK)

    def test_tile_color_is_black_on_location_2_7(self):
        self.assertEqual(self.board[2][7].get_color(),TileColor.BLACK)

    def test_tile_color_is_black_on_location_2_9(self):
        self.assertEqual(self.board[2][9].get_color(),TileColor.BLACK)

    def test_tile_color_is_black_on_location_3_0(self):
        self.assertEqual(self.board[3][0].get_color(),TileColor.BLACK)

    def test_tile_color_is_black_on_location_3_2(self):
        self.assertEqual(self.board[3][2].get_color(),TileColor.BLACK)

    def test_tile_color_is_black_on_location_3_4(self):
        self.assertEqual(self.board[3][4].get_color(),TileColor.BLACK)

    def test_tile_color_is_black_on_location_3_6(self):
        self.assertEqual(self.board[3][6].get_color(),TileColor.BLACK)

    def test_tile_color_is_black_on_location_3_8(self):
        self.assertEqual(self.board[3][8].get_color(),TileColor.BLACK)

    def test_tile_color_is_black_on_location_4_1(self):
        self.assertEqual(self.board[4][1].get_color(),TileColor.BLACK)

    def test_tile_color_is_black_on_location_4_3(self):
        self.assertEqual(self.board[4][3].get_color(),TileColor.BLACK)

    def test_tile_color_is_black_on_location_4_5(self):
        self.assertEqual(self.board[4][5].get_color(),TileColor.BLACK)

    def test_tile_color_is_black_on_location_4_7(self):
        self.assertEqual(self.board[4][7].get_color(),TileColor.BLACK)

    def test_tile_color_is_black_on_location_4_9(self):
        self.assertEqual(self.board[4][9].get_color(),TileColor.BLACK)

    def test_tile_color_is_black_on_location_5_0(self):
        self.assertEqual(self.board[5][0].get_color(),TileColor.BLACK)

    def test_tile_color_is_black_on_location_5_2(self):
        self.assertEqual(self.board[5][2].get_color(),TileColor.BLACK)

    def test_tile_color_is_black_on_location_5_4(self):
        self.assertEqual(self.board[5][4].get_color(),TileColor.BLACK)

    def test_tile_color_is_black_on_location_5_6(self):
        self.assertEqual(self.board[5][6].get_color(),TileColor.BLACK)

    def test_tile_color_is_black_on_location_5_8(self):
        self.assertEqual(self.board[5][8].get_color(),TileColor.BLACK)

    def test_tile_color_is_black_on_location_6_1(self):
        self.assertEqual(self.board[6][1].get_color(),TileColor.BLACK)

    def test_tile_color_is_black_on_location_6_3(self):
        self.assertEqual(self.board[6][3].get_color(),TileColor.BLACK)

    def test_tile_color_is_black_on_location_6_5(self):
        self.assertEqual(self.board[6][5].get_color(),TileColor.BLACK)

    def test_tile_color_is_black_on_location_6_7(self):
        self.assertEqual(self.board[6][7].get_color(),TileColor.BLACK)

    def test_tile_color_is_black_on_location_6_9(self):
        self.assertEqual(self.board[6][9].get_color(),TileColor.BLACK)

    def test_tile_color_is_black_on_location_7_0(self):
        self.assertEqual(self.board[7][0].get_color(),TileColor.BLACK)

    def test_tile_color_is_black_on_location_7_2(self):
        self.assertEqual(self.board[7][2].get_color(),TileColor.BLACK)

    def test_tile_color_is_black_on_location_7_4(self):
        self.assertEqual(self.board[7][4].get_color(),TileColor.BLACK)

    def test_tile_color_is_black_on_location_7_6(self):
        self.assertEqual(self.board[7][6].get_color(),TileColor.BLACK)

    def test_tile_color_is_black_on_location_7_8(self):
        self.assertEqual(self.board[7][8].get_color(),TileColor.BLACK)

    def test_tile_color_is_black_on_location_8_1(self):
        self.assertEqual(self.board[8][1].get_color(),TileColor.BLACK)

    def test_tile_color_is_black_on_location_8_3(self):
        self.assertEqual(self.board[8][3].get_color(),TileColor.BLACK)

    def test_tile_color_is_black_on_location_8_5(self):
        self.assertEqual(self.board[8][5].get_color(),TileColor.BLACK)

    def test_tile_color_is_black_on_location_8_7(self):
        self.assertEqual(self.board[8][7].get_color(),TileColor.BLACK)

    def test_tile_color_is_black_on_location_8_9(self):
        self.assertEqual(self.board[8][9].get_color(),TileColor.BLACK)

    def test_tile_color_is_black_on_location_9_0(self):
        self.assertEqual(self.board[9][0].get_color(),TileColor.BLACK)

    def test_tile_color_is_black_on_location_9_2(self):
        self.assertEqual(self.board[9][2].get_color(),TileColor.BLACK)

    def test_tile_color_is_black_on_location_9_4(self):
        self.assertEqual(self.board[9][4].get_color(),TileColor.BLACK)

    def test_tile_color_is_black_on_location_9_6(self):
        self.assertEqual(self.board[9][6].get_color(),TileColor.BLACK)

    def test_tile_color_is_black_on_location_9_8(self):
        self.assertEqual(self.board[9][8].get_color(),TileColor.BLACK)

## black tile has piece after fill_board()
    def test_black_tile_has_piece_on_location_0_1(self):
        self.assertIsNotNone(self.board[0][1].get_piece())

    def test_black_tile_has_piece_on_location_0_3(self):
        self.assertIsNotNone(self.board[0][3].get_piece())

    def test_black_tile_has_piece_on_location_0_5(self):
        self.assertIsNotNone(self.board[0][5].get_piece())

    def test_black_tile_has_piece_on_location_0_7(self):
        self.assertIsNotNone(self.board[0][7].get_piece())

    def test_black_tile_has_piece_on_location_0_9(self):
        self.assertIsNotNone(self.board[0][9].get_piece())

    def test_black_tile_has_piece_on_location_1_0(self):
        self.assertIsNotNone(self.board[1][0].get_piece())

    def test_black_tile_has_piece_on_location_1_2(self):
        self.assertIsNotNone(self.board[1][2].get_piece())

    def test_black_tile_has_piece_on_location_1_4(self):
        self.assertIsNotNone(self.board[1][4].get_piece())

    def test_black_tile_has_piece_on_location_1_6(self):
        self.assertIsNotNone(self.board[1][6].get_piece())

    def test_black_tile_has_piece_on_location_1_8(self):
        self.assertIsNotNone(self.board[1][8].get_piece())

    def test_black_tile_has_piece_on_location_2_1(self):
        self.assertIsNotNone(self.board[2][1].get_piece())

    def test_black_tile_has_piece_on_location_2_3(self):
        self.assertIsNotNone(self.board[2][3].get_piece())

    def test_black_tile_has_piece_on_location_2_5(self):
        self.assertIsNotNone(self.board[2][5].get_piece())

    def test_black_tile_has_piece_on_location_2_7(self):
        self.assertIsNotNone(self.board[2][7].get_piece())

    def test_black_tile_has_piece_on_location_2_9(self):
        self.assertIsNotNone(self.board[2][9].get_piece())

    def test_black_tile_has_piece_on_location_3_0(self):
        self.assertIsNotNone(self.board[3][0].get_piece())

    def test_black_tile_has_piece_on_location_3_2(self):
        self.assertIsNotNone(self.board[3][2].get_piece())

    def test_black_tile_has_piece_on_location_3_4(self):
        self.assertIsNotNone(self.board[3][4].get_piece())

    def test_black_tile_has_piece_on_location_3_6(self):
        self.assertIsNotNone(self.board[3][6].get_piece())

    def test_black_tile_has_piece_on_location_3_8(self):
        self.assertIsNotNone(self.board[3][8].get_piece())


    def test_black_tile_has_piece_on_location_6_1(self):
        self.assertIsNotNone(self.board[6][1].get_piece())

    def test_black_tile_has_piece_on_location_6_3(self):
        self.assertIsNotNone(self.board[6][3].get_piece())

    def test_black_tile_has_piece_on_location_6_5(self):
        self.assertIsNotNone(self.board[6][5].get_piece())

    def test_black_tile_has_piece_on_location_6_7(self):
        self.assertIsNotNone(self.board[6][7].get_piece())

    def test_black_tile_has_piece_on_location_6_9(self):
        self.assertIsNotNone(self.board[6][9].get_piece())

    def test_black_tile_has_piece_on_location_7_0(self):
        self.assertIsNotNone(self.board[7][0].get_piece())

    def test_black_tile_has_piece_on_location_7_2(self):
        self.assertIsNotNone(self.board[7][2].get_piece())

    def test_black_tile_has_piece_on_location_7_4(self):
        self.assertIsNotNone(self.board[7][4].get_piece())

    def test_black_tile_has_piece_on_location_7_6(self):
        self.assertIsNotNone(self.board[7][6].get_piece())

    def test_black_tile_has_piece_on_location_7_8(self):
        self.assertIsNotNone(self.board[7][8].get_piece())

    def test_black_tile_has_piece_on_location_8_1(self):
        self.assertIsNotNone(self.board[8][1].get_piece())

    def test_black_tile_has_piece_on_location_8_3(self):
        self.assertIsNotNone(self.board[8][3].get_piece())

    def test_black_tile_has_piece_on_location_8_5(self):
        self.assertIsNotNone(self.board[8][5].get_piece())

    def test_black_tile_has_piece_on_location_8_7(self):
        self.assertIsNotNone(self.board[8][7].get_piece())

    def test_black_tile_has_piece_on_location_8_9(self):
        self.assertIsNotNone(self.board[8][9].get_piece())

    def test_black_tile_has_piece_on_location_9_0(self):
        self.assertIsNotNone(self.board[9][0].get_piece())

    def test_black_tile_has_piece_on_location_9_2(self):
        self.assertIsNotNone(self.board[9][2].get_piece())

    def test_black_tile_has_piece_on_location_9_4(self):
        self.assertIsNotNone(self.board[9][4].get_piece())

    def test_black_tile_has_piece_on_location_9_6(self):
        self.assertIsNotNone(self.board[9][6].get_piece())

    def test_black_tile_has_piece_on_location_9_8(self):
        self.assertIsNotNone(self.board[9][8].get_piece())


if __name__ == '__main__':
    unittest.main()