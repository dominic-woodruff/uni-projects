use std::io;

enum Player {
    X,
    O,
}

struct Game {
    board: [[Option<Player>; 3]; 3],
    current_player: Player,
}

impl Game {
    fn new() -> Game {
        Game {
            board: [[None; 3]; 3],
            current_player: Player::X,
        }
    }

    fn make_move(&mut self, row: usize, col: usize) -> Result<(), &'static str> {
        if row >= 3 || col >= 3 {
            return Err("Invalid move");
        }

        if self.board[row][col].is_some() {
            return Err("Position already occupied");
        }

        self.board[row][col] = Some(self.current_player);

        self.current_player = match self.current_player {
            Player::X => Player::O,
            Player::O => Player::X,
        };

        Ok(())
    }

    fn is_game_over(&self) -> bool {
        // Check rows
        for row in 0..3 {
            if self.board[row][0] == self.board[row][1] && self.board[row][1] == self.board[row][2] {
                if self.board[row][0].is_some() {
                    return true;
                }
            }
        }

        // Check columns
        for col in 0..3 {
            if self.board[0][col] == self.board[1][col] && self.board[1][col] == self.board[2][col] {
                if self.board[0][col].is_some() {
                    return true;
                }
            }
        }

        // Check diagonals
        if self.board[0][0] == self.board[1][1] && self.board[1][1] == self.board[2][2] {
            if self.board[0][0].is_some() {
                return true;
            }
        }

        if self.board[0][2] == self.board[1][1] && self.board[1][1] == self.board[2][0] {
            if self.board[0][2].is_some() {
                return true;
            }
        }

        // Check for a draw
        for row in 0..3 {
            for col in 0..3 {
                if self.board[row][col].is_none() {
                    return false;
                }
            }
        }

        true
    }
}

fn main() {
    let mut game = Game::new();

    loop {
        println!("{:?}", game.board);

        let mut input = String::new();
        io::stdin().read_line(&mut input).expect("Failed to read input");

        let coordinates: Vec<usize> = input
            .trim()
            .split(',')
            .map(|s| s.parse().expect("Invalid input"))
            .collect();

        if coordinates.len() != 2 {
            println!("Invalid input");
            continue;
        }

        let row = coordinates[0];
        let col = coordinates[1];

        match game.make_move(row, col) {
            Ok(_) => {
                if game.is_game_over() {
                    println!("Game over!");
                    break;
                }
            }
            Err(e) => println!("{}", e),
        }
    }
}