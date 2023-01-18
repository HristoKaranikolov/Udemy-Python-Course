username = input('What is your username! - ')
password = input('What is your password! - ')

hidden_password = len(password) * '*'

print(f'{username}, your password {hidden_password} is {len(password)} symbols long.')
