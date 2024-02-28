def error_check(invalid_set_errors, not_enough_pieces):
    with open('errors/invalid_set_errors.txt', 'w') as output_file:
        for error in invalid_set_errors:
            output_file.write(error + "\n")

    with open('errors/not_enough_pieces_errors.txt', 'w') as output_file:
        for error in not_enough_pieces:
            output_file.write(error + "\n")