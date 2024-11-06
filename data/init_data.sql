-- Inserting sample users
INSERT INTO
    USER (name, age, gender)
VALUES
    ('Alex Johnson', 29, 'M'),
    ('Taylor Lee', 34, 'F'),
    ('Jordan Kim', 27, 'X'),
    ('Morgan Brown', 41, 'M'),
    ('Casey White', 23, 'F'),
    ('Riley Green', 30, 'X'),
    ('Avery Blue', 36, 'M'),
    ('Jamie Black', 28, 'X'),
    ('Reese Grey', 33, 'F'),
    ('Parker Red', 25, 'M');

-- Inserting sample expense categories
INSERT INTO
    ExpenseCategory (category_name)
VALUES
    ('Housing'),
    ('Utilities'),
    ('Dining'),
    ('Entertainment'),
    ('Transportation'),
    ('Health'),
    ('Insurance'),
    ('Education'),
    ('Miscellaneous');

-- Inserting sample expenses
INSERT INTO
    Expense (user_id, category_id, MONTH, YEAR, amount)
VALUES
    (1, 1, 'Jan', 2024, 800.00),
    (1, 2, 'Jan', 2024, 210.00),
    (1, 3, 'Jan', 2024, 400.00),
    (2, 1, 'Feb', 2024, 820.00),
    (2, 2, 'Feb', 2024, 190.00),
    (2, 3, 'Feb', 2024, 370.00);